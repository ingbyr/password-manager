import pathlib

db_path = pathlib.Path(__file__).parent.joinpath('pm.db').absolute()

if __name__ == '__main__':
    print(db_path)
