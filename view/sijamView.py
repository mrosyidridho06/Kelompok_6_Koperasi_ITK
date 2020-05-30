from Class.gudang import Gudang
from database.base import sessionFactory
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QApplication, QAbstractItemView,QMessageBox,QMainWindow, QWidget,QHBoxLayout, QPushButton,QTableWidget,QTableWidgetItem,QVBoxLayout)
import sys
from PyQt5 import QtGui
from database.SimpanPinjamORM import SimpanPinjamORM


class simpanPinjam(QMainWindow):
    def  __init__(self):
        super(simpanPinjam,self).__init__()
        self.Tampilan()



    def Tampilan(self):
        self.setWindowTitle("Laporan Simpan Pinjam")
        self.setWindowIcon(QtGui.QIcon("view/assets/img/icon.png"))
        self.setGeometry(200, 200, 831, 431)
        self.create_table()




    def create_table(self):
        self.table = QTableWidget(self)
        # self.table.cellClicked.connect(self.cek)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID","NAMA","Lokasi","Tanggal Masuk","Harga","Jumlah"])
        self.table.setFixedSize(830,430)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    # def cek(self, row):
    #     print(self.table.item(row, 0).text())
    #     print(self.table.item(row, 1).text())
    #     print(self.table.item(row, 2).text())
    #     print(self.table.item(row, 3).text())
    #     print(self.table.item(row, 4).text())
    #     print(self.table.item(row, 5).text())

    def isiTable(self):
        query = SimpanPinjamORM.showSijam()
        self.table.setRowCount(len(query))
        for row in range(len(query)):
            self.table.insertRow(1)
            self.table.setItem(row,0,QTableWidgetItem(str(query[row].id_nasabah)))
            self.table.setItem(row,1,QTableWidgetItem(query[row].nama_nasabah))
            self.table.setItem(row,2,QTableWidgetItem(query[row].tanggal))
            # self.table.setItem(row, 3, QTableWidgetItem(query[row].jumlah_simpan))
            self.table.setItem(row, 4,QTableWidgetItem(query[row].jumlah_pinjam))


# def Laporan():
# #     app = QApplication([sys.argv])
# #     win = LaporanGudang()
# #     win.show()
# #     sys.exit(app.exec_())

