import sqlite3

from common import db_path

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 账户数据
cur.execute('''
    CREATE TABLE IF NOT EXISTS account
    (
        id INT PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        comment TEXT
    )''')

# 应用设置
cur.execute('''
    CREATE TABLE IF NOT EXISTS app_config
    (
        id INT PRIMARY KEY,
        username TEXT NOT NULL ,
        password TEXT NOT NULL,
        theme TEXT default 'light'
    )''')

conn.commit()


def create_app_account(username, password):
    c = conn.cursor()
    used_username = c.execute('SELECT username From app_config WHERE username = ?', (username,)).fetchone()
    if used_username:
        return False
    else:
        c.execute(
            'INSERT INTO app_config (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        return True


def login(username, password):
    c = conn.cursor()
    u, p = c.execute('SELECT username, password FROM app_config').fetchone()
    return u == username and p == password
