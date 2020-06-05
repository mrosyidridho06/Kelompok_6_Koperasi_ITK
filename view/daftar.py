from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

from database.akunORM import AkunOrm
from view.login import login
from view.fileElement.QFrame import QFrameElement
from view.fileElement.QLabel import QLabelElement
from view.fileElement.QPushButton import QPushButtonLogin

class daftar(QWidget):
    def __init__(self):
        super(daftar,self).__init__()
        print("suk")

        #--------main Layout-------
        vbox = QGridLayout()

        frame = QFrameElement("rgb(235, 243, 223)")
        frame.setContentsMargins(250, 130, 250, 130)

        boxLayout = QGridLayout(frame)
        boxLayout.setSpacing(20)

        #--------Button-------
        signupBtn = QPushButtonLogin('Daftar')
        signupBtn.clicked.connect(lambda: self.register(ledit1.text(), ledit2.text(), ledit3.text()))

        backBtn = QPushButtonLogin('Kembali')
        backBtn.clicked.connect(lambda: self.parent().setCentralWidget(login()))

        #-------login atribut-------
        fontStyle = QFont()
        fontStyle.setPointSize(14)
        fontStyle.setFamily('eras bold ITC')

        fontStyle1 = QFont()
        fontStyle1.setPointSize(13)
        fontStyle1.setFamily('arial')

        iniLabel = QLabel("", self)
        iniLabel.setText("Daftar")
        iniLabel.setFont(fontStyle)

        leditLabel1 = QLabelElement("Username : ")
        ledit1 = QLineEdit(self)
        ledit1.setStyleSheet("background : rgb(241, 255, 230);")
        ledit1.setPlaceholderText("Masukkan Username")

        leditLabel2 = QLabelElement("Password : ")
        ledit2 = QLineEdit(self)
        ledit2.setStyleSheet("background : rgb(241, 255, 230);")
        ledit2.setPlaceholderText("Masukkan Password")

        leditLabel3 = QLabelElement("Email : ")
        ledit3 = QLineEdit(self)
        ledit3.setStyleSheet("background : rgb(241, 255, 230);")
        ledit3.setPlaceholderText("Masukkan Email")

        #--------layout input--------
        boxLayout.addWidget(iniLabel,0,3,1,1)
        boxLayout.addWidget(leditLabel1,1,0)
        boxLayout.addWidget(ledit1,1,1,1,9)
        boxLayout.addWidget(leditLabel2,2,0)
        boxLayout.addWidget(ledit2,2,1,1,9)
        boxLayout.addWidget(leditLabel3,3,0)
        boxLayout.addWidget(ledit3,3,1,1,9)

        #--------layout button--------
        boxLayout.addWidget(signupBtn,4,4,1,3)
        boxLayout.addWidget(backBtn,4,7,1,3)

        vbox.addWidget(frame)
        self.setLayout(vbox)


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
