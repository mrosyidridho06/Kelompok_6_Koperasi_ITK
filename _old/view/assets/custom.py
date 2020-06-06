from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit


class myInputan(QLineEdit):
    def __init__(self, placeholder):
        super(myInputan,self).__init__()
        self.setPlaceholderText(placeholder)
        # self.setFixedHeight(30)
        # self.setFixedWidth(138)


