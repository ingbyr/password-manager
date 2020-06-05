from datetime import datetime

from PyQt5.QtWidgets import QWidget

from db import Database
from ui.AccountWidget import AccountWidget


class CreateAccountWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('添加用户')
        self.account_widget = AccountWidget()
        self.account_widget.confirm_btn.clicked.connect(self.create_account)
        self.account_widget.cancel_btn.clicked.connect(self.close)
        self.setLayout(self.account_widget.layout)
        self.setGeometry(400, 200, 400, 200)

    def create_account(self):
        accoutname, username, password, usedb = self.account_widget.get_account_info()
        if Database.insert_account(accoutname, username,
                                   password, usedb,
                                   datetime.now()):
            self.account_widget.msg.setText('添加成功')
        else:
            self.account_widget.msg.setText('存在相同数据')
