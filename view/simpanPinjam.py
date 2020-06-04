from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from database.SimpanPinjamORM import SimpanPinjamORM
from view.sijamView import simpanPinjam

import sys


class Tab(QDialog):
    def __init__(self):
        super().__init__()
        # self.setGeometry(200,200,500,300)
        # self.setWindowTitle('SimpanPinjam')
        # self.setWindowIcon(QtGui.QIcon("view/assets/img/icon.png"))

        tabWidget = QTabWidget()
        tabWidget.addTab(inputSimpan(), 'Simpan')
        tabWidget.addTab(inputPinjam(), 'Pinjam')

        self.lapor = QPushButton("Laporan")
        self.lapor.clicked.connect(self.Lihat)

        self.backnya = QPushButton("Back")
        self.backnya.clicked.connect(self.back_btn)

        vbox = QVBoxLayout()
        vbox.addWidget(tabWidget)
        vbox.addWidget(self.backnya)
        vbox.addWidget(self.lapor)
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

        self.isiSimpan()
        self.background()

        qbok = QVBoxLayout()
        qbok.addWidget(self.formGroupBox)

        self.submitBtn = QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit_btn)
        # self.backbtn = QPushButton("Back")
        # self.backbtn.clicked.connect(self.back_btn)

        hbok = QHBoxLayout()
        # hbok.addWidget(self.backbtn)
        hbok.addWidget(self.submitBtn, alignment=QtCore.Qt.AlignRight)
        qbok.addLayout(hbok)

        self.setLayout(qbok)

    # def back_btn(self):
    #     from view.menu import Window
    #     welcome = Window()
    #     self.parent().setCentralWidget(welcome)

    def background(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('view/assets/img/bg.jpg'))
        # self.image.resize(500,400)
        self.image.setGeometry(0, -75, 500, 400)
        # self.image.move(0,-50)

    def isiSimpan(self):
        self.formGroupBox = QGroupBox()
        self.formGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        layout = QFormLayout()

        self.nama = QLineEdit()
        layout.addRow("Nama Nasabah :", self.nama)

        self.tanggal = QDateEdit()
        self.tanggal.setCalendarPopup(True)
        layout.addRow(QLabel("Tanggal :"), self.tanggal)

        self.jumlahsimpan = QLineEdit()
        layout.addRow("Jumlah Simpan:", self.jumlahsimpan)

        self.formGroupBox.setLayout(layout)

    def submit_btn(self):
        if self.nama.text() != "" and self.jumlahsimpan.text() != "":
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
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Gagal Input")
            msg.setInformativeText(f"KESALAHAN")
            msg.setWindowTitle("Gagal")
            s = msg.exec_()


class inputPinjam(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Koperasi ITK")
        self.setWindowIcon(QtGui.QIcon("img/icon.png"))
        self.setGeometry(0, 0, 600, 400)

        self.isiPinjam()
        self.background()

        vbok = QVBoxLayout()
        vbok.addWidget(self.formGroupBox)

        self.submitBtn = QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit_btn)
        # self.backBtn = QPushButton("Back")
        # self.backBtn.clicked.connect(self.back_btn)
        # self.laporanBtn2 = QPushButton("Lihat Laporan")
        # self.laporanBtn.clicked.connect(self.laporan)

        hbok = QHBoxLayout()
        # hbok.addWidget(self.backBtn)
        hbok.addWidget(self.submitBtn, alignment=QtCore.Qt.AlignRight)
        vbok.addLayout(hbok)

        self.setLayout(vbok)

        # self.show()

    def background(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('view/assets/img/bg.jpg'))
        # self.image.resize(500,400)
        self.image.setGeometry(0, -75, 500, 400)
        # self.image.move(0,-50)

    def isiPinjam(self):
        self.formGroupBox = QGroupBox()
        self.formGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        layout = QFormLayout()

        self.nama = QLineEdit()
        layout.addRow("Nama Nasabah :", self.nama)

        self.tanggal = QDateEdit()
        self.tanggal.setCalendarPopup(True)
        layout.addRow(QLabel("Tanggal :"), self.tanggal)

        self.jumlahpinjam = QLineEdit()
        layout.addRow("Jumlah Pinjam:", self.jumlahpinjam)

        self.formGroupBox.setLayout(layout)

    # def back_btn(self):
    #     from view.menu import Window
    #     welcome = Window()
    #     self.parent().setCentralWidget(welcome)

    def submit_btn(self):
        if self.nama.text() !="" and self.jumlahpinjam.text() !="" :
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
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Gagal Input")
            msg.setInformativeText(f"KESALAHAN")
            msg.setWindowTitle("Gagal")
            s = msg.exec_()

# def simpanpinjamInt():
#     App = QApplication(sys.argv)
#     App.setStyle('fusion')
#     tabDialog = Tab()
#     tabDialog.show()
#     sys.exit(App.exec())
