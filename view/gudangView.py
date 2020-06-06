from PyQt5 import QtGui
from PyQt5.QtCore import Qt,QDate
from database.GudangORM import GudangORM
from PyQt5.QtWidgets import *


class LaporanGudang(QWidget):
    def  __init__(self):
        super(LaporanGudang,self).__init__()
        self.setWindowTitle('Laporan Gudang')
        self.setWindowIcon(QtGui.QIcon("view/assets/img/icon.png"))
        self.setMaximumSize(832,630)
        self.viewTabel()
        self.test = QFrame()

        self.btn = QPushButton('Update')
        self.btn.clicked.connect(self.Tupdate)

        self.btn2 = QPushButton('Refresh')
        self.btn2.clicked.connect(self.ulang)

        self.btn3 = QPushButton('Hapus')
        self.btn3.clicked.connect(self.hapus)
        vb = QVBoxLayout()

        self.idG = QLineEdit(self)
        self.idG.setReadOnly(True)

        self.nama = QLineEdit(self)

        self.tanggal = QDateEdit()
        self.tanggal.setCalendarPopup(True)

        self.lokasi = QLineEdit(self)

        self.harga = QLineEdit(self)

        self.jumlah = QSpinBox(self)

        hb1 = QHBoxLayout()
        hb1.addWidget(self.btn2, alignment=Qt.AlignLeft)
        hb1.addWidget(self.btn, alignment=Qt.AlignLeft)
        vb.addLayout(hb1)
        # vb.addSpacing(200)


        formG = QFormLayout()
        formG.addRow("ID : ", self.idG)
        formG.addRow("Nama : ", self.nama)
        formG.addRow("Tanggal : ", self.tanggal)
        formG.addRow("Lokasi : ", self.lokasi)
        formG.addRow("Harga : ", self.harga)
        formG.addRow("Jumlah : ", self.jumlah)
        formG.addRow(vb)
        formG.addRow(self.btn3)
        self.test.setLayout(formG)


        hb = QHBoxLayout()
        hb.addWidget(self.table)
        hb.addWidget(self.test)
        hb.setContentsMargins(0, 0, 0, 0)
        self.lastClick = None

        self.setLayout(hb)



    def viewTabel(self):
        self.table = QTableWidget(self)
        self.table.cellClicked.connect(self.baris)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID","Nama","Tanggal","Lokasi","Harga","Jumlah"])
        self.table.setFixedSize(830,430)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def baris(self, row):
        self.lastClick = int(self.table.item(row, 0).text())
        print(self.lastClick)
        print(self.table.item(row, 1).text())  # Nama
        print(self.table.item(row, 3).text())  # Lokasi
        print(self.table.item(row, 4).text())  # Harga
        print(self.table.item(row, 5).text())  # Jumlah

        self.idG.setText(self.table.item(row, 0).text())
        self.nama.setText(self.table.item(row, 1).text())
        self.lokasi.setText(str(self.table.item(row, 3).text()))
        self.harga.setText(self.table.item(row, 4).text())
        self.jumlah.valueFromText(self.table.item(row, 5).text())

        a = self.table.item(row, 2).text().split('/')
        dd = int(a[0])
        mm = int(a[1])
        yy = int(a[2])
        self.tanggal.setDate(QDate(yy, mm, dd))


    def isiTable(self):
        query = GudangORM.dataGudang()
        self.table.setRowCount(len(query))
        for row in range(len(query)):
            self.table.setItem(row, 0,QTableWidgetItem(str(query[row].id_barang)))
            self.table.setItem(row, 1,QTableWidgetItem(query[row].nama_produk))
            self.table.setItem(row, 2,QTableWidgetItem(query[row].tanggal_masuk))
            self.table.setItem(row, 3,QTableWidgetItem(query[row].lokasi))
            self.table.setItem(row, 4,QTableWidgetItem(query[row].harga_barang))
            self.table.setItem(row, 5,QTableWidgetItem(query[row].jumlah_barang))

    def Tupdate(self):
        try:
            GudangORM.updateGudang(self.idG.text(),
                        self.nama.text(),
                        self.tanggal.text(),
                        self.lokasi.text(),
                        self.harga.text(),
                        self.jumlah.text())
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Data Telah Terupdate")
            msg.setWindowTitle("Berhasil, Selamat")
            s = msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Gagal Input")
            msg.setInformativeText(f"KESALAHAN : {e}")
            msg.setWindowTitle("Gagal")
            s = msg.exec_()

    def ulang(self):
        self.isiTable()

    def hapus(self):
        if self.lastClick != None:
            GudangORM.delGudang(self.lastClick)
            self.isiTable()
        else:
            pass



