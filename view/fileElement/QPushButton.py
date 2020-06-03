from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QPushButton


class QPushButtonMenu(QPushButton):
    def __init__(self, iconLocation, text):
        super().__init__()

        #---------text setting---------
        self.setStyleSheet("height : 80%;" "color : white;" "background-color : rgb(184, 220, 124);")
        self.setText(text)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)

        self.setFont(font)

        #---------icon setting----------
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconLocation))
        self.setIconSize(QtCore.QSize(50, 50))
        self.setIcon(icon)

class QPushButtonGeneral(QPushButton):
    def __init__(self, text):
        super().__init__()

        #---------text setting---------
        self.setStyleSheet("height : 40%;" "color : white;" "background-color : rgb(184, 220, 124);")
        self.setText(text)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)

        self.setFont(font)

