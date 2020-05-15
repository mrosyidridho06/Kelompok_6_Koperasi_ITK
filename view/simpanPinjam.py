from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QVBoxLayout,QMessageBox, QSpinBox, QLabel, QFormLayout,  QGroupBox, QDateEdit ,QDialog, QTabWidget, QWidget
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from database.SimpanPinjamORM import SimpanPinjamORM
import sys

class Tab(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,500,300)
        self.setWindowTitle('SimpanPinjam')
        self.setWindowIcon(QtGui.QIcon("view/assets/img/icon.png"))
        vbox = QVBoxLayout()
        tabWidget = QTabWidget()

        tabWidget.addTab(inputSimpan(), 'Simpan')
        tabWidget.addTab(inputPinjam(), 'Pinjam')

        vbox.addWidget(tabWidget)


        self.setLayout(vbox)

class inputSimpan(QWidget):
    def __init__(self):
        super().__init__()
        self.createFormGroupBox()
        self.UI()

        title = "Koperasi ITK"
        left = 0
        right = 0
        width = 400
        height = 600
        iconName = "view/assets/img/icon.png"

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)

        self.submitBtn = QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit_btn)

        mainLayout.addWidget(self.submitBtn)

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, right, height, width)
        self.setLayout(mainLayout)

        # self.show()
    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('view/assets/img/bg.jpg'))
        # self.image.resize(500,400)
        self.image.setGeometry(0,-75,500,400)
        # self.image.move(0,-50)

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox()
        self.formGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        layout = QFormLayout()

        self.nama = QLineEdit()
        layout.addRow("Nama Nasabah :", self.nama)

        self.tanggal = QDateEdit()
        self.tanggal.setCalendarPopup(True)
        layout.addRow(QLabel("Tanggal :"), self.tanggal)

        self.jumlahsimpan = QLineEdit()
        layout.addRow("Jumlah Simpan:", self.jumlahsimpan)

        self.formGroupBox.setLayout(layout)

    def submit_btn(self):
        try:
            x = SimpanPinjamORM(self.nama.text(),
                                self.tanggal.text(),
                                self.jumlahsimpan.text(),
                                0)
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


class inputPinjam(QWidget):
    def __init__(self):
        super().__init__()
        self.createFormGroupBox()
        self.UI()
        title = "Koperasi ITK"
        left = 0
        right = 0
        width = 400
        height = 600
        iconName = "img/icon.png"

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)

        self.submitBtn = QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit_btn)

        mainLayout.addWidget(self.submitBtn)

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, right, height, width)
        self.setLayout(mainLayout)

        # self.show()

    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('view/assets/img/bg.jpg'))
        # self.image.resize(500,400)
        self.image.setGeometry(0,-75,500,400)
        # self.image.move(0,-50)

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox()
        self.formGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        layout = QFormLayout()

        self.nama =  QLineEdit()
        layout.addRow("Nama Nasabah :",self.nama)

        self.tanggal = QDateEdit()
        self.tanggal.setCalendarPopup(True)
        layout.addRow(QLabel("Tanggal :"), self.tanggal)

        self.jumlahpinjam = QLineEdit()
        layout.addRow("Jumlah Pinjam:",self.jumlahpinjam)


        self.formGroupBox.setLayout(layout)

    def submit_btn(self):
        try:
            x = SimpanPinjamORM(self.nama.text(),
                        self.tanggal.text(),
                        0,
                        self.jumlahpinjam.text())
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

if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setStyle('fusion')
    tabDialog = Tab()
    tabDialog.show()
    sys.exit(App.exec())

