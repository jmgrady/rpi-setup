# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):  # type: ignore[no-untyped-def]
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
