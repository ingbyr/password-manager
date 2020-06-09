import sys

from PyQt5.QtWidgets import QApplication

from Database import conn
from ui.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # qtmodern.styles.dark(app)
    # mw = qtmodern.windows.ModernWindow(MainWindow())
    # mw.show()
    MainWindow().show()

    ret = app.exec_()
    conn.close()
    sys.exit(ret)
