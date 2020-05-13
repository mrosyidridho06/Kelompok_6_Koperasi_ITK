from Class.gudang import Gudang
from database.base import sessionFactory
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QApplication,QAbstractItemView,QMessageBox,QMainWindow, QWidget,QHBoxLayout, QPushButton,QTableWidget,QTableWidgetItem,QVBoxLayout)
import sys
from database.GudangORM import GudangORM

class LaporanGudang(QMainWindow):
    def  __init__(self):
        super(LaporanGudang,self).__init__()
        self.Tampilan()


    def Tampilan(self):
        self.setWindowTitle("Laporan Gudang")
        self.setGeometry(200, 200, 900, 500)

        self.create_table()


    def create_table(self):
        self.table = QTableWidget(self)
        self.table.cellClicked.connect(self.cek)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID","NAMA","Jumlah"])
        self.table.setFixedSize(741,350)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def cek(self, row):
        print(self.table.item(row, 0).text())
        print(self.table.item(row, 1).text())
        print(self.table.item(row, 2).text())


    def isiTable(self):
        query = GudangORM.dataGudang()
        self.table.setRowCount(len(query))
        for row in range(len(query)):
            #self.table.insertRow(1)
            self.table.setItem(row,0,QTableWidgetItem(query[row].id_barang))
            self.table.setItem(row,1,QTableWidgetItem(query[row].nama_produk))
            self.table.setItem(row,2,QTableWidgetItem(query[row].jumlah_barang))


def Laporan():
    app = QApplication([sys.argv])
    win = LaporanGudang()
    win.show()
    sys.exit(app.exec_())

Laporan()