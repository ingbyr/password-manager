import sqlite3

from common import db_path

conn = sqlite3.connect(db_path)


def create_tables():
    c = conn.cursor()

    # 应用账户
    c.execute('''
        CREATE TABLE IF NOT EXISTS app_account  
        (
            id INT PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # 账户数据
    c.execute('''
        CREATE TABLE IF NOT EXISTS account
        (
            id INT PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            comment TEXT,

        )
    ''')

    conn.commit()
