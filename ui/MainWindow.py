from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from qtmodern.windows import ModernWindow

from ui.LoginWindow import LoginWindow


class MainWindow(ModernWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.login_window = LoginWindow()
        self.init_ui()

    def init_ui(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
