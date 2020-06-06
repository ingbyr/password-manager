from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QMenu

import Database
from ui.EditAccountWindow import EditAccountWindow
from ui.widget.AccountTableWidget import AccountTableWidget


class FilterAccountWindow(QWidget):
    refresh_data_signal = pyqtSignal()

    def __init__(self, mv_signal):
        super(FilterAccountWindow, self).__init__()
        self.refresh_data_signal.connect(self.refresh_data)
        self.edit_account_window = EditAccountWindow(mv_signal, self.refresh_data_signal)
        layout = QVBoxLayout()
        layout.setSpacing(20)
        self.tip_label = QLabel()
        layout.addWidget(self.tip_label)
        self.data_table = AccountTableWidget()
        self.data_table.set_item_menu(self.display_menu)
        layout.addWidget(self.data_table)
        self.setLayout(layout)
        self.setGeometry(500, 300, 500, 300)

    def load_data(self, account_name):
        self.account_name = account_name
        self.tip_label.setText('当前账户： ' + self.account_name + '       右键修改或删除数据')
        self.setWindowTitle('当前账户： ' + account_name)
        self.data_table.set_data(Database.select_account_by_account_name(account_name))

    def refresh_data(self):
        self.data_table.set_data(Database.select_account_by_account_name(self.account_name))

    def display_menu(self, pos):
        row_num = -1
        for i in self.data_table.selectionModel().selection().indexes():
            row_num = i.row()
        menu = QMenu()
        edit_action = menu.addAction('修改')
        delete_action = menu.addAction('删除')
        action = menu.exec_(self.data_table.mapToGlobal(pos))

        if action == edit_action:
            account_id = self.data_table.item(row_num, 0).text()
            self.edit_account_window.data_id_signal.emit(int(account_id))
            self.edit_account_window.show()
        elif action == delete_action:
            account_id = self.data_table.item(row_num, 0).text()
            Database.delete_account_by_id(account_id)
            self.refresh_data_signal.emit()
        else:
            return
