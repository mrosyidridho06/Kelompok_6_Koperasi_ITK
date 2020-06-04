from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from view.gudangView import LaporanGudang
from database.GudangORM import GudangORM

from view.fileElement.QPushButton import QPushButtonGeneral
from view.fileElement.QFrame import QFrameElement
from view.fileElement.QLabel import QLabelElement

class inputBarang(QWidget):
    def __init__(self):
        super(inputBarang,self).__init__()
        # self.setWindowTitle("Koperasi ITK")
        # self.setWindowIcon(QtGui.QIcon("view/assets/img/icon.png"))
        # self.setGeometry(0, 0, 600, 400)

        #--------main Layout-------
        vbox = QGridLayout()

        #--------Button-------
        frame = QFrameElement("rgb(235, 243, 223)")
        frame.setContentsMargins(100, 50, 100, 50)

        boxLayout = QGridLayout(frame)
        boxLayout.setSpacing(20)

        self.submitBtn = QPushButtonGeneral("Submit")
        self.submitBtn.clicked.connect(self.submit_btn)

        self.backbtn = QPushButtonGeneral("Back")
        self.backbtn.clicked.connect(self.back_btn)

        self.report = LaporanGudang()
        self.laporanBtn = QPushButtonGeneral("Lihat Laporan")
        self.laporanBtn.clicked.connect(self.Lihat)

        #-------Gudang input-------
        self.namaLabel = QLabelElement("Nama Barang : ")
        self.nama = QLineEdit(self)
        self.nama.setStyleSheet("background : rgb(241, 255, 230);")
        self.nama.setPlaceholderText("Masukkan Nama Barang ")

        self.lokasiLabel = QLabelElement("Lokasi : ")
        self.lokasi = QLineEdit(self)
        self.lokasi.setStyleSheet("background : rgb(241, 255, 230);")
        self.lokasi.setPlaceholderText("Masukkan Lokasi Barang ")

        self.tanggalLabel = QLabelElement("Tanggal Masuk : ")
        self.tanggal = QDateEdit()
        self.tanggal.setStyleSheet("background : rgb(241, 255, 230);")
        self.tanggal.setCalendarPopup(True)

        self.hargaLabel = QLabelElement("Harga : ")
        self.harga = QLineEdit(self)
        self.harga.setStyleSheet("background : rgb(241, 255, 230);")
        self.harga.setPlaceholderText("Masukkan Harga ")

        self.jumlahLabel = QLabelElement("Jumlah : ")
        self.jumlah = QSpinBox(self)
        self.jumlah.setStyleSheet("background : rgb(241, 255, 230);")

        #--------layout input--------
        boxLayout.addWidget(self.namaLabel, 1, 0)
        boxLayout.addWidget(self.nama, 1, 1,1,8)
        boxLayout.addWidget(self.lokasiLabel, 2, 0)
        boxLayout.addWidget(self.lokasi, 2, 1,1,8)
        boxLayout.addWidget(self.tanggalLabel, 3, 0)
        boxLayout.addWidget(self.tanggal, 3, 1,1,8)
        boxLayout.addWidget(self.hargaLabel, 4, 0)
        boxLayout.addWidget(self.harga, 4, 1,1,8)
        boxLayout.addWidget(self.jumlahLabel, 5, 0)
        boxLayout.addWidget(self.jumlah, 5, 1,1,8)

        #--------layout button--------
        boxLayout.addWidget(self.submitBtn, 6, 5,1,4)
        boxLayout.addWidget(self.backbtn, 6, 1,1,4)
        boxLayout.addWidget(self.laporanBtn, 7, 1,1,8)

        vbox.addWidget(frame)
        self.setLayout(vbox)
        self.show()

    def Lihat(self):
        self.report.show()

    def back_btn(self):
        from view.menu import Window
        welcome = Window()
        self.parent().setCentralWidget(welcome)

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

# def gudangInt():
#     App = QApplication(sys.argv)
#     App.setStyle("fusion")
#     window = inputBarang()
#     window.show()
#     sys.exit(App.exec())
