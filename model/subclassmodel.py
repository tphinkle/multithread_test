# Python standard library
import time

# numpy
import numpy.random

# Qt
import PyQt4.QtCore
import PyQt4.QtGui

class MainModel(PyQt4.QtCore.QObject):

    def __init__(self):
        super(MainModel, self).__init__()

        self._plot_period = 1 #ms


    @PyQt4.QtCore.pyqtSlot()
    def run(self):
        self._keep_going = True

        while(self._keep_going == True):

            time.sleep(self._plot_period)

            return

    @PyQt4.QtCore.pyqtSlot()
    def interrupt(self):
        self._keep_going = False

        return
