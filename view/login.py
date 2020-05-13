import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont

app = QApplication([])
app.setStyle('fusion')
mainWindow = QMainWindow()
mainWindow.setWindowTitle("Koperasi ITK")
mainWindow.setGeometry(200,200,400,280)

fontStyle = QFont()
fontStyle.setPointSize(14)
fontStyle.setFamily('eras bold ITC')

fontStyle1 = QFont()
fontStyle1.setPointSize(13)
fontStyle1.setFamily('arial')

iniLabel = QLabel("", mainWindow)
iniLabel.setText("Login")
iniLabel.setFont(fontStyle)
iniLabel.move(160,50)

ledit = QLineEdit('', mainWindow)
txt = QLabel("", mainWindow)
txt.setText("Username")
txt.setFont(fontStyle1)
txt.move(50,97)
ledit.resize(180,25)
ledit.move(170,100)

ledit2 = QLineEdit('', mainWindow)
txt = QLabel("", mainWindow)
txt.setText("Password")
txt.setFont(fontStyle1)
txt.move(50,137)
ledit2.resize(180,25)
ledit2.move(170,140)

loginBtn = QPushButton('Masuk', mainWindow)

loginBtn.move(50,180)


def leditAktif():
    usr = ledit.text()
    iniLabel.setText(usr)
    iniLabel.adjustSize()


loginBtn.clicked.connect(leditAktif)

mainWindow.show()
sys.exit(app.exec_())
