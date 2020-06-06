from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from database.UsersORM import UsersORM
from view.assets.custom import QPushButtonLogin

class Login(QWidget):
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    def __init__(self):
        super(Login,self).__init__()

        self.layout = QFormLayout()

        fontt = QFont()
        fontt.setPointSize(13)
        fontt.setFamily('arial')
        fontt.setBold(True)

        self.label1 = QLabel('LOGIN FORM')
        self.label1.setFont(fontt)
        # self.label2 = QLabel('Silahkan Login dulu!')
        self.label3 = QLabel('Username')
        self.label4 = QLabel('Password')

        self.user = QLineEdit()
        self.user.setPlaceholderText("Masukkan Username")
        self.user.setFixedWidth(300)
        self.user.setFixedHeight(30)

        self.pw = QLineEdit()
        self.pw.setEchoMode(QLineEdit.Password)
        self.pw.setFixedWidth(300)
        self.pw.setFixedHeight(30)

        self.submit = QPushButtonLogin("view/assets/img/gudang.png","Login",self.login)


        qbok = QVBoxLayout()
        qbok.addSpacing(10)
        qbok.addWidget(self.label1, alignment=Qt.AlignHCenter)
        # qbok.addWidget(self.label2, alignment=Qt.AlignHCenter)
        qbok.addSpacing(15)
        qbok.addWidget(self.label3, alignment=Qt.AlignHCenter)
        qbok.addWidget(self.user, alignment=Qt.AlignHCenter)
        qbok.addSpacing(10)
        qbok.addWidget(self.label4, alignment=Qt.AlignHCenter)
        qbok.addWidget(self.pw, alignment=Qt.AlignHCenter)
        qbok.addSpacing(30)
        qbok.addWidget(self.submit, alignment=Qt.AlignHCenter)

        self.layout.addRow(qbok)


        self.layout.setAlignment(Qt.AlignHCenter)
        self.layout.setSpacing(10)
        self.setLayout(self.layout)

    def login(self):
        msg = QMessageBox()
        query = UsersORM.showUsers()
        ada = False
        for row in query:
            if self.user.text() == row.username:
                ada = True
                if self.pw.text() == row.password:

                    from view.menu import Window
                    x = Window()
                    self.parent().setCentralWidget(x)
                else:
                    msg.setWindowTitle("Salah Password")
                    msg.setText('Password anda salah!!')
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    break

        if not ada:
            msg.setWindowTitle("Username tidak ada")
            msg.setText('Username anda tidak ditemukan')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()