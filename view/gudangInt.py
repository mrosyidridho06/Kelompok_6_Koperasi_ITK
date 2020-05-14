from PyQt5.QtWidgets import QApplication, QPushButton,QMessageBox, QLineEdit, QVBoxLayout, QSpinBox, QLabel, QFormLayout, QWidget, QGroupBox, QDateEdit
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys
from view.gudangView import LaporanGudang
from database.GudangORM import GudangORM
# from Class.gudang import Gudang

class inputBarang(QWidget):
    def __init__(self):
        super().__init__()
        self.createFormGroupBox()

        title = "Koperasi ITK"
        left = 0
        right = 0
        width = 400
        height = 600
        iconName = "assets/img/icon.png"
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)

        self.submitBtn = QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit_btn)

        self.report = LaporanGudang()
        laporanBtn = QPushButton("Lihat Laporan")
        laporanBtn.clicked.connect(self.Lihat)

        mainLayout.addWidget(self.submitBtn)
        mainLayout.addWidget(laporanBtn)

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, right, height, width)
        self.setLayout(mainLayout)

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Input Gudang")
        self.formGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QFormLayout()

        self.nama = QLineEdit(self)
        self.nama.setPlaceholderText("Masukkan Nama Barang ")
        self.layout.addRow("Nama Barang :", self.nama)

        self.lokasi = QLineEdit(self)
        self.lokasi.setPlaceholderText("Masukkan Lokasi Barang ")
        self.layout.addRow("Lokasi :", self.lokasi)

        self.tanggal = QDateEdit()
        self.tanggal.setCalendarPopup(True)
        self.layout.addRow(QLabel("Tanggal Masuk :"), self.tanggal)

        self.harga = QLineEdit(self)
        self.harga.setPlaceholderText("Masukkan Harga ")
        self.layout.addRow("Harga :", self.harga)


        self.jumlah = QSpinBox(self)
        self.layout.addRow("Jumlah :", self.jumlah)

        # self.tombol = QPushButton("Submit")
        # self.tombol.clicked.connect(self.submit_btn)
        # self.layout.addRow(self.tombol)
        self.formGroupBox.setLayout(self.layout)

    def Lihat(self):
        self.report.show()

    def submit_btn(self):
        try:
            x = GudangORM(self.nama.text(),
                        self.lokasi.text(),
                        self.tanggal.text(),
                        self.harga.text(),
                        self.jumlah.text())
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

if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setStyle("fusion")
    window = inputBarang()
    window.show()
    inBarang = inputBarang()
    sys.exit(App.exec())
