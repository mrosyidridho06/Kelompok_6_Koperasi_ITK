from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout, QLabel, QMainWindow
import sys
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QPixmap

from view.gudangInt import inputBarang
from view.simpanPinjam import Tab

class Window(QDialog, QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowIcon(QtGui.QIcon("view/assets/img/icon.png"))
        self.setWindowTitle("Menu Koperasi")
        self.setGeometry(500, 200, 400, 100)
        self.Tampilan()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupBox)

        self.setLayout(self.vbox)




    def Tampilan(self):
        self.groupBox = QGroupBox('Pilih Menu')
        self.hboxlayout = QHBoxLayout()

        self.simpanan = Tab()
        # self.setCentralWidget(self.simpanan)

        self.gudang = inputBarang()
        # self.setCentraWidget(self.gudang)


        self.button1 = QPushButton('Simpan Pinjam', self)
        self.button1.setIcon(QtGui.QIcon('kaki.png'))
        self.button1.setIconSize(QtCore.QSize(40,40))
        self.button1.setMinimumHeight(50)
        self.button1.setMinimumWidth(150)
        self.hboxlayout.addWidget(self.button1)
        self.button1.clicked.connect(self.simpanPinjam)

        self.button2 = QPushButton('Gudang', self)
        self.button2.setIcon(QtGui.QIcon('kaki.png'))
        self.button2.setIconSize(QtCore.QSize(40,40))
        self.button2.setMinimumHeight(50)
        self.button2.setMinimumWidth(150)
        self.hboxlayout.addWidget(self.button2)
        self.button2.clicked.connect(self.Gudang)

        self.groupBox.setLayout(self.hboxlayout)

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

