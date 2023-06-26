import sqlite3 as sql

from settings import config

class DataBase:
    def __init__(self):
        self.con = sql.connect('mail_base.db')
        self.cur = self.con.cursor()
        self.bases = config

    def create_table(self):
        
        self.cur.execute(''' 
            CREATE TABLE IF NOT EXISTS UserMailCredentials (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT,
                mail_server TEXT
            ); ''')
        self.con.commit()

        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS MailUnsubExceptions (
                id INTEGER PRIMARY KEY,
                account_id INTEGER,
                mail_from TEXT,
            );''')
        self.con.commit()

        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS OperationHistory (
                id INTEGER PRIMARY KEY,
                account_id INTEGER,
                uid INTEGER
            ); ''')
            
        self.con.commit()


db = DataBase()
