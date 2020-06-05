import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

from Class.Autentikasi import Autentikasi
from view.win import mainwin
from view.fileElement.QFrame import QFrameElement
from view.fileElement.QLabel import QLabelElement
from view.fileElement.QPushButton import QPushButtonLogin


class login(QWidget):
    def __init__(self):
        super(login, self).__init__()

        #--------main Layout-------
        vbox = QGridLayout()

        frame = QFrameElement("rgb(235, 243, 223)")
        frame.setContentsMargins(250, 150, 250, 150)

        boxLayout = QGridLayout(frame)
        boxLayout.setSpacing(20)

        #--------Button-------
        loginBtn = QPushButtonLogin("Login")
        loginBtn.clicked.connect(lambda: self.loginfungsi(ledit1.text(),ledit2.text()))

        signupBtn = QPushButtonLogin("Daftar")
        signupBtn.clicked.connect(lambda: self.tomboldaftar())

        #-------login atribut-------
        fontStyle = QFont()
        fontStyle.setPointSize(14)
        fontStyle.setFamily('eras bold ITC')

        fontStyle1 = QFont()
        fontStyle1.setPointSize(13)
        fontStyle1.setFamily('arial')

        iniLabel = QLabel("", self)
        iniLabel.setText("Login")
        iniLabel.setFont(fontStyle)

        leditLabel1 = QLabelElement("Username : ")
        ledit1 = QLineEdit(self)
        ledit1.setStyleSheet("background : rgb(241, 255, 230);")
        ledit1.setPlaceholderText("Masukkan Username")

        leditLabel2 = QLabelElement("Password : ")
        ledit2 = QLineEdit(self)
        ledit2.setStyleSheet("background : rgb(241, 255, 230);")
        ledit2.setPlaceholderText("Masukkan Password")
        ledit2.setEchoMode(QLineEdit.Password)

        #--------layout input--------
        boxLayout.addWidget(iniLabel,0,3,1,1)
        boxLayout.addWidget(leditLabel1,1,0)
        boxLayout.addWidget(ledit1,1,1,1,9)
        boxLayout.addWidget(leditLabel2,2,0)
        boxLayout.addWidget(ledit2,2,1,1,9)

        #--------layout button--------
        boxLayout.addWidget(signupBtn,4,4,1,3)
        boxLayout.addWidget(loginBtn,4,7,1,3)

        vbox.addWidget(frame)
        self.setLayout(vbox)

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

