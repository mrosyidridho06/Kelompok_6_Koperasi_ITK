from PyQt5.QtWidgets import (QPushButton, QApplication, QMainWindow, QLineEdit,
                            QHBoxLayout, QVBoxLayout, QFormLayout, QLabel, QWidget, QDateEdit, QSpinBox, QDialog, QDialogButtonBox)
from PyQt5 import QtCore
import sys
from PyQt5 import QtGui

class Inputbarang(QWidget):
    def __init__(self):
        super().__init__()

        Label = QLabel("Input Barang")
        Label.setAlignment(QtCore.Qt.AlignCenter)
        submitbtn = QPushButton("Submit")
        laporanbtn = QPushButton("Lihat Laporan")


        title = "Koperasi ITK"
        left = 0
        right = 0
        width = 400
        height = 600
        iconName = "assets/img/icon.png"


        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, right, height, width)
        self.inputBarang()
        self.show()

    def inputBarang(self):
        self.form = QFormLayout(self)

        self.barang = QLineEdit(self)
        self.barang.setPlaceholderText("Nama Barang")
        self.form.addRow("Nama Barang", self.barang)

        self.lokasi = QLineEdit(self)
        self.lokasi.setPlaceholderText("Lokasi")
        self.form.addRow("Lokasi", self.lokasi)

        self.tglMasuk = QDateEdit(self)
        self.tglMasuk.setCalendarPopup(True)
        self.form.addRow("Tanggal Masuk", self.tglMasuk)

        self.harga = QLineEdit(self)
        self.harga.setPlaceholderText("Harga")
        self.form.addRow("Harga", self.harga)

        self.jumlah = QSpinBox(self)
        self.form.addRow("Masukkan Jumlah", self.jumlah)

        self.submit = QPushButton(self)
        self.submit.setText("Tambah")
        self.submit.clicked.connect(self.submit_btn)

        self.laporan = QPushButton(self)
        self.laporan.setText("Laporan")

        self.form.addRow(self.submit,self.laporan)


    def submit_btn(self):
        print("Nama Barang : {}\nLokasi : {}\nTanggal Masuk : {}\nHarga : {}\nJumlah : {}".
        format(self.nama.text(),
        self.noTel.text(),
        self.alamat.toPlainText(),
        self.jk.currentText(),
        self.Nik.text(),
        self.tglLahir.text()))

if __name__ == "__main__":
    App = QApplication(sys.argv)
    inBarang = Inputbarang()
    sys.exit(App.exec())

