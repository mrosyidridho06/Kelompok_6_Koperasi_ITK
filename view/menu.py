from PyQt5.QtWidgets import QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QMainWindow
from PyQt5 import QtGui
from view.assets.custom import QPushButtonMenu
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


        self.button1 = QPushButtonMenu("view/assets/img/sinjam.png", "Simpan Pinjam",self.simpanPinjam)
        # self.button1.setIcon(QtGui.QIcon('kaki.png'))
        # self.button1.setIconSize(QtCore.QSize(40,40))
        # self.button1.setMinimumHeight(50)
        # self.button1.setMinimumWidth(150)
        self.hboxlayout.addWidget(self.button1)
        # self.button1.clicked.connect(self.simpanPinjam)

        self.button2 = QPushButtonMenu("view/assets/img/gudang.png", "Gudang",self.Gudang)
        # self.button2.setIcon(QtGui.QIcon('kaki.png'))
        # self.button2.setIconSize(QtCore.QSize(40,40))
        # self.button2.setMinimumHeight(50)
        # self.button2.setMinimumWidth(150)
        self.hboxlayout.addWidget(self.button2)
        # self.button2.clicked.connect(self.Gudang)

        self.groupBox.setLayout(self.hboxlayout)

    def simpanPinjam(self):
        from view.simpanPinjam import Tab
        simpan = Tab()
        self.parent().setCentralWidget(simpan)


    def Gudang(self):
        from view.gudangInt import inputBarang
        inputB = inputBarang()
        self.parent().setCentralWidget(inputB)

