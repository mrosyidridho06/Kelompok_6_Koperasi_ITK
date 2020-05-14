from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout, QLabel, QMainWindow
import sys
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QPixmap

from view.gudangInt import inputBarang
from view.simpanPinjam import Tab

class Window(QDialog, QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Menu Koperasi"
        self.top = 500
        self.left = 200
        self.width = 400
        self.height = 100

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon('assets/img/icon.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.setLayout(vbox)



    def createLayout(self):
        self.groupBox = QGroupBox('Pilih Menu')
        hboxlayout = QHBoxLayout()

        self.simpanan = Tab()
        self.setCentralWidget(self.simpanan)

        self.gudang = inputBarang()
        self.setCentraWidget(self.gudang)


        button1 = QPushButton('Simpan Pinjam', self)
        button1.setIcon(QtGui.QIcon('kaki.png'))
        button1.setIconSize(QtCore.QSize(40,40))
        button1.setMinimumHeight(50)
        button1.setMinimumWidth(150)
        hboxlayout.addWidget(button1)
        button1.clicked.connect(self.simpanPinjam)

        button2 = QPushButton('Gudang', self)
        button2.setIcon(QtGui.QIcon('kaki.png'))
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setMinimumHeight(50)
        button2.setMinimumWidth(150)
        hboxlayout.addWidget(button2)
        button2.clicked.connect(self.Gudang)

        self.groupBox.setLayout(hboxlayout)

    def simpanPinjam(self):
        self.simpanan.show()

    def Gudang(self):
        self.gudang.show()

def menu():
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())

