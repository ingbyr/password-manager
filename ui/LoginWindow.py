from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QPushButton


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.tabs = QTabWidget()

        self.init_login_tab()
        self.init_register_tab()
        self.vbox.addWidget(self.tabs)
        self.setLayout(self.vbox)

    def init_login_tab(self):
        login_tab = QWidget()

        hbox = QHBoxLayout()
        confirm_btn = QPushButton("登陆")
        confirm_btn.clicked.connect(self.login_confirm)
        hbox.addWidget(confirm_btn)
        close_btn = QPushButton("关闭")
        close_btn.clicked.connect(self.close)
        hbox.addWidget(close_btn)

        login_tab.setLayout(hbox)

        self.tabs.addTab(login_tab, "登陆")

    def init_register_tab(self):
        tab_register = QWidget()
        self.tabs.addTab(tab_register, "注册")

    def login_confirm(self):
        print('login confirm')