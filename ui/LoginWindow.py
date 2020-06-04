from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QLineEdit, QMessageBox, QMainWindow

from db.Database import create_app_account, login
from ui.CenterWidget import CenterWidget


class LoginWindow(QWidget, CenterWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('登陆')
        self.input_account = QLineEdit()
        self.input_password = QLineEdit()
        self.root = QVBoxLayout()
        self.init_ui()
        self.setLayout(self.root)
        self.setGeometry(300, 180, 300, 180)

    def init_ui(self):
        # 账户
        hbox_account = QHBoxLayout()
        label_account = QLabel("用户名")
        hbox_account.addWidget(label_account)
        hbox_account.addWidget(self.input_account)
        self.root.addLayout(hbox_account)

        # 密码
        hbox_password = QHBoxLayout()
        label_password = QLabel("密码")
        self.input_password.setEchoMode(QLineEdit.Password)
        hbox_password.addWidget(label_password)
        hbox_password.addWidget(self.input_password)
        self.root.addLayout(hbox_password)

        # 按钮
        hbox_btn = QHBoxLayout()
        confirm_btn = QPushButton("登陆")
        confirm_btn.clicked.connect(self.do_login)
        hbox_btn.addWidget(confirm_btn)

        register_btn = QPushButton("注册")
        register_btn.clicked.connect(self.do_register)
        hbox_btn.addWidget(register_btn)

        close_btn = QPushButton("关闭")
        close_btn.clicked.connect(self.close)
        hbox_btn.addWidget(close_btn)

        self.root.addLayout(hbox_btn)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def do_login(self):
        account = self.input_account.text()
        password = self.input_password.text()
        if login(account, password):
            self.close()
        else:
            QMessageBox.warning(self, '账户名或密码错误', '账户名或密码错误', QMessageBox.Yes)

    def do_register(self):
        account = self.input_account.text()
        password = self.input_password.text()
        # TODO 检查用户名和密码合法性，并对密码加密
        if create_app_account(account, password):
            QMessageBox.information(self, '注册成功', '注册成功，欢迎用户 ' + account, QMessageBox.Yes)
            self.close()
        else:
            QMessageBox.warning(self, '注册失败', '用户名已被占用', QMessageBox.Close)





