from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QPushButton, QWidget, QMenu, QMessageBox

import Backup
import Database
from ui.CreateAccountWindow import CreateAccountWindow
from ui.EditAccountWindow import EditAccountWindow
from ui.FilterAccountWindow import FilterAccountWindow
from ui.BackupWindow import LoadBackupWindow
from ui.LoginWindow import LoginWindow
from ui.widget.AccountTableWidget import AccountTableWidget
from ui.widget.CenterWidget import CenterWidget


# 主窗口
class MainWindow(QMainWindow, CenterWidget):
    quit_signal = pyqtSignal()
    init_signal = pyqtSignal()
    refresh_data_signal = pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('密码管理器')

        # 订阅信号
        self.quit_signal.connect(self.close)
        self.init_signal.connect(self.init_ui)
        self.refresh_data_signal.connect(self.load_data)

        # 登陆
        self.login_window = LoginWindow(self)
        self.open_login_window()

        # 创建账户
        self.create_account_window = CreateAccountWindow(self)
        self.edit_account_window = EditAccountWindow(self.refresh_data_signal)

        # 账户数据
        self.account_table = AccountTableWidget()

        # 单个账户数据
        self.account_window = FilterAccountWindow(self.refresh_data_signal)

        # 加载备份数据
        self.load_backup_window = LoadBackupWindow(self.refresh_data_signal)

        self.setGeometry(500, 500, 500, 500)
        self.center()

    # 加载主窗口
    def init_ui(self):
        self.center()
        grid = QGridLayout()
        grid.setSpacing(20)
        root = QWidget()
        root.setLayout(grid)
        self.setCentralWidget(root)

        create_account_btn = QPushButton('添加')
        create_account_btn.clicked.connect(self.open_account_window)
        grid.addWidget(create_account_btn, 1, 0)

        self.change_pw_way_text = {
            False: '不显示明文',
            True: '显示明文'
        }
        self.change_pw_way_btn = QPushButton(self.change_pw_way_text[self.account_table.mask_password])
        self.change_pw_way_btn.clicked.connect(self.change_pw_way)
        grid.addWidget(self.change_pw_way_btn, 1, 1)

        local_backup_btn = QPushButton('备份数据')
        local_backup_btn.clicked.connect(self.local_backup_data)
        grid.addWidget(local_backup_btn, 1, 2)

        load_backup_btn = QPushButton('加载备份')
        load_backup_btn.clicked.connect(self.load_backup_data)
        grid.addWidget(load_backup_btn, 1, 3)

        # 账户展示
        self.account_table.set_item_menu(self.display_menu)
        self.load_data()
        grid.addWidget(self.account_table, 2, 0, 4, 4)

    # 登陆窗口
    def open_login_window(self):
        self.login_window.show()
        self.login_window.center()

    # 添加账户数据
    def open_account_window(self):
        self.create_account_window.show()

    # 备份本地数据库
    def local_backup_data(self):
        file = Backup.backup(Database.select_all_account())
        QMessageBox.information(self, '备份成功', '备份文件： ' + str(file))

    # 加载备份
    def load_backup_data(self):
        self.load_backup_window.load_backups()
        self.load_backup_window.show()

    # 切换密码明文显示
    def change_pw_way(self):
        self.account_table.mask_password = not self.account_table.mask_password
        self.change_pw_way_btn.setText(self.change_pw_way_text[self.account_table.mask_password])
        self.load_data()

    # 加载数据到 table view
    def load_data(self):
        self.account_table.set_data(Database.select_all_account())

    def display_menu(self, pos):
        row_num = -1
        for i in self.account_table.selectionModel().selection().indexes():
            row_num = i.row()
        menu = QMenu()
        find_action = menu.addAction('显示该账户所有数据')
        edit_action = menu.addAction('修改')
        delete_action = menu.addAction('删除')
        action = menu.exec_(self.account_table.mapToGlobal(pos))

        if action == find_action:
            an = self.account_table.item(row_num, 1).text()
            self.account_window.load_data(an)
            self.account_window.show()
        elif action == edit_action:
            account_id = self.account_table.item(row_num, 0).text()
            self.edit_account_window.data_id_signal.emit(int(account_id))
            self.edit_account_window.show()
        elif action == delete_action:
            account_id = self.account_table.item(row_num, 0).text()
            Database.delete_account_by_id(account_id)
            self.refresh_data_signal.emit()
        else:
            return
