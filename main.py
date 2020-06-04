import sys

import qtmodern.styles
import qtmodern.windows
from PyQt5.QtWidgets import QApplication

from ui.LoginWindow import LoginWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(LoginWindow())
    mw.show()
    sys.exit(app.exec_())
