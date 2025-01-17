# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from PySide6.QtGui import QKeySequence,QShortcut

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
from ui_PrefWin import Ui_MainWindow as PrefWin_UI
import multiprocessing
import tkinter as tk
from HOF import HOF_Hanover as HOF_KMBHan
from HOF import ericcode

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
def search_in_slice(sliceee, name):
    for stop in sliceee:
        if stop.name == name:
            return stop
    return None
class ObservableList(list):
    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.callback = callback

    def _notify(self):
        if self.callback:
            self.callback()

    def __setitem__(self, index, value):
        super().__setitem__(index, value)
        self._notify()

    def append(self, value):
        super().append(value)
        self._notify()

    def extend(self, iterable):
        super().extend(iterable)
        self._notify()

    def insert(self, index, value):
        super().insert(index, value)
        self._notify()

    def remove(self, value):
        super().remove(value)
        self._notify()

    def pop(self, index=-1):
        value = super().pop(index)
        self._notify()
        return value

    def clear(self):
        super().clear()
        self._notify()

    def __delitem__(self, index):
        super().__delitem__(index)
        self._notify()

    def __iadd__(self, other):
        result = super().__iadd__(other)
        self._notify()
        return result

    def __imul__(self, other):
        result = super().__imul__(other)
        self._notify()
        return result
# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.ui = HOFView_Ui_MainWindow()
#         self.ui.setupUi(self)
class Main(QMainWindow):
    hof_class = HOF_KMBHan()
    opened_windows = []
    export_path = ""
    hofname = ""
    bus_rt_direction = 1
    # cross_method_dataqueue = ObservableList([None for _ in range(50)], callback=None)
    # head_index = 0
    # tail_index = 0
    cross_method_datum = [None for _ in range(50)]

    # def __init__(self, parent=None):
    #     super().__init__(parent)
    #     self.cross_method_dataqueue = ObservableList([None for _ in range(50)], callback=self.indexIncrement)
    #     self.head_index = 0
    #     self.tail_index = 0
    # def indexIncrement(self):
    #     # self.current_data_queue_index += 1
    #     # self.current_data_queue_index %= 50
    #     # self.next_queue_index +=1
    #     # self.next_queue_index %= 50
    def fileexplorer(self) -> str:

        path_Selected = QFileDialog.getExistingDirectory(None, 'Select Directory', 'C:\\')

        return path_Selected
    @staticmethod
    def raise_unimplemented() -> None:
        message = QMessageBox()
        message.setMinimumSize(200, 100)
        message.setWindowTitle("Error")
        message.setText("This feature is not yet implemented.")
        message.setIcon(QMessageBox.Critical) # type: ignore
        message.setStandardButtons(QMessageBox.Ok) # type: ignore
        message.exec()
    class PrefWin(QMainWindow):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.ui = PrefWin_UI()
            self.ui.setupUi(self)
            self.ui.plainTextEdit_3.setPlainText(Main.export_path)
            self.ui.plainTextEdit_3.textChanged.connect(self.set_path)
            self.ui.toolButton.clicked.connect(self.fileexplorer)
        def closewindow(self):
            self.close()
        def fileexplorer(self):
            Main.export_path = QFileDialog.getExistingDirectory(self, 'Select Directory', 'C:\\')
            self.ui.plainTextEdit_3.setPlainText(Main.export_path)
        def set_path(self):
            Main.export_path = self.ui.plainTextEdit_3.toPlainText()
            
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
                Main.hofname = file[0].split("/")[-1].removesuffix(".db")
                self.close()
                
                


        def open_hof(self):
            Main.hof_class = HOF_KMBHan()
            file = QFileDialog.getOpenFileName(self, 'Open HOF', 'C:\\', 'HOF Files (*.hof)')
            if file[0]:
                Main.hof_class.load_from_hof(file[0])
                Main.opened_windows.append(Main.HOFView())
                Main.opened_windows[-1].show()
                Main.hofname = file[0].split("/")[-1].removesuffix(".hof")
                self.close()

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
                self.ui.listWidget_3.addItem(i.name) #stopreporter
            for i in Main.hof_class.ddu:
                self.ui.listWidget_4.addItem(i.RTNO) #ddu
            for i in Main.hof_class.termini:
                self.ui.listWidget_5.addItem(ericcode(i.eric).retstr()) #termini
            for i in Main.hof_class.infosystem:
                self.ui.listWidget_2.addItem(i.route) #infosystem

            #----Infosystem Part----#
            self.ui.listWidget_2.itemSelectionChanged.connect(self.get_bsl)
            self.ui.listWidget_2.itemSelectionChanged.connect(self.change_rt_info)
            self.ui.pushButton.clicked.connect(self.dirchange_Y)
            self.ui.pushButton_2.clicked.connect(self.dirchange_Z)
            self.ui.listWidget.doubleClicked.connect(self.open_bs)
            
            #----Ctrl+S Shortcut----#
            self.shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
            self.shortcut.activated.connect(self.save)

        def open_bs(self):
            def search_bs(name: str, threads: int):
                ls = Main.hof_class.stopreporter
                slices = list(split(ls, threads))
                with multiprocessing.Pool(threads) as pool:
                    results = pool.starmap(search_in_slice, [(slice, name) for slice in slices])
                
                for result in results:
                    if result is not None:
                        return result
                return None

            item = self.ui.listWidget.currentItem()
            index = item.text()
            stop = search_bs(index, multiprocessing.cpu_count())
            if stop is not None:
                Main.opened_windows.append(Main.AddBusStop(None,stop.name, stop.EngDisplay,stop.ChiSeconds,stop.EngSeconds,stop.Outbound_sectionfare if isinstance(stop.Outbound_sectionfare,float) else -1.0,stop.Inbound_sectionfare if isinstance(stop.Inbound_sectionfare,float) else -1.0,True if stop.name[0] == "_" else False))
                Main.opened_windows[-1].show()
            else:
                QMessageBox.warning(self, "Error", f"Bus stop {index} not found.")
        def dirchange_Y(self):
            Main.bus_rt_direction = 1
            print(self.bus_rt_direction)
            self.get_bsl()
        def dirchange_Z(self):
            Main.bus_rt_direction = 2
            print(self.bus_rt_direction)
            self.get_bsl()
        def get_bsl(self):
            # print("hi")
            item =  self.ui.listWidget_2.currentIndex()
            index = item.row()
            self.ui.listWidget.clear()
            # for i in (Main.hof_class.infosystem[index].db_export_bsl1 if Main.HOFView.bus_rt_direction == 1 else Main.hof_class.infosystem[index].db_export_bsl2):
            #     self.ui.listWidget.addItem(i)
            # print(Main.hof_class.infosystem[index].busstop_list1 if Main.bus_rt_direction == 1 else Main.hof_class.infosystem[index].busstop_list2_class.db_export)
            self.ui.listWidget.addItems(Main.hof_class.infosystem[index].db_export_bsl1 if Main.bus_rt_direction == 1 else Main.hof_class.infosystem[index].busstop_list2_class.db_export)
        def change_rt_info(self):
            Main.bus_rt_direction = 1
            item =  self.ui.listWidget_2.currentIndex()
            index = item.row()
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(Main.hof_class.infosystem[index].route))
            self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(Main.hof_class.infosystem[index].direction1))
            self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(Main.hof_class.infosystem[index].direction2))
            # return Main.hof_class.infosystem[index].busstoplist1 if Main.HOFView.bus_rt_direction == 1 else Main.hof_class.infosystem[index].busstoplist2
        def save(self):
            if Main.hofname == "":
                Main.hofname = "Untitled"
            if Main.export_path == "":
                Main.export_path = Main().fileexplorer()
            Main.hof_class.save_to_db(Main.export_path + "/" + Main.hofname + ".db")
            import sqlite3
            conn = sqlite3.connect(Main.export_path + "/" + Main.hofname + ".db")
            c = conn.cursor()
            c.execute("create table if not exists prefs (key text, value text)")
            c.execute("insert into prefs values ('export_path', ?)", (Main.export_path,))
            QMessageBox.information(self, "Saved", "Saved to " + Main.export_path + "/" + Main.hofname + ".db")
        def closewindow(self):
            self.close()

    

    class AddBusStop(QMainWindow):
        def __init__(self, parent=None,name:str = "",engdisp:str="",chisec:int=0,engsec:int=0,osf:float=-1.0,isf:float=-1.0,autoskip:bool=False):
            super().__init__(parent)
            self.ui = AddBusStop_UI()
            self.ui.setupUi(self)
            self.ui.plainTextEdit.setPlainText(name)
            self.ui.plainTextEdit_2.setPlainText(engdisp)
            self.ui.spinBox.setValue(chisec)
            self.ui.spinBox_2.setValue(engsec)
            self.ui.doubleSpinBox.setValue(osf)
            self.ui.doubleSpinBox_2.setValue(isf)
            self.ui.checkBox.setChecked(autoskip)

        def get_bs(self):
            Main.raise_unimplemented()
            

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
