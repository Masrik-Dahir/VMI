# This Python file uses the following encoding: utf-8
import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget

from form import Ui_MainWindow


class MainWindow(QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        uic.loadUi("form.ui", self)
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()
