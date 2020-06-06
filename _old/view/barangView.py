from PyQt5.QtWidgets import (QApplication, QAbstractItemView,QMessageBox,QMainWindow, QWidget,QHBoxLayout, QPushButton,QTableWidget,QTableWidgetItem,QVBoxLayout)
import sys
from database.BarangORM import BarangORM

class LaporanBarang(QMainWindow):
    def  __init__(self):
        super(LaporanBarang,self).__init__()
        self.Tampilan()



    def Tampilan(self):
        self.setWindowTitle("Laporan Barang")
        #self.setGeometry(200, 200, 900, 500)
        self.create_table()



    def create_table(self):
        self.table = QTableWidget(self)
        self.table.cellClicked.connect(self.cek)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID","NAMA","Jumlah","Lokasi","Tanggal Masuk","Harga"])
        self.table.setFixedSize(741,350)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def cek(self, row):
        print(self.table.item(row, 0).text())
        print(self.table.item(row, 1).text())
        print(self.table.item(row, 2).text())
        print(self.table.item(row, 3).text())
        print(self.table.item(row, 4).text())
        print(self.table.item(row, 5).text())

    def isiTable(self):
        query = BarangORM.dataBarang()
        self.table.setRowCount(len(query))
        for row in range(len(query)):
            #self.table.insertRow(1)
            self.table.setItem(row,0,QTableWidgetItem(str(query[row].id_barang)))
            self.table.setItem(row,1,QTableWidgetItem(query[row].nama_barang))
            self.table.setItem(row,2,QTableWidgetItem(query[row].jumlah_barang))
            self.table.setItem(row, 3, QTableWidgetItem(query[row].lokasi))
            self.table.setItem(row, 4, QTableWidgetItem(query[row].tanggal_masuk))
            self.table.setItem(row, 5, QTableWidgetItem(query[row].harga_barang))


def Laporan():
    app = QApplication([sys.argv])
    win = LaporanBarang()
    win.show()
    sys.exit(app.exec_())

Laporan()