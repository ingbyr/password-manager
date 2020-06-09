from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView, QAbstractItemView

import Backup
import Database
from Common import backup_dir

from ui.widget.CenterWidget import CenterWidget


# 数据库备份和加载
class LoadBackupWindow(QWidget, CenterWidget):
    def __init__(self, refresh_signal):
        super(LoadBackupWindow, self).__init__()
        self.refresh_signal = refresh_signal

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.addWidget(QLabel('选择需要加载的备份文件：'))

        self.backups_listview = QListView()
        self.backups_listview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.backups_listview.setSpacing(5)
        self.backups_listview.clicked.connect(self.choose_backup)
        layout.addWidget(self.backups_listview)

        self.setLayout(layout)
        self.center()

    # 选中待加载的备份文件后，重置数据库，添加备份数据到数据库
    def choose_backup(self, idx):
        file = self.backups[idx.row()]
        file = backup_dir.joinpath(file)
        accounts = Backup.load_backup(file)
        Database.restore_accounts(accounts)
        self.refresh_signal.emit()
        self.close()

    # 加载备份文件列表
    def load_backups(self):
        self.backups = Backup.list_backups()
        slm = QStringListModel()
        slm.setStringList(self.backups)
        self.backups_listview.setModel(slm)
