from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from database.GudangORM import GudangORM
from view.gudangView import LaporanGudang

class inputBarang(QWidget):
    def __init__(self):
        super(inputBarang,self).__init__()

        self.Gudangnya()

        qbok = QVBoxLayout()
        qbok.addWidget(self.formGroupBox)

        self.submitBtn = QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit_btn)
        self.backbtn = QPushButton("Back")
        self.backbtn.clicked.connect(self.back_btn)

        self.report = LaporanGudang()
        self.laporanBtn = QPushButton("Lihat Laporan")
        self.laporanBtn.clicked.connect(self.Lihat)

        hbok = QHBoxLayout()
        hbok.addWidget(self.backbtn)
        hbok.addWidget(self.submitBtn)
        qbok.addLayout(hbok)
        qbok.addWidget(self.laporanBtn)


        self.Layot = QFormLayout()
        self.Layot.addRow(qbok)
        self.setLayout(self.Layot)
               

    def Gudangnya(self):
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

    def back_btn(self):
        from view.menu import Window
        welcome = Window()
        self.parent().setCentralWidget(welcome)

    def submit_btn(self):
        try:
            x = GudangORM(self.nama.text(),
                        self.tanggal.text(),
                        self.lokasi.text(),
                        self.harga.text(),
                        self.jumlah.text())
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Telah Disimpan")
            msg.setWindowTitle("Berhasil")
            s = msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Gagal Input")
            msg.setInformativeText(f"KESALAHAN : {e}")
            msg.setWindowTitle("Gagal")
            s = msg.exec_()

# def gudangInt():
#     App = QApplication(sys.argv)
#     App.setStyle("fusion")
#     window = inputBarang()
#     window.show()
#     sys.exit(App.exec())
