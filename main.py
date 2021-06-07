# This Python file uses the following encoding: utf-8
import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog

from form import Ui_MainWindow


class MainWindow(QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        uic.loadUi("form.ui", self)
        self.pushButton.clicked.connect(self.browser_file)
        self.show()

    def browser_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'C:/', 'Image files(*.iso)')
        self.lineEdit.setText(fname[0])


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()