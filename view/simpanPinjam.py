from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from database.SimpanPinjamORM import SimpanPinjamORM
from view.sijamView import simpanPinjam

import sys

from view.fileElement.QPushButton import QPushButtonGeneral
from view.fileElement.QFrame import QFrameElement
from view.fileElement.QLabel import QLabelElement

class Tab(QDialog):
    def __init__(self):
        super().__init__()
        # self.setGeometry(200,200,500,300)
        # self.setWindowTitle('SimpanPinjam')
        # self.setWindowIcon(QtGui.QIcon("view/assets/img/icon.png"))

        #--------main Layout-------
        vbox = QGridLayout()

        frame = QFrameElement("rgb(235, 243, 223)")

        boxLayout = QGridLayout(frame)
        boxLayout.setSpacing(20)

        self.report = simpanPinjam()
        self.lapor = QPushButtonGeneral("Laporan")
        self.lapor.setStyleSheet("height : 20%;" "color : white;" "background-color : rgb(184, 220, 124);")
        self.lapor.clicked.connect(self.Lihat)

        self.backnya = QPushButtonGeneral("Back")
        self.backnya.setStyleSheet("height : 20%;" "color : white;" "background-color : rgb(184, 220, 124);")
        self.backnya.clicked.connect(self.back_btn)

        #--------Tab Widget-------
        tabWidget = QTabWidget()
        tabWidget.addTab(inputSimpan(), 'Simpan')
        tabWidget.addTab(inputPinjam(), 'Pinjam')

        #--------layouting--------
        vbox.addWidget(tabWidget)
        vbox.addWidget(self.lapor,1,0)
        vbox.addWidget(self.backnya,2,0)
        self.setLayout(vbox)

    def back_btn(self):
        from view.menu import Window
        self.parent().setCentralWidget(Window())

    def Lihat(self):
        self.report = simpanPinjam()
        self.report.show()


class inputSimpan(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Koperasi ITK")
        self.setWindowIcon(QtGui.QIcon("view/assets/img/icon.png"))
        self.setGeometry(0, 0, 600, 400)

        #--------main Layout-------
        qbok = QGridLayout()

        frame = QFrameElement("rgb(235, 243, 223)")
        frame.setContentsMargins(100, 50, 100, 50)

        boxLayout = QGridLayout(frame)
        boxLayout.setSpacing(20)

        #-------input-------
        self.namaLabel = QLabelElement("Nama Nasabah : ")
        self.nama = QLineEdit(self)
        self.nama.setStyleSheet("background : rgb(241, 255, 230);")

        self.tanggalLabel = QLabelElement("Tanggal : ")
        self.tanggal = QDateEdit()
        self.tanggal.setStyleSheet("background : rgb(241, 255, 230);")
        self.tanggal.setCalendarPopup(True)

        self.jumlahLabel = QLabelElement("Jumlah Simpan : ")
        self.jumlah = QLineEdit(self)
        self.jumlah.setStyleSheet("background : rgb(241, 255, 230);")

        #--------Button simpan--------
        self.submitBtn = QPushButtonGeneral("Submit")
        self.submitBtn.clicked.connect(self.submit_btn)

        #--------layouting--------
        boxLayout.addWidget(self.namaLabel, 0,0)
        boxLayout.addWidget(self.nama, 0,1,1,5)
        boxLayout.addWidget(self.tanggalLabel, 1,0)
        boxLayout.addWidget(self.tanggal, 1,1,1,5)
        boxLayout.addWidget(self.jumlahLabel, 2,0)
        boxLayout.addWidget(self.jumlah, 2,1,1,5)
        boxLayout.addWidget(self.submitBtn, 3,5,1,1,QtCore.Qt.AlignBottom)

        qbok.addWidget(frame)
        self.setLayout(qbok)
        self.show()

    def submit_btn(self):
        try:
            SimpanPinjamORM(self.nama.text(),
                                self.tanggal.text(),
                                self.jumlahsimpan.text(),
                                0).insertSimpanPinjam()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Telah Disimpan")
            msg.setWindowTitle("Berhasil")
            msg.exec_()
            # self.clear_btn()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Gagal Input")
            msg.setInformativeText(f"KESALAHAN : {e}")
            msg.setWindowTitle("Gagal")
            s = msg.exec_()


class inputPinjam(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Koperasi ITK")
        self.setWindowIcon(QtGui.QIcon("img/icon.png"))
        self.setGeometry(0, 0, 600, 400)

        #--------main Layout-------
        hbok = QGridLayout()

        frame = QFrameElement("rgb(235, 243, 223)")
        frame.setContentsMargins(100, 50, 100, 50)

        boxLayout = QGridLayout(frame)
        boxLayout.setSpacing(20)

        #-------input-------
        self.namaLabel = QLabelElement("Nama Nasabah : ")
        self.nama = QLineEdit(self)
        self.nama.setStyleSheet("background : rgb(241, 255, 230);")

        self.tanggalLabel = QLabelElement("Tanggal : ")
        self.tanggal = QDateEdit()
        self.tanggal.setStyleSheet("background : rgb(241, 255, 230);")
        self.tanggal.setCalendarPopup(True)

        self.jumlahLabel = QLabelElement("Jumlah Pinjam : ")
        self.jumlah = QLineEdit(self)
        self.jumlah.setStyleSheet("background : rgb(241, 255, 230);")

        #--------Button pinjam--------
        self.submitBtn = QPushButtonGeneral("Submit")
        self.submitBtn.clicked.connect(self.submit_btn)

        #--------layouting--------
        boxLayout.addWidget(self.namaLabel, 0,0)
        boxLayout.addWidget(self.nama, 0,1,1,5)
        boxLayout.addWidget(self.tanggalLabel, 1,0)
        boxLayout.addWidget(self.tanggal, 1,1,1,5)
        boxLayout.addWidget(self.jumlahLabel, 2,0)
        boxLayout.addWidget(self.jumlah, 2,1,1,5)
        boxLayout.addWidget(self.submitBtn, 3,5,1,1,QtCore.Qt.AlignBottom)

        hbok.addWidget(frame)
        self.setLayout(hbok)
        self.show()

    # def back_btn(self):
    #     from view.menu import Window
    #     welcome = Window()
    #     self.parent().setCentralWidget(welcome)

    def submit_btn(self):
        try:
            SimpanPinjamORM(self.nama.text(),
                                self.tanggal.text(),
                                0,
                                self.jumlahpinjam.text()).insertSimpanPinjam()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Telah Disimpan")
            msg.setWindowTitle("Berhasil")
            s = msg.exec_()
            # self.clear_btn()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Gagal Input")
            msg.setInformativeText(f"KESALAHAN : {e}")
            msg.setWindowTitle("Gagal")
            s = msg.exec_()

# def simpanpinjamInt():
#     App = QApplication(sys.argv)
#     App.setStyle('fusion')
#     tabDialog = Tab()
#     tabDialog.show()
#     sys.exit(App.exec())
