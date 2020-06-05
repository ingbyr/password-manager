from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QPushButton, QWidget

from ui.CenterWidget import CenterWidget
from ui.CreateAccountWindow import CreateAccountWindow
from ui.LoginWindow import LoginWindow


class MainWindow(QMainWindow, CenterWidget):
    load_data_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('密码管理器')

        # 订阅信号
        self.load_data_signal.connect(self.load_data)

        # 登陆
        self.login_window = LoginWindow(self)
        self.check_login()

        # 创建账户
        self.account_window = CreateAccountWindow()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        root = QWidget()
        root.setLayout(grid)
        self.setCentralWidget(root)

        create_account_btn = QPushButton('添加')
        create_account_btn.clicked.connect(self.open_account_window)
        grid.addWidget(create_account_btn, 1, 0)

    def check_login(self):
        self.login_window.show()

    def load_data(self):
        pass

    def open_account_window(self):
        self.account_window.show()
