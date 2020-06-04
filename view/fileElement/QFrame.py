from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QFrame


class QFrameElement(QFrame):

    def __init__(self, colorName):
        super().__init__()
        self.setStyleSheet(
            "background: "+colorName+";\n"
            "border : none;\n"
            "border-radius : 10px;\n")
        self.setContentsMargins(25, 25, 25, 25)

