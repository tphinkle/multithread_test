# Python standard library
import time

# numpy
import numpy.random

# Qt
import PyQt4.QtCore
import PyQt4.QtGui

class SubClassModel(PyQt4.QtCore.QThread):

    new_data = PyQt4.QtCore.pyqtSignal('PyQt_PyObject')

    def __init__(self):
        super(SubClassModel, self).__init__()

        self._plot_period = .1 #ms


    @PyQt4.QtCore.pyqtSlot()
    def run(self):
        self._keep_going = True

        while(self._keep_going == True):
            self._data = numpy.random.random(1000)
            self.emit(PyQt4.QtCore.SIGNAL('new_data(PyQt_PyObject)'), self._data)

            time.sleep(self._plot_period)


    @PyQt4.QtCore.pyqtSlot()
    def interrupt(self):
        print 'stopping subclass loop'
        self._keep_going = False

        return
