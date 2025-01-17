# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_HOFView import Ui_MainWindow as HOFView_Ui_MainWindow
from ui_Welc import Ui_MainWindow as Entrypoint_Ui_MainWindow
from ui_AddBusStop import Ui_MainWindow as AddBusStop_UI
from ui_AddDDU import Ui_MainWindow as AddDDU_UI
from ui_AddRouteEntry import Ui_MainWindow as AddRouteEntry_UI
from ui_AddTermini import Ui_MainWindow as AddTermini_UI
import tkinter as tk
from HOF import HOF_Hanover as HOF_KMBHan
from HOF import ericcode

# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.ui = HOFView_Ui_MainWindow()
#         self.ui.setupUi(self)
class Main(QMainWindow):
    hof_class = None
    opened_windows = []
    def raise_unimplemented():
        message = QMessageBox()
        message.setMinimumSize(200, 100)
        message.setWindowTitle("Error")
        message.setText("This feature is not yet implemented.")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok)
        message.exec()
    class Entrypoint(QMainWindow):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.ui = Entrypoint_Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.actionOpen_Project_Folder.triggered.connect(self.open_db)
            self.ui.actionOpen_HOF.triggered.connect(self.open_hof)
            self.ui.pushButton.clicked.connect(self.open_hof)
            self.ui.pushButton_2.clicked.connect(self.open_db)
            self.ui.pushButton_3.clicked.connect(self.open_globalcfg)
        def open_db(self):
            Main.hof_class = HOF_KMBHan()
            file = QFileDialog.getOpenFileName(self, 'Open Database', 'C:\\', 'Database Files (*.db)')
            if file[0]:
                Main.hof_class.load_from_db(file[0])
                Main.opened_windows.append(Main.HOFView())
                Main.opened_windows[-1].show()
                
                


        def open_hof(self):
            Main.hof_class = HOF_KMBHan()
            file = QFileDialog.getOpenFileName(self, 'Open HOF', 'C:\\', 'HOF Files (*.hof)')
            if file[0]:
                Main.hof_class.load_from_hof(file[0])

        def open_globalcfg(self):
            Main.raise_unimplemented()
        def closewindow(self):
            self.close()

    class HOFView(QMainWindow):
        bus_rt_direction = 1
        def __init__(self, parent=None):
            super().__init__(parent)
            self.ui = HOFView_Ui_MainWindow()
            self.ui.setupUi(self)
            for i in Main.hof_class.stopreporter:
                self.ui.listWidget_3.addItem(i.name)
            for i in Main.hof_class.ddu:
                self.ui.listWidget_4.addItem(i.RTNO)
            for i in Main.hof_class.termini:
                self.ui.listWidget_5.addItem(ericcode(i.eric).retstr())
            for i in Main.hof_class.infosystem:
                self.ui.listWidget_2.addItem(i.route)
            self.ui.listWidget_2.itemClicked.connect(self.get_bsl)
        def get_bsl(self):
            item =  self.ui.listWidget_2.currentIndex()
            index = item.row()
            self.ui.listWidget.clear()
            for i in (Main.hof_class.infosystem[index].busstoplist1 if Main.HOFView.bus_rt_direction == 1 else Main.hof_class.infosystem[index].busstoplist2):
                self.ui.listWidget.addItem(i.name)
            # return Main.hof_class.infosystem[index].busstoplist1 if Main.HOFView.bus_rt_direction == 1 else Main.hof_class.infosystem[index].busstoplist2

        def closewindow(self):
            self.close()

    

    class AddBusStop(QMainWindow):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.ui = AddBusStop_UI()
            self.ui.setupUi(self)

    class AddDDU(QMainWindow):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.ui = AddDDU_UI()
            self.ui.setupUi(self)

    class AddRouteEntry(QMainWindow):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.ui = AddRouteEntry_UI()
            self.ui.setupUi(self)

    class AddTermini(QMainWindow):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.ui = AddTermini_UI()
            self.ui.setupUi(self)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main.Entrypoint()
    widget.show()
    sys.exit(app.exec())
