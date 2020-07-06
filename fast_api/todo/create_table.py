from models import *
import db
import os


if __name__ == '__main__':
    path = SQLITE_NAME
    if not os.path.isfile(path):
        # create tables
        Base.metadata.create_all(db.engine)

    # create tables for sample user(e.g. admin)
    admin = User(
        username="admin",
        password="fastapi",
        mail="hoge@example.com"
    )
    # add admin to database
    db.session.add(admin)
    # commit to database
    db.session.commit()

    # create sample task
    task = Task(
        user_id = admin.id,
        content = "deadline of hogehoge",
        deadline = datetime(2019, 12, 25, 12, 00, 00)
    )

    print(task)
    db.session.add(task)
    db.session.commit()

    # close session to database
    db.session.close()
