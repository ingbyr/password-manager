from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QVBoxLayout

import Database
from ui.widget.AccountTableWidget import AccountTableWidget


class AccountWindow(QWidget):

    def __init__(self):
        super(AccountWindow, self).__init__()
        layout = QVBoxLayout()
        layout.setSpacing(20)

        layout.addWidget(QLabel('右键修改或删除数据'))
        self.data_table = AccountTableWidget()
        layout.addWidget(self.data_table)
        self.setLayout(layout)
        self.setGeometry(500, 300, 500, 300)

    def load_data(self, accountname):
        self.setWindowTitle('当前账户： ' + accountname)
        self.data_table.set_data(Database.select_account_by_accountname(accountname))
