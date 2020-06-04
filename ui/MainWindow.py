from PyQt5.QtWidgets import QWidget, QMainWindow

from ui.CenterWidget import CenterWidget
from ui.LoginWindow import LoginWindow


class MainWindow(QMainWindow, CenterWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Window22222")

        self.login_window = LoginWindow()
        self.check_login()

    def check_login(self):
        self.login_window.show()