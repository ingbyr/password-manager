from PyQt5.QtWidgets import QDesktopWidget


# 组件公共父类，用于将窗口放置屏幕中心
class CenterWidget:

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
