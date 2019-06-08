#-*- coding:utf-8 -*-

import sys
#PyQt must be installed.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

formClass = uic.loadUiType('ui.ui')[0]

class MainformClass(QMainWindow, formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.calc)
        self.pushButton.clicked.connect(self.ev)

    def calc(self):
        inputed = self.lineEdit.text()
        self.label.setText(inputed)

    def ev(self):
        inputed = self.lineEdit.text()
        self.label.setText(str(eval(inputed)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainformClass()
    mainWindow.show()
    app.exec_()