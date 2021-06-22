# This Python file uses the following encoding: utf-8
import os
import re
import sys
from random import randint
from threading import Thread

from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QImage, QMouseEvent, QColor
from PyQt5.QtWidgets import QWidget, QFileDialog, QGraphicsScene, QGraphicsView, QGraphicsSceneMouseEvent, \
    QGraphicsProxyWidget, QGraphicsItem, QGraphicsWidget

from form import Ui_MainWindow
from process import process


def reverse(a):
    txt = a[::-1]
    return txt


class MainWindow(QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        uic.loadUi("form.ui", self)
        self.pushButton.clicked.connect(self.browser_file)
        self.pushButton_3.clicked.connect(self.dropdown_selection)
        self.pid_pushButton.clicked.connect(self.show_datastructure)
        self.pushButton_6.clicked.connect(self.profile_work)
        self.scene = QGraphicsScene(self)
        self.processes_scene = QGraphicsScene(self)
        self.show()

    def browser_file(self):
        print('Upload Button Clicked!')
        self.fname = QFileDialog.getOpenFileName(self, 'Open File', 'C:/', 'Dumps (*.mem *.vmem)')
        self.lineEdit.setText(self.fname[0])

        self.text = ""

        print("Observe dropdown selected!")
        location = 'python2.7 volatility/vol.py imageinfo -f ' + self.fname[0]
        p = os.popen(location).read()
        # print(p)
        l = [i for i in p.split('\n')]
        l = [i for i in l[0].split(':')]
        l = [i.replace(" ", "") for i in l[1].split(',')]
        [self.comboBox_2.addItem(i) for i in l]

        self.text += p + '\n'
        splitted = p.split('\n', 1)
        profiles = splitted[0].strip()
        # print(profiles)
        self.text += profiles + '\n'
        profiles = profiles.split(',')
        # print(profiles)
        self.text += str(profiles) + '\n'
        # index = profiles[0].find("Win")
        # print(index)
        i = 0
        self.important = ""
        while i < len(profiles):
            index = profiles[0].find("Win")
            suggested = profiles[0][index:]
            profiles[0] = suggested.strip()
            i += 1
        # print(profiles)
        self.text += str(profiles) + '\n'
        first = profiles[0]
        pslist = 'python2.7 volatility/vol.py --profile=' + first + ' pslist -f ' + self.fname[0]

        p = os.popen(pslist).read()
        # print(p)
        self.text += str(p) + '\n'
        self.important += str(p) + '\n'
        splitted = p.split('\n', 2)
        self.processes = splitted[2].split('\n')

        x = 0
        process_list = []
        for string in self.processes:
            self.important += str(string) + '\n'
            asd = re.sub(' +', ' ', string).split(' ')
            if asd != ['']:
                process_list.append(asd)
            self.rect_item = QtWidgets.QGraphicsRectItem(QtCore.QRectF(x, 0, 200, 500))
            a1 = randint(0, 255)
            a2 = randint(0, 255)
            a3 = randint(0, 255)
            a4 = randint(0, 255)
            self.rect_item.setBrush(QColor(a1, a2, a3, a4))
            x += 200

            self.processes_scene.addItem(self.rect_item)

        self.obj = []
        for i in process_list:
            p = process(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10])
            self.obj.append(p)

        # print([i.get_pid() for i in self.obj])



    def dropdown_selection(self):

        print("Select Button clicked!")
        a = self.comboBox.currentText()
        if str(a) == 'Observe':
            self.text += self.important
            self.scene.addText(self.text)
            self.graphicsView.setScene(self.scene)
            print("The processes are printed on the GraphicView window!")

        if str(a) == 'Processes':
            print("Processes dropdown chosen")
            self.graphicsView.setScene(self.processes_scene)
            print("Done")

        if str(a) == 'Modify':
            print(a)

    def show_datastructure(self):
        print("PID Select Button clicked!")
        PID = self.pid_lineEdit.text()


    def profile_work(self):
        print("Profile Select Button clicked!")
        combo_2 = self.comboBox_2.currentText()

        location = 'python2.7 volatility/vol.py --profile='+combo_2+' -f ' + self.fname[0] + ' volshell'
        p = os.popen(location).read()
        command = "sc()"
        p = os.popen(command).read()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()

