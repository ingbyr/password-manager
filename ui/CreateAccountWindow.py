from datetime import datetime

from PyQt5.QtWidgets import QWidget

import Database
import Cryptor
from ui.widget.AccountWidget import AccountWidget

from ui.widget.CenterWidget import CenterWidget


# 添加某条数据
class CreateAccountWindow(QWidget, CenterWidget):
    def __init__(self, mv):
        super().__init__()
        self.mv = mv
        self.setWindowTitle('添加')
        self.account_widget = AccountWidget()
        self.account_widget.confirm_btn.clicked.connect(self.create_account)
        self.account_widget.cancel_btn.clicked.connect(self.close)
        self.setLayout(self.account_widget.layout)
        self.setGeometry(400, 200, 400, 200)
        self.center()

    def create_account(self):
        an, un, pw, ub = self.account_widget.get_account_info()
        pw = Cryptor.encode(pw)
        if Database.insert_account(an, un, pw, ub,
                                   datetime.now().date()):
            self.account_widget.msg.setText('添加成功')
            self.mv.refresh_data_signal.emit()
        else:
            self.account_widget.msg.setText('存在相同数据')
