from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QSpinBox, QLabel, QFormLayout, QWidget, QGroupBox, QDateEdit
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys
from view.barangView import LaporanBarang

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

        submitBtn = QPushButton("Submit")


        self.report = LaporanBarang()
        laporanBtn = QPushButton("Lihat Laporan")
        laporanBtn.clicked.connect(self.Lihat)

        mainLayout.addWidget(submitBtn)
        mainLayout.addWidget(laporanBtn)


        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, right, height, width)
        self.setLayout(mainLayout)

        self.show()

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Input Barang")
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

        self.formGroupBox.setLayout(self.layout)

    def Lihat(self):
        self.report.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setStyle("fusion")
    inBarang = inputBarang()
    sys.exit(App.exec())
