from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QSpinBox, QLabel, QFormLayout, QWidget, QGroupBox, QDateEdit
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys

class inpotBarang(QWidget):
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
        laporanBtn = QPushButton("Lihat Laporan")

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
        layout = QFormLayout()

        layout.addRow(QLabel("Nama Barang :"), QLineEdit())
        layout.addRow(QLabel("Lokasi :"), QLineEdit())
        tm = QDateEdit()
        tm.setCalendarPopup(True)
        layout.addRow(QLabel("Tanggal Masuk :"), tm)
        layout.addRow(QLabel("Harga :"), QLineEdit())
        layout.addRow(QLabel("Jumlah :"), QSpinBox())
        self.formGroupBox.setLayout(layout)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    inBarang = inpotBarang()
    sys.exit(App.exec())
