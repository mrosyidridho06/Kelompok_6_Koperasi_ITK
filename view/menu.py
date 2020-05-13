from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout, QLabel
import sys
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QPixmap

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "Menu Koperasi"
        self.top = 500
        self.left = 200
        self.width = 400
        self.height = 100

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon('kaki.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.setLayout(vbox)

        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox('Pilih Menu')
        hboxlayout = QHBoxLayout()

        button1 = QPushButton('kaki 1', self)
        button1.setIcon(QtGui.QIcon('kaki.png'))
        button1.setIconSize(QtCore.QSize(40,40))
        button1.setMinimumHeight(50)
        button1.setMinimumWidth(150)
        hboxlayout.addWidget(button1)

        button2 = QPushButton('kaki 2', self)
        button2.setIcon(QtGui.QIcon('kaki.png'))
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setMinimumHeight(50)
        button2.setMinimumWidth(150)
        hboxlayout.addWidget(button2)

        self.groupBox.setLayout(hboxlayout)

if __name__ == "__main__" :
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
