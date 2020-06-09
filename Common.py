import os
import pathlib

# 数据库路径
db_path = pathlib.Path(__file__).parent.joinpath('pm.db').absolute()

# 备份文件路径
backup_dir = pathlib.Path(__file__).parent.joinpath('backup').absolute()

# 数据的index
ACCOUNT_ID = 0
ACCOUNT_NAME = 1
USERNAME = 2
PASSWORD = 3
USED_BY = 4
DATE = 5

# 密码默认显示方式
PASSWORD_MASK = '******'

if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)
