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
        self.setWindowTitle("Laporan Simpan Pinjam")
        self.setWindowIcon(QtGui.QIcon("view/assets/img/icon.png"))
        self.setGeometry(200, 200, 831, 431)
        self.create_table()

    def create_table(self):
        print("isitable")
        self.table = QTableWidget(self)
        # self.table.cellClicked.connect(self.cek)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID","NAMA","Tanggal","Simpan","Pinjam"])
        query = SimpanPinjamORM.showSijam()
        print(len(query))
        self.table.setRowCount(len(query))
        for row in range(len(query)):
            self.table.setItem(row,0,QTableWidgetItem(str(query[row].id_nasabah)))
            self.table.setItem(row,1,QTableWidgetItem(query[row].nama_nasabah))
            self.table.setItem(row,2,QTableWidgetItem(query[row].tanggal))
            self.table.setItem(row, 3, QTableWidgetItem(str(query[row].jumlah_simpan)))
            self.table.setItem(row, 4,QTableWidgetItem(str(query[row].jumlah_pinjam)))
        self.table.setFixedSize(830,430)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)



# def Laporan():
# #     app = QApplication([sys.argv])
# #     win = LaporanGudang()
# #     win.show()
# #     sys.exit(app.exec_())

