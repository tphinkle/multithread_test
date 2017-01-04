# Python standard library
import sys
sys.path.append('/home/preston/Desktop/Programming/projects/multithreading_test/pyqtgraph-0.9.10/')

# Qt
import PyQt4.QtGui
import PyQt4.QtCore

# PyQtGraph
import pyqtgraph as pg


class MainView(PyQt4.QtGui.QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()

        self.resize(800, 600)

        self.setup_plot()
        self.setup_buttons()



    def setup_buttons(self):
        print 'setting up buttons'

        self._start_subclass_button = PyQt4.QtGui.QPushButton("Subclass\nStart", parent = self)
        self._start_subclass_button.setGeometry(100, 500, 100, 75)

        self._stop_subclass_button = PyQt4.QtGui.QPushButton("Subclass\nStop", parent = self)
        self._stop_subclass_button.setGeometry(300, 500, 100, 75)

        self._start_movetothread_button = PyQt4.QtGui.QPushButton("MoveToThread\nStart", parent = self)
        self._start_movetothread_button.setGeometry(500, 500, 100, 75)

        self._stop_movetothread_button = PyQt4.QtGui.QPushButton("MoveToThread\nStop", parent = self)
        self._stop_movetothread_button.setGeometry(700, 500, 100, 75)

        return

    def setup_plot(self):
        self._main_plot = pg.PlotWidget(parent = self)
        self._main_plot.setLabel('bottom', text = 'Time (s)')
        self._main_plot.setLabel('left', text = 'Signal')
        self._main_plot.showGrid(x = True, y = True, alpha = 1.0)
        self._main_plot.setGeometry(0,0,640,480)

        self._main_plot_item = pg.PlotDataItem()

        self._main_plot.addItem(self._main_plot_item)

        return
