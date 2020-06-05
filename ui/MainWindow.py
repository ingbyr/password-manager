from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QPushButton, QWidget, QTableWidget, QHeaderView, QTableWidgetItem

from db.Database import select_all_account
from ui.CenterWidget import CenterWidget
from ui.CreateAccountWindow import CreateAccountWindow
from ui.LoginWindow import LoginWindow


class MainWindow(QMainWindow, CenterWidget):
    quit_signal = pyqtSignal()
    init_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        self.table = QTableWidget()
        self.setWindowTitle('密码管理器')

        # 订阅信号
        self.quit_signal.connect(self.close)
        self.init_signal.connect(self.init_ui)

        # 登陆
        self.login_window = LoginWindow(self)
        # TODO uncomment below
        # self.open_login_window()
        self.init_ui()

        # 创建账户
        self.account_window = CreateAccountWindow()

    # 加载主窗口UI和数据
    def init_ui(self):
        grid = QGridLayout()
        grid.setSpacing(20)
        root = QWidget()
        root.setLayout(grid)
        self.setCentralWidget(root)

        create_account_btn = QPushButton('添加')
        create_account_btn.clicked.connect(self.open_account_window)
        grid.addWidget(create_account_btn, 1, 0)

        local_backup_btn = QPushButton('本地备份')
        local_backup_btn.clicked.connect(self.local_backup_data)
        grid.addWidget(local_backup_btn, 1, 1)

        cloud_backup_btn = QPushButton('云端备份')
        cloud_backup_btn.clicked.connect(self.cloud_backup_data)
        grid.addWidget(cloud_backup_btn, 1, 2)

        # 账户展示
        self.table.setColumnCount(6)
        header_labels = ['id', '账户名', '用户名', '密码', '使用者', '创建时间']
        self.table.setHorizontalHeaderLabels(header_labels)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for idx, header in enumerate(header_labels):
            if idx == 0 or idx == len(header_labels):
                self.table.horizontalHeader().setSectionResizeMode(idx, QHeaderView.ResizeToContents)
        grid.addWidget(self.table, 2, 0, 4, 3)
        # 从数据库加载
        self.load_data()

    # 登陆窗口
    def open_login_window(self):
        self.login_window.show()

    # 添加账户数据
    def open_account_window(self):
        self.account_window.show()

    def local_backup_data(self):
        pass

    def cloud_backup_data(self):
        pass

    def load_data(self):
        accounts = select_all_account()
        print(accounts)
        for account in accounts:
            row = self.table.rowCount()
            self.table.setRowCount(row + 1)
            for i, d in enumerate(account):
                self.table.setItem(row, i, QTableWidgetItem(d))
