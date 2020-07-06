# todo app

## directroy

.
|- run.py           : サーバー立ち上げ
|- urls.py          : urlのルーティング
|- controllers.py   : レスポンス処理用
|- db.py            : sqlite3の基底クラス
|- models.py        : モデルの定義（sqlite3のテーブル定義）
|- templates
　　|- layout.html : 基本的なレイアウト
　　|- index.htmle : はじめに入るページ
　　|- admin.html  : 管理者用ページ

## 開発用サーバ立ち上げ

```bash
python3 run.py
```

## reference

- [1] [FastAPIチュートリアル: ToDoアプリを作ってみよう](https://rightcode.co.jp/blog/information-technology/fastapi-tutorial-todo-apps-environment)
