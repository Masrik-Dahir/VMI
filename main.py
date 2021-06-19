# This Python file uses the following encoding: utf-8
import os
import sys
from threading import Thread

from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QImage, QMouseEvent
from PyQt5.QtWidgets import QWidget, QFileDialog, QGraphicsScene, QGraphicsView, QGraphicsSceneMouseEvent, \
    QGraphicsProxyWidget, QGraphicsItem, QGraphicsWidget

from form import Ui_MainWindow


def reverse(a):
    txt = a[::-1]
    return txt


class MainWindow(QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        uic.loadUi("form.ui", self)
        self.pushButton.clicked.connect(self.browser_file)
        self.pushButton_3.clicked.connect(self.dropdown_selection)
        # self.graphicsView
        self.show()

    def browser_file(self):
        print('Upload Button Clicked!')
        self.fname = QFileDialog.getOpenFileName(self, 'Open File', 'C:/', 'Dumps (*.mem *.vmem)')
        self.lineEdit.setText(self.fname[0])

        # print(self.fname[0])
        # location = 'python2.7 volatility/vol.py imageinfo -f ' + self.fname[0]
        # p = os.popen(location).read()
        # print(p)
        # splitted = p.split('\n', 1)
        # profiles = splitted[0].strip()
        # print(profiles)
        # profiles = profiles.split(',')
        # print(profiles)
        # #index = profiles[0].find("Win")
        # #print(index)
        # i=0
        # while i < len(profiles):
        #     index = profiles[0].find("Win")
        #     suggested = profiles[0][index:]
        #     profiles[0] = suggested.strip()
        #     i+=1
        # print(profiles)
        # first = profiles[0]
        # pslist = 'python2.7 volatility/vol.py --profile=' + first + ' pslist -f ' + self.fname[0]
        # p = os.popen(pslist).read()
        # print(p)
        # splitted = p.split('\n', 2)
        # processes = splitted[2].split('\n')
        # for string in processes:
        #     print(string)


    def dropdown_selection(self):
        print("Select Button clicked!")
        scene = QGraphicsScene()
        text = ""
        a = self.comboBox.currentText()
        if (str(a) == 'Observe'):
            print("Observe dropdown selected!")
            location = 'python2.7 volatility/vol.py imageinfo -f ' + self.fname[0]
            p = os.popen(location).read()
            # print(p)
            text+=p + '\n'
            splitted = p.split('\n', 1)
            profiles = splitted[0].strip()
            # print(profiles)
            text+=profiles + '\n'
            profiles = profiles.split(',')
            # print(profiles)
            text+=str(profiles) + '\n'
            # index = profiles[0].find("Win")
            # print(index)
            i = 0
            important = ""
            while i < len(profiles):
                index = profiles[0].find("Win")
                suggested = profiles[0][index:]
                profiles[0] = suggested.strip()
                i += 1
            # print(profiles)
            text+=str(profiles) + '\n'
            first = profiles[0]
            pslist = 'python2.7 volatility/vol.py --profile=' + first + ' pslist -f ' + self.fname[0]
            p = os.popen(pslist).read()
            # print(p)
            text+=str(p) + '\n'
            important+=str(p)+'\n'
            splitted = p.split('\n', 2)
            processes = splitted[2].split('\n')

            for string in processes:
                # print(string)
                important += str(string) + '\n'

        # scene.addText(text)
        scene.addText(important)
        self.graphicsView.setScene(scene)

        print("The processes are printed on the GraphicView window!")

        if (str(a) == 'Modify'):
            print(a)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()