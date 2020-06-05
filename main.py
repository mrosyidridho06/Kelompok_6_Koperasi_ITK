from PyQt5.QtWidgets import QMainWindow, QApplication

from view.login import login
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        self.setWindowTitle("Koperasi ITK")
        self.setGeometry(250, 150, 1100, 650)
        self.setMinimumSize(900, 506)
        self.resize(900, 506)

        widget = login()
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
