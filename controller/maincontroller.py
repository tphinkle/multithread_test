# Qt
import PyQt4.QtCore
import PyQt4.QtGui



class MainController(PyQt4.QtCore.QObject):

    def __init__(self, subclass_model, main_view):
        super(MainController, self).__init__()

        self._subclass_model = subclass_model
        self._main_view = main_view

        self.make_connections()


    def make_connections(self):
        # View to model

        # Subclass model
        self.connect(self._main_view._start_subclass_button,\
         PyQt4.QtCore.SIGNAL('clicked()'), self, PyQt4.QtCore.SLOT('start_subclass()'))

        self.connect(self._subclass_model,\
        PyQt4.QtCore.SIGNAL('new_data(PyQt_PyObject)'), self, PyQt4.QtCore.SLOT('update_plot(PyQt_PyObject)'))

        self.connect(self._main_view._stop_subclass_button,\
         PyQt4.QtCore.SIGNAL('clicked()'), self, PyQt4.QtCore.SLOT('stop_subclass()'))



         # MoveToThread model
        self.connect(self._main_view._start_movetothread_button,\
         PyQt4.QtCore.SIGNAL('clicked()'), self, PyQt4.QtCore.SLOT('start_movetothread()'))

        self.connect(self._main_view._stop_movetothread_button,\
        PyQt4.QtCore.SIGNAL('clicked()'), self, PyQt4.QtCore.SLOT('stop_movetothread()'))

    @PyQt4.QtCore.pyqtSlot()
    def start_subclass(self):
        self._subclass_model.start()
        return

    @PyQt4.QtCore.pyqtSlot()
    def stop_subclass(self):
        self._subclass_model.exit()
        return

    @PyQt4.QtCore.pyqtSlot()
    def start_movetothread(self):

        return

    @PyQt4.QtCore.pyqtSlot()
    def stop_movetothread(self):

        return

    @PyQt4.QtCore.pyqtSlot('PyQt_PyObject')
    def update_plot(self, data):
        self._main_view._main_plot_item.setData(data)

        return
