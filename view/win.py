import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from view.login import Login

class mainwin(QMainWindow):
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    def __init__(self):
        super(mainwin, self).__init__()

        self.setWindowTitle('Koperasi ITK')
        self.setWindowIcon(QIcon("view/assets/img/icon.png"))
        self.resize(600, 406)
        self.setMaximumSize(900,506)
        self.setContentsMargins(0, 0, 0, 0)

        self.StyleSheet = """
        QMainWindow{
            background-color: white;
        }
        QPushButton{

        }
        QPushButton:hover{
            background-color: #a3c2c2;
        }
        """
        self.app.setStyleSheet(self.StyleSheet)

        login = Login()
        self.setCentralWidget(login)


