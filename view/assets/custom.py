from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtGui, QtCore


class QPushButtonLogin(QPushButton):
    def __init__(self, iconLocation, text,act,parent=None):
        super(QPushButtonLogin,self).__init__(parent)
        self.setStyleSheet('color : black;\
                            background-color : rgb(184, 220, 124)')

        self.setText(text)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.setFont(font)
        self.setFixedHeight(50)
        self.setFixedWidth(238)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconLocation))
        self.setIconSize(QtCore.QSize(50, 50))
        self.setIcon(icon)
        self.clicked.connect(act)

class QPushButtonMenu(QPushButton):
    def __init__(self, iconLocation,text,act,parent=None):
        super(QPushButtonMenu,self).__init__(parent)

        self.setText(text)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.setFont(font)
        self.setFixedHeight(50)
        self.setFixedWidth(238)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconLocation))
        self.setIconSize(QtCore.QSize(30, 30))
        self.setIcon(icon)
        self.clicked.connect(act)

