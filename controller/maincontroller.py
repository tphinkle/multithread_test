# Qt
import PyQt4.QtCore
import PyQt4.QtGui



class MainController(PyQt4.QtCore.QObject):

    def __init__(self, main_model, main_view):
        super(MainController, self).__init__()

        self._main_model = main_model
        self._main_view = main_view

        self.make_connections()

        self._model_thread = PyQt4.QtCore.QThread()
        self._model_thread.start()

    def make_connections(self):
        # View to model

        # Subclass model
        self.connect(self._main_view._start_subclass_button,\
         PyQt4.QtCore.SIGNAL('clicked()'), self, PyQt4.QtCore.SLOT('start_subclass()'))

        self.connect(self._main_view._stop_subclass_button,\
         PyQt4.QtCore.SIGNAL('clicked()'), self, PyQt4.QtCore.SLOT('stop_subclass()'))



         # MoveToThread model
        self.connect(self._main_view._start_movetothread_button,\
         PyQt4.QtCore.SIGNAL('clicked()'), self, PyQt4.QtCore.SLOT('start_movetothread()'))

        self.connect(self._main_view._stop_movetothread_button,\
        PyQt4.QtCore.SIGNAL('clicked()'), self, PyQt4.QtCore.SLOT('stop_movetothread()'))

    @PyQt4.QtCore.pyqtSlot()
    def start_subclass(self):
        self._subclass_model.run()
        return

    @PyQt4.QtCore.pyqtSlot()
    def stop_subclass(self):
        self._subclass_model.quit()
        return

    @PyQt4.QtCore.pyqtSlot()
    def start_movetothread(self):

        return

    @PyQt4.QtCore.pyqtSlot()
    def stop_movetothread(self):

        return
