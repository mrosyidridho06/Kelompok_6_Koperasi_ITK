import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PyQt5.QtGui import QFont

from Class.Autentikasi import Autentikasi
from view.win import mainwin


class login(QWidget):
    def __init__(self):
        super(login, self).__init__()

        fontStyle = QFont()
        fontStyle.setPointSize(14)
        fontStyle.setFamily('eras bold ITC')

        fontStyle1 = QFont()
        fontStyle1.setPointSize(13)
        fontStyle1.setFamily('arial')

        iniLabel = QLabel("", self)
        iniLabel.setText("Login")
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
        ledit2.setEchoMode(QLineEdit.Password)

        loginBtn = QPushButton('Masuk', self)
        loginBtn.clicked.connect(lambda: self.loginfungsi(ledit.text(),ledit2.text()))

        signupBtn = QPushButton('Daftar', self)
        signupBtn.clicked.connect(lambda: self.tomboldaftar())


        signupBtn.move(50, 180)
        loginBtn.move(270,180)
    def loginfungsi(self, email, password):
        auth = Autentikasi(email, password)
        auth.login()
        if auth.getStatusLogin() == True:
            self.mainscreen = mainwin()
            self.parent().setCentralWidget(self.mainscreen)
        else:
            masge = QMessageBox()
            masge.setIcon(QMessageBox.Warning)
            masge.setText("Kolom harus terisi Semua")
            masge.setWindowTitle("Error")
            masge.exec_()

    def tomboldaftar(self):
        from view.daftar import daftar
        self.parent().setCentralWidget(daftar())

