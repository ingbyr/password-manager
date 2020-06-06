from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QPushButton, QWidget, QMenu

from Database import select_all_account
from ui.AccountWindow import AccountWindow
from ui.EditAccountWindow import EditAccountWindow
from ui.widget.AccountTableWidget import AccountTableWidget
from ui.widget.CenterWidget import CenterWidget
from ui.CreateAccountWindow import CreateAccountWindow
from ui.LoginWindow import LoginWindow


class MainWindow(QMainWindow, CenterWidget):
    quit_signal = pyqtSignal()
    init_signal = pyqtSignal()
    refresh_data_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('密码管理器')

        # 订阅信号
        self.quit_signal.connect(self.close)
        self.init_signal.connect(self.init_ui)
        self.refresh_data_signal.connect(self.load_data)

        # 登陆
        self.login_window = LoginWindow(self)
        # TODO uncomment below
        # self.open_login_window()

        # 创建账户
        self.create_account_window = CreateAccountWindow(self)
        self.edite_account_window = EditAccountWindow(self)

        # 账户数据
        self.data_table = AccountTableWidget()

        # 单个账户数据
        self.account_window = AccountWindow()

        self.init_ui()

    # 加载主窗口
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
        self.data_table.set_item_menu(self.display_menu)
        self.load_data()
        grid.addWidget(self.data_table, 2, 0, 4, 3)

    # 登陆窗口
    def open_login_window(self):
        self.login_window.show()

    # 添加账户数据
    def open_account_window(self):
        self.create_account_window.show()

    def local_backup_data(self):
        pass

    def cloud_backup_data(self):
        pass

    # 加载数据到 table view
    def load_data(self):
        accounts = select_all_account()
        self.data_table.set_data(accounts)

    def display_menu(self, pos):
        row_num = -1
        for i in self.data_table.selectionModel().selection().indexes():
            row_num = i.row()

        menu = QMenu()
        find_action = menu.addAction('显示该账户所有数据')
        edit_action = menu.addAction('修改')
        delete_action = menu.addAction('删除')
        action = menu.exec_(self.data_table.mapToGlobal(pos))

        if action == find_action:
            accountname = self.data_table.item(row_num, 1).text()
            self.account_window.load_data(accountname)
            self.account_window.show()
        elif action == edit_action:
            data_id = self.data_table.item(row_num, 0).text()
            self.edite_account_window.data_id_signal.emit(int(data_id))
            self.edite_account_window.show()
        elif action == delete_action:
            pass
        else:
            return
