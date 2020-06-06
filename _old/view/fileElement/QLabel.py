from PyQt5.QtWidgets import QLabel
from PyQt5 import QtGui

class QLabelElement(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)

        self.setFont(font)
