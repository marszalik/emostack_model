from __future__ import annotations
from services.Singleton import Singleton
from sqlalchemy import create_engine, text


@Singleton
class DbSrv:

    def __init__(self):

        self.db = create_engine('sqlite:///emostack.db').connect()

    def conn(self):
        return self.db

    def query(self, sql):
        return text(sql)
