import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.uic.properties import QtWidgets
from VMI_GUI import Ui_MainWindow


Ui_MainWindow, QtBaseClass = uic.loadUiType("VMI_GUI.ui")


class Ui(QtBaseClass, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        self.resize(1024, 640)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec())
