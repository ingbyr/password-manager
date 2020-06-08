import sqlite3

from Crypto.Random import get_random_bytes

import Encrypt
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
        password BLOB NOT NULL ,
        usedby TEXT DEFAULT '' ,
        datetime TEXT NOT NULL 
    )''')

# 应用设置
cur.execute('''
    CREATE TABLE IF NOT EXISTS app_config
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL ,
        password BLOB NOT NULL ,
        pkey BLOB NOT NULL,
        nonce BLOB NOT NULL
    )''')

conn.commit()


def create_app_account(username, password):
    c = conn.cursor()
    used_username = c.execute('SELECT username From app_config WHERE username = ?', (username,)).fetchone()
    if used_username:
        return False
    else:
        # 随机生成128位密钥，用于密码加密和解密，与账户绑定
        pk = get_random_bytes(16)
        nonce = Encrypt.init_encoder(pk)
        epw = Encrypt.encode(password)
        c.execute(
            'INSERT INTO app_config (username, password, pkey, nonce) VALUES (?, ?, ?, ?)',
            (username, epw, pk, nonce))
        conn.commit()
        login(username, password)
        return True


def login(username, password):
    c = conn.cursor()
    u, p, pk, nonce = c.execute('SELECT username, password, pkey, nonce FROM app_config WHERE username=?',
                                (username,)).fetchone()
    Encrypt.init_encoder(pk)
    Encrypt.init_decoder(pk, nonce)
    p = Encrypt.decode(p)
    if u == username and p == password:
        return True
    else:
        return False


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


def select_all_account():
    c = conn.cursor()
    return c.execute('SELECT * FROM account').fetchall()


def select_account_by_account_name(account_name):
    c = conn.cursor()
    return c.execute('SELECT * FROM account WHERE accountname=?', (account_name,)).fetchall()


def select_account_by_id(data_id):
    c = conn.cursor()
    return c.execute('SELECT accountname, username, password, usedby FROM account WHERE id=?', (data_id,)).fetchone()


def update_account(data_id, an, un, pw, ub, date):
    c = conn.cursor()
    c.execute('UPDATE account '
              'SET accountname = ?, username = ?, password = ?, usedby=?, datetime=? '
              'WHERE id = ?',
              (an, un, pw, ub, date, data_id))
    conn.commit()


def delete_account_by_id(account_id):
    c = conn.cursor()
    c.execute('DELETE FROM account WHERE id = ?', (account_id,))
    conn.commit()


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
        insert_account(account[1], account[2], account[3], account[4], account[5])
