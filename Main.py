import sys

import qtmodern.styles
import qtmodern.windows
from PyQt5.QtWidgets import QApplication

from db.Database import conn
from ui.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(MainWindow())
    mw.show()
    ret = app.exec_()
    conn.close()
    sys.exit(ret)
