from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, \
    QLineEdit, QMessageBox, QGridLayout

from Database import create_app_account, login
from ui.widget.CenterWidget import CenterWidget


class LoginWindow(QWidget, CenterWidget):
    def __init__(self, mv):
        super().__init__()
        self.mv = mv
        self.setWindowTitle('登陆')
        self.account = QLineEdit()
        self.password = QLineEdit()
        self.init_ui()
        self.setGeometry(300, 150, 300, 150)

    def init_ui(self):

        grid = QGridLayout()
        grid.setSpacing(15)
        # 账户
        grid.addWidget(QLabel('用户名'), 1, 0)
        grid.addWidget(self.account, 1, 1)

        # 密码
        grid.addWidget(QLabel('密码'), 2, 0)
        grid.addWidget(self.password, 2, 1)

        # 按钮
        hbox_btn = QHBoxLayout()
        hbox_btn.setSpacing(5)
        confirm_btn = QPushButton("登陆")
        confirm_btn.clicked.connect(self.do_login)
        hbox_btn.addWidget(confirm_btn)

        register_btn = QPushButton("注册")
        register_btn.clicked.connect(self.do_register)
        hbox_btn.addWidget(register_btn)

        close_btn = QPushButton("关闭")
        close_btn.clicked.connect(self.quit)
        hbox_btn.addWidget(close_btn)
        btns = QWidget()
        btns.setLayout(hbox_btn)
        grid.addWidget(btns, 3, 0, 1, 2)

        self.setLayout(grid)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def do_login(self):
        account = self.account.text()
        password = self.password.text()
        if login(account, password):
            self.open_main_window()
        else:
            QMessageBox.warning(self, '账户名或密码错误', '账户名或密码错误', QMessageBox.Yes)

    def do_register(self):
        account = self.account.text()
        password = self.password.text()
        # TODO 检查用户名和密码合法性，并对密码加密
        if create_app_account(account, password):
            QMessageBox.information(self, '注册成功', '注册成功，欢迎用户 ' + account, QMessageBox.Yes)
            self.open_main_window()
        else:
            QMessageBox.warning(self, '注册失败', '用户名已被占用', QMessageBox.Close)

    def open_main_window(self):
        self.close()
        self.mv.init_signal.emit()

    def quit(self):
        self.close()
        self.mv.quit_signal.emit()

