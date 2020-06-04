from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PyQt5.QtGui import QFont

from database.akunORM import AkunOrm
from view.login import login

class daftar(QWidget):
    def __init__(self):
        super(daftar,self).__init__()
        print("suk")
        fontStyle = QFont()
        fontStyle.setPointSize(14)
        fontStyle.setFamily('eras bold ITC')

        fontStyle1 = QFont()
        fontStyle1.setPointSize(13)
        fontStyle1.setFamily('arial')

        iniLabel = QLabel("", self)
        iniLabel.setText("Daftar")
        iniLabel.setFont(fontStyle)
        iniLabel.move(160, 50)

        ledit = QLineEdit('', self)
        txt = QLabel("", self)
        txt.setText("Username")
        txt.setFont(fontStyle1)
        txt.move(50, 97)
        ledit.resize(180, 25)
        ledit.move(170, 100)

        ledit2 = QLineEdit('', self)
        txt = QLabel("", self)
        txt.setText("Password")
        txt.setFont(fontStyle1)
        txt.move(50, 137)
        ledit2.resize(180, 25)
        ledit2.move(170, 140)

        ledit3 = QLineEdit('', self)
        txt = QLabel("", self)
        txt.setText("Email")
        txt.setFont(fontStyle1)
        txt.move(50, 187)
        ledit3.resize(180, 25)
        ledit3.move(170, 180)

        signupBtn = QPushButton('Daftar', self)
        signupBtn.clicked.connect(lambda: self.register(ledit.text(), ledit2.text(), ledit3.text()))

        backBtn = QPushButton('Kembali', self)
        backBtn.clicked.connect(lambda: self.parent().setCentralWidget(login()))

        signupBtn.move(50, 220)
        backBtn.move(270, 220)

    def register(self, nama, password, email):
        print("tes")
        if nama != "" and password != "" and nama != "":
            print("tes")
            try:
                AkunOrm(nama, password, email).insert()
                masge =QMessageBox()
                masge.setWindowTitle("Success")
                masge.setText("User berhasil dibuat")
                masge.exec_()
                self.parent().setCentralWidget(login())
            except Exception as eror:
                masge = QMessageBox()
                masge.setIcon(QMessageBox.Warning)
                masge.setText(eror)
                masge.setWindowTitle("Error")
                masge.exec_()
        else:
            print("tes3")
            masge = QMessageBox()
            masge.setIcon(QMessageBox.Warning)
            masge.setText("Kolom harus terisi Semua")
            masge.setWindowTitle("Error")
            masge.exec_()