from PyQt5.QtWidgets import QDesktopWidget


class CenterWidget:
    def __init__(self):
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
