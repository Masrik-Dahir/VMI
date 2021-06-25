from random import randint
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsTextItem, QGraphicsRectItem


class process(QGraphicsRectItem):
    def __init__(self, x_location, offset, name, pid, ppid, thds, hnds, sess, wow64):
        super().__init__()
        self.x_location = x_location
        self.offset = offset
        self.name = name
        self.pid = pid
        self.ppid = ppid
        self.thds = thds
        self.hnds = hnds
        self.sess = sess
        self.wow64 = wow64
        # self.start = start
        # self.exit = exit



        self.dic = {}
        self.dic['offset'] = self.offset
        self.dic['name'] = self.name
        self.dic['pid'] = self.pid
        self.dic['ppid'] = self.ppid
        self.dic['thds'] = self.thds
        self.dic['hnds'] = self.hnds
        self.dic['sess'] = self.sess
        self.dic['wow64'] = self.wow64
        # self.dic['start'] = self.start
        # self.dic['exit'] = self.exit

        #self.pid_text = QtWidgets.QGraphicsTextItem("test")
        self.rect_item = QtWidgets.QGraphicsRectItem(QtCore.QRectF(x_location, 0, 200, 500))




        a1 = randint(0, 255)
        a2 = randint(0, 255)
        a3 = randint(0, 255)
        a4 = randint(0, 255)
        self.rect_item.setBrush(QColor(a1, a2, a3, a4))

        self.gui_offset = QGraphicsTextItem()
        self.gui_name = QGraphicsTextItem()
        self.gui_pid = QGraphicsTextItem()
        self.gui_ppid = QGraphicsTextItem()
        self.gui_thds = QGraphicsTextItem()
        self.gui_hnds = QGraphicsTextItem()
        self.gui_sess = QGraphicsTextItem()
        self.gui_wow64 = QGraphicsTextItem()
        # self.gui_start = QGraphicsTextItem()
        # self.gui_exit = QGraphicsTextItem()

        self.gui_offset.setPos(self.x_location, 0)
        self.gui_offset.setPlainText("Offset: " + self.offset)

        self.gui_name.setPos(self.x_location, 35)
        self.gui_name.setPlainText("Name: " + self.name)

        self.gui_pid.setPos(self.x_location, 70)
        self.gui_pid.setPlainText("PID: " + self.pid)

        self.gui_ppid.setPos(self.x_location, 105)
        self.gui_ppid.setPlainText("PPID: " + self.ppid)

        self.gui_thds.setPos(self.x_location, 140)
        self.gui_thds.setPlainText("Threads: " + self.thds)

        self.gui_hnds.setPos(self.x_location, 175)
        self.gui_hnds.setPlainText("Handles: " + self.hnds)

        self.gui_sess.setPos(self.x_location, 210)
        self.gui_sess.setPlainText("Session: " + self.sess)

        self.gui_wow64.setPos(self.x_location, 245)
        self.gui_wow64.setPlainText("wow64: " + self.wow64)

        # self.gui_start.setPos(self.x_location, 315)
        # self.gui_start.setPlainText("Start: " + self.start)
        #
        # self.gui_exit.setPos(self.x_location, 350)
        # self.gui_exit.setPlainText("Exit: " + self.exit)

    def handleDoubleClick(self):
        print("Helo")


    def get_offset(self):
        return self.gui_offset

    def get_name(self):
        return self.gui_name

    def get_pid(self):
        return self.gui_pid

    def get_ppid(self):
        return self.gui_ppid

    def get_thds(self):
        return self.gui_thds

    def get_sess(self):
        return self.gui_sess

    def get_wow64(self):
        return self.gui_wow64


    # def get_start(self):
    #     return self.gui_start
    #
    # def get_exit(self):
    #     return self.gui_exit

    def get_hnds(self):
        return self.gui_hnds

    def toString(self):
        return self.dic

    def get_rect_item(self):
        return self.rect_item


