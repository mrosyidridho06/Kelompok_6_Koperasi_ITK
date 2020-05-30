import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QImage, QBrush, QPalette, QIcon
from view.menu import Window

class mainwin(QMainWindow):
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    def __init__(self):
        super(mainwin, self).__init__()

        self.setWindowTitle('Koperasi ITK')
        self.setWindowIcon(QIcon("view/assets/img/icon.png"))
        self.resize(900, 506)
        self.setMaximumSize(900,506)
        self.setContentsMargins(0, 0, 0, 0)

        # im = QImage('asset\Home900.jpg')
        # pal = QPalette()
        # pal.setBrush(10, QBrush(im))
        # self.setPalette(pal)
        self.StyleSheet = """
        QPushButton{
            
        }
        QPushButton:hover{
            background-color: #a3c2c2;
        }
        """
        self.app.setStyleSheet(self.StyleSheet)

        window = Window()
        self.setCentralWidget(window)

    def mMenu(self):
        from view.menu import Window
        self.utama = Window()
        self.setCentralWidget(self.utama)

    def mGudangInt(self):
        from view.gudangInt import inputBarang
        self.gudang = inputBarang()
        self.setCentralWidget(self.gudang)

    def mSimpanpinjamInt(self):
        from view.simpanPinjam import Tab
        self.simpan = Tab()
        self.setCentralWidget(self.simpan)

