import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

Ui_MainWindow, QtBaseClass = uic.loadUiType("VMI_GUI.ui")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        self.graphics()

    def graphics (self):
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        pen = QtGui.QPen(QtCore.Qt.green)
        side = 20

        for i in range(100):
            for j in range(100):
                r = QtCore.QRectF(QtCore.QPointF(i * side, j * side), QtCore.QSizeF(side, side))
                scene.addRect(r, pen)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
