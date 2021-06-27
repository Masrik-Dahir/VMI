# This Python file uses the following encoding: utf-8
import os
import re
import sys, threading
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog, QGraphicsScene, QApplication
from form import Ui_MainWindow
from process import process
import time


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
        self.pushButton_6.clicked.connect(self.start_thread)
        self.scene = QGraphicsScene(self)
        self.processes_scene = QGraphicsScene(self)
        self.exit_pushButton.clicked.connect(self.quit)
        self.text = ""
        self.important = ""
        self.show()

    def browser_file(self):
        print('Upload Button Clicked!')
        processes_scene = QGraphicsScene(self)
        self.fname = QFileDialog.getOpenFileName(self, 'Open File', 'C:/', 'Dumps (*.mem *.vmem)')
        self.lineEdit.setText(self.fname[0])
        text = ""
        important = ""
        scene = QGraphicsScene(self)

        print("Observe dropdown selected!")
        location = 'python2.7 volatility/vol.py imageinfo -f ' + self.fname[0]
        p = os.popen(location).read()
        # print(p)
        l = [i for i in p.split('\n')]
        l = [i for i in l[0].split(':')]
        l = [i.replace(" ", "") for i in l[1].split(',')]
        [self.comboBox_2.addItem(i) for i in l]

        text += p + '\n'
        splitted = p.split('\n', 1)
        profiles = splitted[0].strip()
        text += profiles + '\n'
        profiles = profiles.split(',')
        text += str(profiles) + '\n'
        i = 0

        while i < len(profiles):
            index = profiles[0].find("Win")
            suggested = profiles[0][index:]
            profiles[0] = suggested.strip()
            i += 1
        text += str(profiles) + '\n'
        first = profiles[0]
        pslist = 'python2.7 volatility/vol.py --profile=' + first + ' pslist -f ' + self.fname[0]

        p = os.popen(pslist).read()
        print(p)
        text += str(p) + '\n'
        self.text = text
        important += str(p) + '\n'
        splitted = p.split('\n', 2)
        self.processes = splitted[2].split('\n')

        x = 0
        process_list = []
        dropdown_pid_list = []

        for string in self.processes:
            important += str(string) + '\n'
            asd = re.sub(' +', ' ', string).split(' ')

            if asd != ['']:
                process_list.append(asd)
        self.important = important
        self.text += self.important
        scene.addText(self.text)
        self.obj = []
        x = 0
        y = 0
        next_y = 0
        for i in process_list:

            if len(self.obj) % 8 == 0 and len(self.obj) != 1:
                y = y + 320
                x = 0
                next_y = next_y + 320

            p = process(x, y, next_y, i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            x = x + 320

            self.obj.append(p)
            processes_scene.addItem(p.get_rect_item())
            processes_scene.addItem(p.get_offset())
            processes_scene.addItem(p.get_name())
            processes_scene.addItem(p.get_pid())
            processes_scene.addItem(p.get_ppid())
            processes_scene.addItem(p.get_thds())
            processes_scene.addItem(p.get_hnds())
            processes_scene.addItem(p.get_sess())
            processes_scene.addItem(p.get_wow64())

            self.processes_scene = processes_scene
            dropdown_pid_list.append(p.get_pid_dropdown())


        self.pid_comboBox.addItems(dropdown_pid_list)
        self.scene = scene

    def dropdown_selection(self):

        print("Select Button clicked!")
        a = self.comboBox.currentText()
        if str(a) == 'Observe':
            scene = self.scene
            self.graphicsView.setScene(scene)
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

    def start_thread(self):
        thread1 = threading.Thread(target=self.profile_work)
        thread1.start()
        time.sleep(7)
        # p = os.popen("sc()").read()
        # p = os.popen("mc()").read()
        # p = os.popen("pc()").read()

    def profile_work(self):
        self.pushButton_6.setDisabled(True)
        print("Profile Select Button clicked!")
        combo_2 = self.comboBox_2.currentText()
        location = 'python2.7 volatility/vol.py --profile='+combo_2+' -f ' + self.fname[0] + ' volshell'
        p = os.popen(location).read()
        command = "sc()"

    def quit(self):
        sys.exit()



app = QtWidgets.QApplication(sys.argv)
QApplication.setStyle("Fusion")
window = MainWindow()
app.exec_()

