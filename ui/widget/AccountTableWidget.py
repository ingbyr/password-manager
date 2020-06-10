from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem

import Cryptor
from Common import ACCOUNT_ID, PASSWORD, PASSWORD_MASK


# 账户数据列表GUI
class AccountTableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.mask_password = True
        # 账户展示
        self.setColumnCount(6)
        header_labels = ['id', '账户名', '用户名', '密码', '使用者', '创建时间']
        self.setHorizontalHeaderLabels(header_labels)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 调整列显示策略
        for idx, header in enumerate(header_labels):
            if idx == ACCOUNT_ID or idx == len(header_labels):
                self.horizontalHeader().setSectionResizeMode(idx, QHeaderView.ResizeToContents)

    # 添加右键菜单
    def set_item_menu(self, menu_generator):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(menu_generator)

    # 填充数据到table
    def set_data(self, accounts):
        self.setRowCount(0)
        for account in accounts:
            row = self.rowCount()
            self.setRowCount(row + 1)
            for i, d in enumerate(account):
                if i == PASSWORD:
                    if self.mask_password:
                        self.setItem(row, i, QTableWidgetItem(PASSWORD_MASK))
                    else:
                        self.setItem(row, i, QTableWidgetItem(Cryptor.decode(d)))
                else:
                    self.setItem(row, i, QTableWidgetItem(str(d)))
