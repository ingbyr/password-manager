import os
import pickle
from datetime import datetime

from Common import backup_dir


# 备份
def backup(accounts):
    file = backup_dir.joinpath(datetime.now().strftime('%Y%m%d%H%M%S') + '.bin')
    pickle.dump(accounts, open(file, "wb"))
    return file


# 显示所有备份
def list_backups():
    return os.listdir(backup_dir)


# 加载备份
def load_backup(file):
    return pickle.load(open(file, "rb"))
