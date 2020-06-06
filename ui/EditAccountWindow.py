from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

import Database
from ui.widget.AccountWidget import AccountWidget


class EditAccountWindow(QWidget):
    data_id_signal = pyqtSignal(int)

    def __init__(self, mv):
        super().__init__()
        self.mv = mv
        self.setWindowTitle('修改')
        self.account_widget = AccountWidget()
        self.account_widget.accountname.setDisabled(True)
        self.account_widget.confirm_btn.clicked.connect(self.save_account)
        self.account_widget.cancel_btn.clicked.connect(self.close)
        self.setLayout(self.account_widget.layout)
        self.setGeometry(400, 200, 400, 200)

        self.data_id_signal.connect(self.init_ui_data)

    @QtCore.pyqtSlot(int)
    def init_ui_data(self, data_id):
        accoutname, username, password, useby = Database.select_account_by_id(data_id)
        self.account_widget.accountname.setText(accoutname)
        self.account_widget.username.setText(username)
        self.account_widget.password.setText(password)
        self.account_widget.usedby.setText(useby)

    def save_account(self):
        accoutname, username, password, useby = self.account_widget.get_account_info()
        if Database.insert_account(accoutname, username,
                                   password, useby,
                                   datetime.now().date()):
            self.account_widget.msg.setText('修改成功')
            self.mv.refresh_data_signal.emit()
        else:
            self.account_widget.msg.setText('修改失败')
