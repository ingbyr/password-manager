import sqlite3

from Crypto.Random import get_random_bytes

import Cryptor
from Common import *

# 连接数据库 Sqlite3
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 账户数据表
cur.execute('''
    CREATE TABLE IF NOT EXISTS account
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        accountname TEXT NOT NULL ,
        username TEXT NOT NULL ,
        password BLOB NOT NULL ,
        usedby TEXT DEFAULT '' ,
        datetime TEXT NOT NULL 
    )''')

# 应用设置表
cur.execute('''
    CREATE TABLE IF NOT EXISTS app_config
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL ,
        password BLOB NOT NULL ,
        pkey BLOB NOT NULL
    )''')

conn.commit()


# 创建应用账户
def create_app_account(username, password):
    c = conn.cursor()
    used_username = c.execute('SELECT username From app_config WHERE username = ?', (username,)).fetchone()
    if used_username:
        return False
    else:
        # 随机生成128位密钥，用于密码加密和解密，与账户绑定
        pk = get_random_bytes(16)
        Cryptor.init(pk)
        epw = Cryptor.encode(password)
        c.execute(
            'INSERT INTO app_config (username, password, pkey) VALUES (?, ?, ?)',
            (username, epw, pk))
        conn.commit()
        login(username, password)
        return True


# 是否已创建应用账户
def exist_app_account():
    c = conn.cursor()
    app_config = c.execute('SELECT * From app_config').fetchone()
    return app_config is None


# 验证应用登陆信息
def login(username, password):
    c = conn.cursor()
    u, p, pk = c.execute('SELECT username, password, pkey FROM app_config WHERE username=?',
                         (username,)).fetchone()
    Cryptor.init(pk)
    p = Cryptor.decode(p)
    if u == username and p == password:
        return True
    else:
        return False


# 添加数据
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


# 检索所有数据
def select_all_account():
    c = conn.cursor()
    return c.execute('SELECT * FROM account').fetchall()


# 检索某账户名下所有数据
def select_account_by_account_name(account_name):
    c = conn.cursor()
    return c.execute('SELECT * FROM account WHERE accountname=?', (account_name,)).fetchall()


# 通过id检索数据
def select_account_by_id(data_id):
    c = conn.cursor()
    an, un, pw, ub = c.execute('SELECT accountname, username, password, usedby FROM account WHERE id=?',
                               (data_id,)).fetchone()
    pw = Cryptor.decode(pw)
    return an, un, pw, ub


# 更新id为data_id的数据
def update_account(data_id, an, un, pw, ub, date):
    c = conn.cursor()
    pw = Cryptor.encode(pw)
    c.execute('UPDATE account '
              'SET accountname = ?, username = ?, password = ?, usedby=?, datetime=? '
              'WHERE id = ?',
              (an, un, pw, ub, date, data_id))
    conn.commit()


# 删除data_id的数据
def delete_account_by_id(account_id):
    c = conn.cursor()
    c.execute('DELETE FROM account WHERE id = ?', (account_id,))
    conn.commit()


# 重置数据
def restore_accounts(accounts):
    c = conn.cursor()
    c.execute('DROP TABLE account')
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
    for account in accounts:
        insert_account(account[ACCOUNT_NAME], account[USERNAME], account[PASSWORD], account[USED_BY],
                       account[DATE])
