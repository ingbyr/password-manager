from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

import Database
from ui.widget.AccountWidget import AccountWidget


class EditAccountWindow(QWidget):
    data_id_signal = pyqtSignal(int)

    def __init__(self, *refresh_signals):
        super().__init__()
        self.refresh_signals = refresh_signals
        self.data_id = -1
        self.setWindowTitle('修改')
        self.account_widget = AccountWidget()
        self.account_widget.confirm_btn.clicked.connect(self.save_account)
        self.account_widget.cancel_btn.clicked.connect(self.close)
        self.setLayout(self.account_widget.layout)
        self.setGeometry(400, 200, 400, 200)

        self.data_id_signal.connect(self.init_ui_data)

    @QtCore.pyqtSlot(int)
    def init_ui_data(self, data_id):
        an, un, pw, ub = Database.select_account_by_id(data_id)
        self.data_id = data_id
        self.account_widget.accountname.setText(an)
        self.account_widget.username.setText(un)
        self.account_widget.password.setText(pw)
        self.account_widget.usedby.setText(ub)

    def save_account(self):
        an, un, pw, ub = self.account_widget.get_account_info()
        Database.update_account(self.data_id, an, un, pw, ub, datetime.now().date())
        for signal in self.refresh_signals:
            signal.emit()
        self.close()
