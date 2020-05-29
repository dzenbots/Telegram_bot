import os

from peewee import SqliteDatabase, Model, CharField

from settings import DB_FILE_PATH

db = SqliteDatabase(DB_FILE_PATH)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    telegram_id = CharField(unique=True)
    reg_status = CharField()


def init_db():
    db.connect()
    db.create_tables([
        User
    ], safe=True)
