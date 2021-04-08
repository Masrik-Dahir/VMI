import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

Ui_MainWindow, QtBaseClass = uic.loadUiType("VMI_GUI.ui")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        self.viewer = GraphicsWindow(self)


class GraphicsWindow(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super(GraphicsWindow, self).__init__(parent)
        self._scene = QtWidgets.QGraphicsScene(self)
        self.graphicsView.setScene(self._scene)
        self.setScene(self._scene)
        pen = QtGui.QPen(QtCore.Qt.green)
        side = 20

        for i in range(100):
            for j in range(100):
                r = QtCore.QRectF(QtCore.QPointF(i * side, j * side), QtCore.QSizeF(side, side))
                scene.addRect(r, pen)
                r = print([j])

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            factor = 1.25
            self._zoom += 1
        else:
            factor = 0.8
            self._zoom -= 1
        if self._zoom > 0:
            self.scale(factor, factor)
        else:
            self._zoom = 0


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
