# MVCモデルのcontroller
# FastAPIのインスタンスを生成
# create instance of FastAPI
# urls.pyでURLに紐づく関数を定義する
# Depends and HTTPException is necessary for using 'Basic Authentication'
from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.status import HTTP_401_UNAUTHORIZED

import db
from models import User, Task
from mycalendar import MyCalendar
from auth import auth

import hashlib
from datetime import datetime, timedelta

app = FastAPI(
    title = "TODO appliccation created by FastApi",
)

security = HTTPBasic()

# settings relating templates
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env # jinja2.Environment : settings for filter or global

# make pattern confirm whether input data is correct or incorrect.
import re  # new
pattern = re.compile(r'\w{4,20}')  # 任意の4~20の英数字を示す正規表現
pattern_pw = re.compile(r'\w{6,20}')  # 任意の6~20の英数字を示す正規表現
pattern_mail = re.compile(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')  # e-mailの正規表現



def index(request : Request):
    return templates.TemplateResponse("index.html",
                                    {"request" : request})

# 管理者ページ
def admin(request : Request, credentials : HTTPBasicCredentials = Depends(security)):
    # the information getted by 'Basic Authentication'
    username = auth(credentials)

    # get timestamp of today and nextweek
    today = datetime.now()
    next_w = today + timedelta(days=7)

    # get the data whose username is same with username from database
    user = db.session.query(User).filter(User.username == username).first()
    task = db.session.query(Task).filter(Task.user_id == user.id).all()

    # after getting data, you must always close session to the database
    db.session.close()

    # from here, related to calendar
    # get calendar HTML form
    cal = MyCalendar(
        username,
        {t.deadline.strftime("%Y%m%d") : t.done for t in task}
    )

    cal = cal.formatyear(today.year, 4)

    # rewrite task list
    task = [t for t in task if today <= t.deadline <= next_w]
    links = [t.deadline.strftime("/todo/" + username + "%Y%m%d") for t in task]

    # if no problem, jumps to admin page
    return templates.TemplateResponse("admin.html",
                                    {"request" : request,
                                    "user" : user,
                                    "task" : task,
                                    "links" : links,
                                    "calendar" : cal})

# for register
async def register(request : Request):
    if request.method == "GET":
        return templates.TemplateResponse("register.html",
                                        {"request" : request,
                                        "username" : "",
                                        "error" : []})

    if request.method == "POST":
        # post data
        data = await request.form()
        username = data.get("username")
        password = data.get("password")
        password_tmp = data.get("password_tmp")
        mail = data.get("mail")

        error = []

        tmp_user = db.session.query(User).filter(User.username == username).first()
 
        # 怒涛のエラー処理
        # error handling
        if tmp_user is not None:
            error.append('同じユーザ名のユーザが存在します。')
        if password != password_tmp:
            error.append('入力したパスワードが一致しません。')
        if pattern.match(username) is None:
            error.append('ユーザ名は4~20文字の半角英数字にしてください。')
        if pattern_pw.match(password) is None:
            error.append('パスワードは6~20文字の半角英数字にしてください。')
        if pattern_mail.match(mail) is None:
            error.append('正しくメールアドレスを入力してください。')
 
        # エラーがあれば登録ページへ戻す
        # if error is exist, get back to registeraion page
        if error:
            return templates.TemplateResponse('register.html',
                                              {'request': request,
                                               'username': username,
                                               'error': error})
 
        # 問題がなければユーザ登録
        # if error is not exist, register the user information to database
        user = User(username, password, mail)
        db.session.add(user)
        db.session.commit()
        db.session.close()
 
        return templates.TemplateResponse('complete.html',
                                          {'request': request,
                                           'username': username})


def detail(
    request : Request, username, year, month, day,
    credentials : HTTPBasicCredentials = Depends(security)
):

    """URLパターンは引数で取得可能
    """

    # whether authentication is Ok or Not ?
    username_tmp = auth(credentials)

    # if other user get in , block the user
    if username_tmp != username:
        return RedirectResponse("/")

    # get login user
    user = db.session.query(User).filter(User.username == username).first()
    # get tasks of the user
    task = db.session.query(Task).filter(Task.user_id == user.id).all()
    db.session.close()

    # aggregate list which have timestamp is same to target timestamp
    # monthes and days is dropped '0' 
    theday = "{}{}{}".format(year, month.zfill(2), day.zfill(2))
    task = [t for t in task if t.deadline.strftime("%Y%m%d") == theday]

    return templates.TemplateResponse("detail.html",
                                    {'request': request,
                                    "username": username,
                                    "task" : task,
                                    "year" : year,
                                    "month" : month,
                                    "day": day})

async def done(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    # 認証OK？
    username = auth(credentials)
 
    # ユーザ情報を取得
    user = db.session.query(User).filter(User.username == username).first()
 
    # ログインユーザのタスクを取得
    task = db.session.query(Task).filter(Task.user_id == user.id).all()
 
    # フォームで受け取ったタスクの終了判定を見て内容を変更する
    data = await request.form()
    t_dones = data.getlist('done[]')  # リストとして取得
 
    for t in task:
        if str(t.id) in t_dones:  # もしIDが一致すれば "終了した予定" とする
            t.done = True
 
    db.session.commit()  # update!!
    db.session.close()
 
    return RedirectResponse('/admin')  # 管理者トップへリダイレクト


async def add(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    # 認証
    username = auth(credentials)
 
    # ユーザ情報を取得
    user = db.session.query(User).filter(User.username == username).first()
 
    # フォームからデータを取得
    data = await request.form()
    print("data is {}".format(data))
    year = int(data['year'])
    month = int(data['month'])
    day = int(data['day'])
    hour = int(data['hour'])
    minute = int(data['minute'])
 
    deadline = datetime(year=year, month=month, day=day,
                        hour=hour, minute=minute)
 
    # 新しくタスクを生成しコミット
    task = Task(user.id, data['content'], deadline)
    db.session.add(task)
    db.session.commit()
    db.session.close()
 
    return RedirectResponse('/admin')


def delete(request: Request, t_id, credentials: HTTPBasicCredentials = Depends(security)):
    # 認証
    username = auth(credentials)
 
    # ログインユーザ情報を取得
    user = db.session.query(User).filter(User.username == username).first()
 
    # 該当タスクを取得
    task = db.session.query(Task).filter(Task.id == t_id).first()
 
    # もしユーザIDが異なれば削除せずリダイレクト
    if task.user_id != user.id:
        return RedirectResponse('/admin')
 
    # 削除してコミット
    db.session.delete(task)
    db.session.commit()
    db.session.close()
 
    return RedirectResponse('/admin')



def get(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    # 認証
    username = auth(credentials)

    # ユーザ情報を取得
    user = db.session.query(User).filter(User.username == username).first()

    # タスクを取得
    task = db.session.query(Task).filter(Task.user_id == user.id).all()

    db.session.close()

    # JSONフォーマット
    task = [{
        'id': t.id,
        'content': t.content,
        'deadline': t.deadline.strftime('%Y-%m-%d %H:%M:%S'),
        'published': t.date.strftime('%Y-%m-%d %H:%M:%S'),
        'done': t.done,
    } for t in task]

    return task



async def insert(request: Request,
                 content: str = Form(...), deadline: str = Form(...),
                 credentials: HTTPBasicCredentials = Depends(security)):
    """
    タスクを追加してJSONで新規タスクを返す。「deadline」は%Y-%m-%d_%H:%M:%S (e.g. 2019-11-03_12:30:00)の形式
    """
    # 認証
    username = auth(credentials)
 
    # ユーザ情報を取得
    user = db.session.query(User).filter(User.username == username).first()
 
    # タスクを追加
    task = Task(user.id, content, datetime.strptime(deadline, '%Y-%m-%d_%H:%M:%S'))
 
    db.session.add(task)
    db.session.commit()
 
    # テーブルから新しく追加したタスクを取得する
    task = db.session.query(Task).all()[-1]
    db.session.close()
 
    # 新規タスクをJSONで返す
    return {
        'id': task.id,
        'content': task.content,
        'deadline': task.deadline.strftime('%Y-%m-%d %H:%M:%S'),
        'published': task.date.strftime('%Y-%m-%d %H:%M:%S'),
        'done': task.done,
    }