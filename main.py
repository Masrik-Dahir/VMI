# This Python file uses the following encoding: utf-8
import os
import sys
from threading import Thread

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog
from form import Ui_MainWindow


class MainWindow(QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        uic.loadUi("form.ui", self)
        self.pushButton.clicked.connect(self.browser_file)
        self.pushButton_3.clicked.connect(self.dropdown_selection)
        # self.graphicsView
        self.show()

    def browser_file(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open File', 'C:/', 'Dumps (*.mem *.vmem)')
        self.lineEdit.setText(self.fname[0])

        print(self.fname[0])
        location = 'python2.7 volatility/vol.py imageinfo -f ' + self.fname[0]
        p = os.popen(location).read()
        print(p)
        splitted = p.split('\n', 1)
        profiles = splitted[0].strip()
        print(profiles)
        profiles = profiles.split(',')
        print(profiles)
        #index = profiles[0].find("Win")
        #print(index)
        i=0
        while i < len(profiles):
            index = profiles[0].find("Win")
            suggested = profiles[0][index:]
            profiles[0] = suggested.strip()
            i+=1
        print(profiles)
        first = profiles[0]
        pslist = 'python2.7 volatility/vol.py --profile=' + first + ' pslist -f ' + self.fname[0]
        p = os.popen(pslist).read()
        print(p)
        splitted = p.split('\n', 2)
        processes = splitted[2].split('\n')
        for string in processes:
            print(string)


    def dropdown_selection(self):
        a = self.comboBox.currentText()
        if (str(a) == 'Observe'):
            location = 'python2.7 volatility/vol.py imageinfo -f ' + self.fname[0]
            p = os.popen(location).read()
            print(p)
            splitted = p.split('\n', 1)
            profiles = splitted[0].strip()
            print(profiles)
            profiles = profiles.split(',')
            print(profiles)
            # index = profiles[0].find("Win")
            # print(index)
            i = 0
            while i < len(profiles):
                index = profiles[0].find("Win")
                suggested = profiles[0][index:]
                profiles[0] = suggested.strip()
                i += 1
            print(profiles)
            first = profiles[0]
            pslist = 'python2.7 volatility/vol.py --profile=' + first + ' pslist -f ' + self.fname[0]
            p = os.popen(pslist).read()
            print(p)
            splitted = p.split('\n', 2)
            processes = splitted[2].split('\n')

            for string in processes:
                self.graphicsView.scene().addText(string)
                print(string)
            self.graphicsView.show()

        if (str(a) == 'Modify'):
            print(a)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()