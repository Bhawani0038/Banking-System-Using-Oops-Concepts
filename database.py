# database.py

import pymysql as mq

class Database:
    def __init__(self):
        self.myobj = mq.connect(
            host='localhost',
            user='root',
            password='',
            database='bank_database')
        self.cursorobj = self.myobj.cursor()
        self.create_table()

    def create_table(self):
        ct = '''CREATE TABLE IF NOT EXISTS data(id INT primary key auto_increment, password varchar(5),
        Name varchar(25), Account_Balance INT, Phone_no INT)'''
        self.cursorobj.execute(ct)

    def execute_query(self, query,value=None):
        self.cursorobj.execute(query,value)

    def commit(self):
        self.myobj.commit()

    def fetch_one(self):
        return self.cursorobj.fetchone()

    def close_connection(self):
        self.cursorobj.close()
        self.myobj.close()
