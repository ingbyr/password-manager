import os
import pathlib

db_path = pathlib.Path(__file__).parent.joinpath('pm.db').absolute()
backup_dir = pathlib.Path(__file__).parent.joinpath('backup').absolute()

if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)

if __name__ == '__main__':
    print(db_path)
