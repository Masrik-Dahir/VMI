from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 2000, 2000)
    win.setWindowTitle("masrikdahir")

    label = QtWidgets.QLabel(win)
    label.setText("Coding is Awesome!")
    label.move(200,200)


    win.show()
    sys.exit(app.exec_())

window()