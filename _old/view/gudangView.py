from Class.gudang import Gudang
from database.base import sessionFactory
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QApplication, QAbstractItemView, QMessageBox, QMainWindow, QWidget, QHBoxLayout,
                             QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout)
import sys
from PyQt5 import QtGui
from database.GudangORM import GudangORM


class LaporanGudang(QMainWindow):
    def __init__(self):
        super(LaporanGudang, self).__init__()
        self.Tampilan()

    def Tampilan(self):
        self.setWindowTitle("Laporan Gudang")
        self.setWindowIcon(QtGui.QIcon("view/assets/img/icon.png"))
        self.setGeometry(200, 200, 831, 431)
        self.create_table()

    def create_table(self):
        self.table = QTableWidget(self)
        # self.table.cellClicked.connect(self.cek)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["NAMA", "Lokasi", "Tanggal Masuk", "Harga", "Jumlah"])
        self.table.setFixedSize(830, 430)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def isiTable(self):
        query = GudangORM.dataGudang()
        self.table.setRowCount(len(query))
        for row in range(len(query)):
            # self.table.insertRow(1)

            print(row)
            self.table.setItem(row, 0, QTableWidgetItem(query[row].nama_produk))
            self.table.setItem(row, 1, QTableWidgetItem(query[row].lokasi))
            self.table.setItem(row, 2, QTableWidgetItem(query[row].tanggal_masuk))
            self.table.setItem(row, 3, QTableWidgetItem(query[row].jumlah_barang))
            self.table.setItem(row, 4, QTableWidgetItem(query[row].harga_barang))


def Laporan():
    app = QApplication([sys.argv])
    win = LaporanGudang()
    win.show()
    sys.exit(app.exec_())
