from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QHBoxLayout


# 某条账户数据的GUI
class AccountWidget(QWidget):
    def __init__(self):
        super().__init__()
        label_account = QLabel('账户名')
        label_username = QLabel('用户名')
        label_password = QLabel('密码')
        label_usedby = QLabel('应用或网站')

        self.accountname = QLineEdit()
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.usedby = QLineEdit()

        hbox_btn = QHBoxLayout()
        hbox_btn.setSpacing(5)
        self.confirm_btn = QPushButton('确认')
        self.cancel_btn = QPushButton('关闭')
        self.msg = QLabel()
        hbox_btn.addWidget(self.msg)
        hbox_btn.addStretch(1)
        hbox_btn.addWidget(self.confirm_btn)
        hbox_btn.addWidget(self.cancel_btn)
        widget_btn = QWidget()
        widget_btn.setLayout(hbox_btn)

        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.layout.addWidget(label_account, 1, 0)
        self.layout.addWidget(self.accountname, 1, 1)
        self.layout.addWidget(label_username, 2, 0)
        self.layout.addWidget(self.username, 2, 1)
        self.layout.addWidget(label_password, 3, 0)
        self.layout.addWidget(self.password, 3, 1)
        self.layout.addWidget(label_usedby, 4, 0)
        self.layout.addWidget(self.usedby, 4, 1)
        self.layout.addWidget(widget_btn, 5, 0, 1, 2)

    def get_account_info(self):
        accountname = self.accountname.text()
        username = self.username.text()
        password = self.password.text()
        usedby = self.usedby.text()
        return accountname, username, password, usedby
