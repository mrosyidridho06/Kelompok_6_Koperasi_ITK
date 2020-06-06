from PyQt5 import QtGui
from PyQt5.QtCore import Qt,QDate
from database.SimpanPinjamORM import SimpanPinjamORM
from PyQt5.QtWidgets import *


class simpanPinjam(QWidget):
    def  __init__(self):
        super(simpanPinjam,self).__init__()
        self.setWindowTitle('Laporan Simpan Pinjam')
        self.setWindowIcon(QtGui.QIcon("view/assets/img/icon.png"))
        self.setMaximumSize(932, 432)
        self.Tampilan()
        self.test1 = QFrame()

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

        self.simpan = QLineEdit(self)

        self.pinjam = QLineEdit(self)


        hb1 = QHBoxLayout()
        hb1.addWidget(self.btn2, alignment=Qt.AlignLeft)
        hb1.addWidget(self.btn, alignment=Qt.AlignLeft)
        vb.addLayout(hb1)


        formG = QFormLayout()
        formG.addRow("ID : ", self.idG)
        formG.addRow("Nama : ", self.nama)
        formG.addRow("Tanggal : ", self.tanggal)
        formG.addRow("Simpan : ", self.simpan)
        formG.addRow("Pinjam : ", self.pinjam)
        formG.addRow(vb)
        formG.addRow(self.btn3)
        self.test1.setLayout(formG)


        hb = QHBoxLayout()
        hb.addWidget(self.table)
        hb.addWidget(self.test1)
        hb.setContentsMargins(0, 0, 0, 0)
        self.lastClick = None

        self.setLayout(hb)



    def Tampilan(self):
        self.table = QTableWidget(self)
        self.table.cellClicked.connect(self.baris)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID","Nama","Tanggal","Simpan","Pinjam"])
        self.table.setFixedSize(650,430)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def baris(self, row):
        self.lastClick = int(self.table.item(row, 0).text())
        print(self.lastClick)
        print(self.table.item(row, 1).text())  # Nama
        print(self.table.item(row, 3).text())  # Simpan
        print(self.table.item(row, 4).text())  # Pinjam

        self.idG.setText(self.table.item(row, 0).text())
        self.nama.setText(self.table.item(row, 1).text())
        self.simpan.setText(str(self.table.item(row, 3).text()))
        self.pinjam.setText(self.table.item(row, 4).text())

        a = self.table.item(row, 2).text().split('/')
        dd = int(a[0])
        mm = int(a[1])
        yy = int(a[2])
        self.tanggal.setDate(QDate(yy, mm, dd))


    def isiTable(self):
        query = SimpanPinjamORM.dataSijam()
        self.table.setRowCount(len(query))
        for row in range(len(query)):
            self.table.setItem(row, 0,QTableWidgetItem(str(query[row].id_nasabah)))
            self.table.setItem(row, 1,QTableWidgetItem(query[row].nama_nasabah))
            self.table.setItem(row, 2,QTableWidgetItem(query[row].tanggal))
            self.table.setItem(row, 3,QTableWidgetItem(query[row].jumlah_simpan))
            self.table.setItem(row, 4,QTableWidgetItem(query[row].jumlah_pinjam))

    def Tupdate(self):
        try:
            SimpanPinjamORM.updateSimpanPinjam(self.idG.text(),
                        self.nama.text(),
                        self.tanggal.text(),
                        self.simpan.text(),
                        self.pinjam.text())
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
            SimpanPinjamORM.delSijam(self.lastClick)
            self.isiTable()
        else:
            pass
