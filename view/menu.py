from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QGroupBox, QLabel, QMainWindow, QGridLayout
import sys
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QPixmap

from view.gudangInt import inputBarang
from view.simpanPinjam import Tab
from view.fileElement.QPushButton import QPushButtonMenu
from view.fileElement.QFrame import QFrameElement

class Window(QDialog, QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowIcon(QtGui.QIcon("view/assets/img/icon.png"))
        self.setWindowTitle("Menu Koperasi")
        self.setGeometry(500, 200, 400, 100)
        vbox = QGridLayout()


        #--------main frame-------
        frame = QFrameElement("rgb(235, 243, 223)")
        frame.setContentsMargins(110, 0, 110, 0)

        boxLayout = QGridLayout(frame)
        boxLayout.setSpacing(100)

        self.simpanan = Tab()
        # self.setCentralWidget(self.simpanan)

        self.gudang = inputBarang()
        # self.setCentraWidget(self.gudang)

        #----------button---------
        self.btnSinjam = QPushButtonMenu("view/assets/img/sinjam.png", "Simpan\nPinjam")
        self.btnSinjam.clicked.connect(self.simpanPinjam)

        self.btnGudang = QPushButtonMenu("view/assets/img/gudang.png", "Gudang")
        self.btnGudang.clicked.connect(self.Gudang)

        #--------layouting--------
        boxLayout.addWidget(self.btnSinjam, 0, 4, 1, 1)
        boxLayout.addWidget(self.btnGudang, 0, 3, 1, 1)

        vbox.addWidget(frame)
        self.setLayout(vbox)

    def simpanPinjam(self):
        from view.simpanPinjam import Tab
        simpan = Tab()
        self.parent().setCentralWidget(simpan)


    def Gudang(self):
        from view.gudangInt import inputBarang
        inputB = inputBarang()
        self.parent().setCentralWidget(inputB)
    # def simpanPinjam(self):
    #     self.parent().simpanPinjamint()
    #
    # def Gudang(self):
    #     self.gudang.show()

# def menu():
#     App = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(App.exec())

