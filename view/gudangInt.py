from Class.gudang import Gudang
#from Model.base import sessionFactory,modelFactory
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QApplication, QDateEdit,QMessageBox, QComboBox, QTextEdit,QFrame, QFormLayout, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout)
from view.assets.lineEdit import lineEdit
import sys


class InputGudang(QWidget):
    def  __init__(self):
        super(InputGudang,self).__init__()
        self.setWindowTitle("Input Gudang")
        self.setGeometry(200,200,700,500)
        self.Tampilan()


    def Tampilan(self):

        self.form = QFormLayout(self)
        self.nama = lineEdit("")
        self.nama.setPlaceholderText("Masukkan Barang")
        self.nama.setFixedSize(200,20)
        self.form.addRow("Nama Barang : ", self.nama)


        self.lokasi = QLineEdit(self)
        self.lokasi.setPlaceholderText("Masukkan Lokasi")
        self.form.addRow("Lokasi : ", self.lokasi)

        self.tanggal = QDateEdit(self)
        self.form.addRow("Tanggal : ", self.tanggal)

        self.harga = QLineEdit(self)
        self.harga.setPlaceholderText("Masukkan Harga")
        self.form.addRow("Harga : ", self.harga)

        self.jumlah = QLineEdit(self)
        self.jumlah.setPlaceholderText("Masukkan Jumlah")
        self.form.addRow("Jumlah : ", self.jumlah)

        self.btn = QPushButton(self)
        self.btn.setText("Tombol")
        self.btn.clicked.connect(self.btn_clear)
        self.form.addRow(self.btn)

    def btn_clear(self):
        pass

def Tambahgudang():
    app = QApplication([sys.argv])
    win = InputGudang()
    win.show()
    sys.exit(app.exec_())

Tambahgudang()