from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QVBoxLayout,  QSpinBox, QLabel, QFormLayout,  QGroupBox, QDateEdit ,QDialog, QTabWidget, QWidget
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys

class Tab(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tab Widget')

        vbox = QVBoxLayout()
        tabWidget = QTabWidget()

        tabWidget.addTab(inputSimpan(), 'Simpan')
        tabWidget.addTab(inputPinjam(), 'Pinjam')

        vbox.addWidget(tabWidget)

        self.setLayout(vbox)

class inputSimpan(QWidget):
    def __init__(self):
        super().__init__()
        self.createFormGroupBox()

        title = "Koperasi ITK"
        left = 0
        right = 0
        width = 400
        height = 600
        iconName = "img/icon.png"

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)

        submitBtn = QPushButton("Submit")

        mainLayout.addWidget(submitBtn)

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, right, height, width)
        self.setLayout(mainLayout)

        self.show()

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox()
        self.formGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        layout = QFormLayout()
        tm = QDateEdit()
        tm.setCalendarPopup(True)
        layout.addRow(QLabel("Nama Nasabah :"), QLineEdit())
        layout.addRow(QLabel("Tanggal :"), tm)
        layout.addRow(QLabel("Jumlah Simpan:"), QLineEdit())
        self.formGroupBox.setLayout(layout)


class inputPinjam(QWidget):
    def __init__(self):
        super().__init__()
        self.createFormGroupBox()

        title = "Koperasi ITK"
        left = 0
        right = 0
        width = 400
        height = 600
        iconName = "img/icon.png"

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)

        submitBtn = QPushButton("Submit")

        mainLayout.addWidget(submitBtn)

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, right, height, width)
        self.setLayout(mainLayout)

        self.show()

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox()
        self.formGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        layout = QFormLayout()
        layout.addRow(QLabel("Nama Nasabah :"), QLineEdit())
        layout.addRow(QLabel("Tanggal :"), QDateEdit())
        layout.addRow(QLabel("Jumlah Pinjam:"), QLineEdit())
        self.formGroupBox.setLayout(layout)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    tabDialog = Tab()
    tabDialog.show()
    App.exec()
