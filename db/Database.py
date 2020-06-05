import datetime
import sqlite3

from Common import db_path

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 账户数据
cur.execute('''
    CREATE TABLE IF NOT EXISTS account
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        accountname TEXT NOT NULL ,
        username TEXT NOT NULL ,
        password TEXT NOT NULL ,
        usedby TEXT DEFAULT '' ,
        datetime TEXT NOT NULL 
    )''')

# 应用设置
cur.execute('''
    CREATE TABLE IF NOT EXISTS app_config
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL ,
        password TEXT NOT NULL ,
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


def insert_account(accountname, username, password, usedby, datetime):
    c = conn.cursor()
    res = c.execute('SELECT accountname FROM account WHERE accountname=? and username=? and usedby=?',
                    (accountname, username, usedby)).fetchone()
    if not res:
        c.execute('INSERT INTO account (accountname, username, password, usedby, datetime) VALUES (?, ?, ?, ?, ?)',
                  (accountname, username, password, usedby, datetime))
        conn.commit()
        return True
    else:
        return False
