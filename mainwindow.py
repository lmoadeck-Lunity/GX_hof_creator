# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from PySide6.QtGui import QCloseEvent, QKeySequence,QShortcut
from PySide6.QtCore import Signal, Slot, QTimer
from threading import Thread
from time import sleep
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
import copy
import tkinter as tk
import os
from HOF import HOF_Hanover as HOF_KMBHan
from HOF import ericcode
from collections import deque
global build_with_genLED
build_with_genLED = False
def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
def search_in_slice(sliceee, name):
    for index, stop in enumerate(sliceee):
        if stop.name == name:
            return stop, index
    return None, -1
    
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
    # bus_rt_direction = 1
    # cross_method_dataqueue = ObservableList([None for _ in range(50)], callback=None)
    # head_index = 0
    # tail_index = 0
    cur_instance = None
    cross_method_datum = deque([Signal(int) for _ in range(1)], maxlen=50)  
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
    @staticmethod
    def maybeSave(lst:list) -> bool:
        if any(lst):
            ret = QMessageBox.warning(None, "Application", "The document has been modified.\nDo you want to save your changes?", QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel) #type: ignore
            if ret == QMessageBox.Save: #type: ignore
                return True
            elif ret == QMessageBox.Cancel: #type: ignore
                return False
        return True
    
    @staticmethod
    def fileexplorer() -> str:

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
            self.ui.lineEdit.setText(Main.export_path)
            self.ui.lineEdit.textChanged.connect(self.set_path)
            self.ui.lineEdit_2.setText(Main.hofname)
            self.ui.lineEdit_2.textChanged.connect(lambda: setattr(Main, "hofname", self.ui.lineEdit_2.text()))
            self.ui.toolButton.clicked.connect(self.fileexplorer)
        def closewindow(self):
            self.close()
        def fileexplorer(self):
            Main.export_path = QFileDialog.getExistingDirectory(self, 'Select Directory', 'C:\\')
            self.ui.lineEdit.setText(Main.export_path)
        def set_path(self):
            Main.export_path = self.ui.lineEdit.text()
            
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
                Main.export_path = file[0].removesuffix(Main.hofname + ".db")
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
        closed = Signal()
        def __init__(self, parent=None):
            super().__init__(parent)
            self.ui = HOFView_Ui_MainWindow()
            self.ui.setupUi(self)
            # for i in Main.hof_class.stopreporter:
            #     self.ui.listWidget_3.addItem(i.name) #stopreporter
            # for i in Main.hof_class.ddu:
            #     self.ui.listWidget_4.addItem(i.RTNO) #ddu
            # for i in Main.hof_class.termini:
            #     self.ui.listWidget_5.addItem(ericcode(i.eric).retstr()) #termini
            # for i in Main.hof_class.infosystem:
            #     self.ui.listWidget_2.addItem(i.route) #infosystem
            self.ui.listWidget_3.addItems([i.name for i in Main.hof_class.stopreporter])
            self.ui.listWidget_4.addItems([i.RTNO for i in Main.hof_class.ddu])
            self.ui.listWidget_5.addItems([i.destination for i in Main.hof_class.termini])
            self.ui.listWidget_2.addItems([i.route for i in Main.hof_class.infosystem])
            self.ui.actionExport_HOF.triggered.connect(self.export_hof)
            self.ui.actionSave_to_DB.triggered.connect(self.save)
            self.ui.actionPreferences.triggered.connect(self.open_pref)
            self.ui.actionGenerate_8w_6w_LCD.triggered.connect(self.generate_8w_6w_LCD)
            self.ui.actionGenerate_DPIPv2.triggered.connect(self.generate_8w_6w_LCD)
            self.ui.actionOpen_global_cfg.triggered.connect(lambda: Main.raise_unimplemented())
            self.ui.actionOpen_HOF.triggered.connect(self.reopen_hof)
            self.ui.actionOpen_Project_Folder.triggered.connect(self.open_db)
            self.ui.actionOpen_TTL_for_Route.triggered.connect(lambda: Main.raise_unimplemented())  
            
            # self.ui.act
            #----                               ----#
            # thread = Thread(target=self.update_listviews_every_3_minutes)
            # thread.start()
            # self.update_listviews_every_3_minutes() # Probably not needed anymore
            #----Termini, DDU, Stopreporter Part----#
            self.ui.listWidget_3.doubleClicked.connect(self.open_bs_lw3)
            self.ui.listWidget_4.doubleClicked.connect(self.open_ddu)
            self.ui.listWidget_5.doubleClicked.connect(self.open_termini)
            
            self.ui.pushButton_3.clicked.connect(lambda: self.add_stuff(1))
            self.ui.pushButton_7.clicked.connect(lambda: self.add_stuff(2))
            self.ui.pushButton_14.clicked.connect(lambda: self.add_stuff(3))
            
            self.ui.pushButton_5.clicked.connect(lambda: self.delete_stuff(1))
            self.ui.pushButton_8.clicked.connect(lambda: self.delete_stuff(2))
            self.ui.pushButton_15.clicked.connect(lambda: self.delete_stuff(3))

            self.ui.pushButton_11.clicked.connect(lambda: self.duplicate_stuff(1))
            self.ui.pushButton_13.clicked.connect(lambda: self.duplicate_stuff(2))
            self.ui.pushButton_16.clicked.connect(lambda: self.duplicate_stuff(3))

            self.ui.pushButton_23.clicked.connect(lambda: self.sort_stuff(1))
            self.ui.pushButton_22.clicked.connect(lambda: self.sort_stuff(2))
            self.ui.pushButton_21.clicked.connect(lambda: self.sort_stuff(3))

            #----Infosystem Part----#
            self.ui.listWidget_2.itemSelectionChanged.connect(self.change_rt_info)
            self.ui.listWidget_2.itemSelectionChanged.connect(self.get_bsl)
            
            # self.ui.listWidget_2.itemSelectionChanged.connect(self.dirchange_Y) # shit change
            self.ui.pushButton.clicked.connect(self.dirchange_Y)
            self.ui.pushButton_2.clicked.connect(self.dirchange_Z)
            self.ui.listWidget.doubleClicked.connect(self.open_bs)
            self.ui.listWidget_2.doubleClicked.connect(self.open_rt)
            self.ui.pushButton_9.clicked.connect(lambda: self.add_stuff(4))
            self.ui.pushButton_10.clicked.connect(lambda: self.delete_stuff(4))
            self.ui.pushButton_12.clicked.connect(lambda: self.duplicate_stuff(4))
            self.ui.pushButton_4.clicked.connect(self.add_bs_from_sel)
            self.ui.pushButton_6.clicked.connect(self.del_bs_from_sel)
            self.ui.pushButton_20.clicked.connect(self.change_bs_FromSel)
            self.ui.toolButton_4.clicked.connect(self.bsl_goup)
            self.ui.toolButton_3.clicked.connect(self.bsl_godown)
            self.ui.pushButton_18.clicked.connect(self.check_bsl_validity)
            self.ui.pushButton_24.clicked.connect(self.check_all_bsl_validity)
            # self.ui.pushButton_5
            #----Ctrl+S Shortcut----#
            self.shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
            self.shortcut.activated.connect(self.save)
        def add_stuff(self,stuff:int):
            dct = {
                1: (Main.hof_class.stopreporter, self.ui.listWidget_3),
                2: (Main.hof_class.ddu, self.ui.listWidget_4),
                3: (Main.hof_class.termini, self.ui.listWidget_5),
                4: (Main.hof_class.infosystem, self.ui.listWidget_2)
            }
            if stuff == 1:
                lenth = len(Main.hof_class.stopreporter)
                Main.hof_class.add_stopreporter(f"NS{lenth}", "New Stop", 0, 0, -1.0, -1.0)
                Main.opened_windows.append(Main.AddBusStop(None,f"NS{lenth}", "New Stop", 0, 0, -1.0, -1.0,curindex=lenth))
                Main.opened_windows[-1].show()
                dct[stuff][1].addItem(f"NS{lenth}")
            elif stuff == 2:
                lenth = len(Main.hof_class.ddu)
                Main.hof_class.add_ddu(f"RT{lenth}", "Outbound", "Inbound", -1.0, -1.0, 0, 0)
                Main.opened_windows.append(Main.AddDDU(None,f"RT{lenth}", "Outbound", "Inbound", -1.0, -1.0, 0, 0,curindex=lenth))
                Main.opened_windows[-1].show()
                dct[stuff][1].addItem(f"RT{lenth}")
            elif stuff == 3:
                lenth = len(Main.hof_class.termini)
                Main.hof_class.add_terminus(False, f"{lenth}A", "","",[],f"{lenth}B")
                Main.opened_windows.append(Main.AddTermini(None,f"{lenth}A", "", "", [],curindex=lenth))
                Main.opened_windows[-1].show()
                dct[stuff][1].addItem(f"{lenth}A")
            elif stuff == 4:
                lenth = len(Main.hof_class.infosystem)
                Main.hof_class.add_infosystem(False, f"R{lenth}", "Outbound", "Inbound", [], [])
                Main.opened_windows.append(Main.AddRouteEntry(None,False,f"R{lenth}", "Outbound", "Inbound",curindex=lenth))
                dct[stuff][1].addItem(f"R{lenth}")
            
        def duplicate_stuff(self, stuff: int):
            dct = {
                1: (Main.hof_class.stopreporter, self.ui.listWidget_3),
                2: (Main.hof_class.ddu, self.ui.listWidget_4),
                3: (Main.hof_class.termini, self.ui.listWidget_5),
                4: (Main.hof_class.infosystem, self.ui.listWidget_2)
            }
            if stuff == 1:
                ite = self.ui.listWidget_3.currentIndex()
                index = ite.row()
                original = Main.hof_class.stopreporter[index]
                new_item = copy.deepcopy(original)
                Main.hof_class.stopreporter.insert(index, new_item)
                self.ui.listWidget_3.insertItem(index, new_item.name)
            elif stuff == 2:
                ite = self.ui.listWidget_4.currentIndex()
                index = ite.row()
                original = Main.hof_class.ddu[index]
                new_item = copy.deepcopy(original)
                Main.hof_class.ddu.insert(index, new_item)
                self.ui.listWidget_4.insertItem(index, new_item.RTNO)
            elif stuff == 3:
                ite = self.ui.listWidget_5.currentIndex()
                index = ite.row()
                original = Main.hof_class.termini[index]
                new_item = copy.deepcopy(original)
                Main.hof_class.termini.insert(index, new_item)
                self.ui.listWidget_5.insertItem(index, new_item.eric)
            elif stuff == 4:
                ite = self.ui.listWidget_2.currentIndex()
                index = ite.row()
                original = Main.hof_class.infosystem[index]
                new_item = copy.deepcopy(original)
                Main.hof_class.infosystem.insert(index, new_item)
                self.ui.listWidget_2.insertItem(index, new_item.route)

            # elif stuff == 2:
            #     ite = self.ui.listWidget_4.currentIndex()
            #     index = ite.row()
            #     original = Main.hof_class.ddu[index]
            #     new_item = type(original)(**original.__dict__)  # Create a new instance with the same attributes
            #     Main.hof_class.ddu.insert(index, new_item)
            #     self.ui.listWidget_4.insertItem(index, new_item.RTNO)
            # elif stuff == 3:
            #     ite = self.ui.listWidget_5.currentIndex()
            #     index = ite.row()
            #     original = Main.hof_class.termini[index]
            #     new_item = type(original)(**original.__dict__)  # Create a new instance with the same attributes
            #     Main.hof_class.termini.insert(index, new_item)
            #     self.ui.listWidget_5.insertItem(index, new_item.eric)
            # elif stuff == 4:
            #     ite = self.ui.listWidget_2.currentIndex()
            #     index = ite.row()
            #     original = Main.hof_class.infosystem[index]
            #     new_item = type(original)(**original.__dict__)  # Create a new instance with the same attributes
            #     Main.hof_class.infosystem.insert(index, new_item)
            #     self.ui.listWidget_2.insertItem(index, new_item.route)


        def generate_8w_6w_LCD(self):
            if not build_with_genLED:
                QMessageBox.warning(self, "Error", "This version of the program does not have the LED generator.", QMessageBox.Ok) #type: ignore
            else:
                Main.raise_unimplemented()

        def reopen_hof(self):
            Main.hof_class = HOF_KMBHan()
            file = QFileDialog.getOpenFileName(self, 'Open HOF', 'C:\\', 'HOF Files (*.hof)')
            if file[0]:
                Main.hof_class.load_from_hof(file[0])
                Main.opened_windows.append(Main.HOFView())
                Main.opened_windows[-1].show()
                Main.hofname = file[0].split("/")[-1].removesuffix(".hof")

                self.close()
        
        def open_db(self):
            Main.hof_class = HOF_KMBHan()
            file = QFileDialog.getOpenFileName(self, 'Open Database', 'C:\\', 'Database Files (*.db)')
            if file[0]:

                Main.hof_class.load_from_db(file[0])
                Main.opened_windows.append(Main.HOFView())
                Main.opened_windows[-1].show()
                Main.hofname = file[0].split("/")[-1].removesuffix(".db")
                Main.export_path = file[0].removesuffix(Main.hofname + ".db")


                self.close()
            
            

        def open_pref(self):
            Main.opened_windows.append(Main.PrefWin())
            Main.opened_windows[-1].show()

        
        @Slot(None,bool) #type: ignore  
        def update_listviews_every_3_minutes(self, TF:bool = False) -> None:
            # self.shortcuta = QShortcut(QKeySequence("Ctrl+S"), self)
        
            # If TF is True, stop timer
            if TF and hasattr(self, '_updateTimer'):
                self._updateTimer.stop()
                return
            
            # Initialize timer if doesn't exist
            if not hasattr(self, '_updateTimer'):
                self._updateTimer = QTimer(self)
                self._updateTimer.timeout.connect(self._perform_listviews_update)
            
            # Start or restart timer for 3 minutes
            self._updateTimer.start(180000)  # 3 * 60 * 1000 ms
            self._perform_listviews_update()
        
        def _perform_listviews_update(self):
            lw3_curindex = self.ui.listWidget_3.currentIndex()
            lw4_curindex = self.ui.listWidget_4.currentIndex()
            lw5_curindex = self.ui.listWidget_5.currentIndex()
        
            self.ui.listWidget_3.clear()
            self.ui.listWidget_4.clear()
            self.ui.listWidget_5.clear()
            self.ui.listWidget_3.addItems([i.name for i in Main.hof_class.stopreporter])
            self.ui.listWidget_4.addItems([i.RTNO for i in Main.hof_class.ddu])
            self.ui.listWidget_5.addItems([i.destination for i in Main.hof_class.termini])
            self.ui.listWidget_3.setCurrentIndex(lw3_curindex)
            self.ui.listWidget_4.setCurrentIndex(lw4_curindex)
            self.ui.listWidget_5.setCurrentIndex(lw5_curindex)
        
        # def closeEvent(self, event):

        
        # ...existing code...





        def delete_stuff(self,stuff:int):
            dct = {
                1: (Main.hof_class.stopreporter, self.ui.listWidget_3),
                2: (Main.hof_class.ddu, self.ui.listWidget_4),
                3: (Main.hof_class.termini, self.ui.listWidget_5),
                4: (Main.hof_class.infosystem, self.ui.listWidget_2)
            }
            if stuff == 1:
                ite = self.ui.listWidget_3.currentIndex()
                index = ite.row()
                Main.hof_class.stopreporter.pop(index)
                self.ui.listWidget_3.takeItem(index)
            elif stuff == 2:
                ite = self.ui.listWidget_4.currentIndex()
                index = ite.row()
                Main.hof_class.ddu.pop(index)
                self.ui.listWidget_4.takeItem(index)
            elif stuff == 3:
                ite = self.ui.listWidget_5.currentIndex()
                index = ite.row()
                Main.hof_class.termini.pop(index)
                self.ui.listWidget_5.takeItem(index)
            elif stuff == 4:
                ite = self.ui.listWidget_2.currentIndex()
                index = ite.row()
                Main.hof_class.infosystem.pop(index)
                self.ui.listWidget_2.takeItem(index)

        def sort_stuff(self,stuff:int) -> None:
            dct = {
                1: (Main.hof_class.stopreporter, self.ui.listWidget_3),
                2: (Main.hof_class.ddu, self.ui.listWidget_4),
                3: (Main.hof_class.termini, self.ui.listWidget_5),
                4: (Main.hof_class.infosystem, self.ui.listWidget_2)
            }
            if stuff == 1:
                Main.hof_class.stopreporter = sorted(Main.hof_class.stopreporter, key=lambda x: x.name)
                self.ui.listWidget_3.clear()
                self.ui.listWidget_3.addItems([i.name for i in Main.hof_class.stopreporter])
            elif stuff == 2:
                Main.hof_class.ddu = sorted(Main.hof_class.ddu, key=lambda x: x.RTNO)
                self.ui.listWidget_4.clear()
                self.ui.listWidget_4.addItems([i.RTNO for i in Main.hof_class.ddu])
            elif stuff == 3:
                Main.hof_class.termini = sorted(Main.hof_class.termini, key=lambda x: x.eric)
                self.ui.listWidget_5.clear()
                self.ui.listWidget_5.addItems([i.destination for i in Main.hof_class.termini])
            elif stuff == 4:
                Main.hof_class.infosystem = sorted(Main.hof_class.infosystem, key=lambda x: x.route)
                self.ui.listWidget_2.clear()
                self.ui.listWidget_2.addItems([i.route for i in Main.hof_class.infosystem])


        @Slot(None, int,int) #type: ignore
        def update_listviews(self,index:int,func_in:int) -> int:
            dct = {
                1: lambda: self.ui.listWidget_3.item(index).setText(Main.hof_class.stopreporter[index].name), # Stopreporter
                2: lambda: self.ui.listWidget_4.item(index).setText(Main.hof_class.ddu[index].RTNO), # DDU
                3: lambda: self.ui.listWidget_5.item(index).setText(Main.hof_class.termini[index].destination), # Termini
                4: lambda: self.ui.listWidget_2.item(index).setText(Main.hof_class.infosystem[index].route) # Infosystem
            }
            
            # Execute the functions
            dct[func_in]()
            return 1
        
        def check_bsl_validity(self):
            miss_bs = []
            bsl = [i.name for i in Main.hof_class.stopreporter]
            rt_sel = self.ui.listWidget_2.currentIndex()
            rt_index = rt_sel.row()
            if Main.hof_class.infosystem[rt_index].busstop_list1_class._busstops == []:
                QMessageBox.warning(self, "Error", "Bus stop list 1 is empty.", QMessageBox.Ok) #type: ignore
            elif Main.hof_class.infosystem[rt_index].busstop_list2_class._busstops == []:
                QMessageBox.warning(self, "Error", "Bus stop list 2 is empty.", QMessageBox.Ok) #type: ignore
            else:
                for i in Main.hof_class.infosystem[rt_index].busstop_list1_class._busstops:
                    if i not in bsl:
                        miss_bs.append(i)
                for i in Main.hof_class.infosystem[rt_index].busstop_list2_class._busstops:
                    if i not in bsl:
                        miss_bs.append(i)
                if miss_bs != []:
                    QMessageBox.warning(self, "Error", f"Bus stops {miss_bs} are not found in the bus stop list.", QMessageBox.Ok) #type: ignore
                else:
                    QMessageBox.information(self, "Success", "Bus stop list is valid.", QMessageBox.Ok) #type: ignore

        def check_all_bsl_validity(self):
            miss_bs = set()
            bsl = [i.name for i in Main.hof_class.stopreporter]
            for rt in Main.hof_class.infosystem:
                for i in rt.busstop_list1_class._busstops:
                    if i not in bsl:
                        miss_bs.add(i)
                for i in rt.busstop_list2_class._busstops:
                    if i not in bsl:
                        miss_bs.add(i)
            if miss_bs != set():
                # message = QMessageBox()
                # message.setMinimumSize(200, 100)
                # message.setWindowTitle("Error")
                # message.setText(f"Bus stops {miss_bs if len(miss_bs)< 20 else list(miss_bs)[:20]} are not found in the bus stop list. Do you want to add them?")
                # message.setIcon(QMessageBox.Warning) # type: ignore
                # message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) # type: ignore
                # message.accepted.connect(lambda: self.add_bs_from_list(list(miss_bs)))
                QMessageBox.warning(self, "Error", f"Bus stops {miss_bs if len(miss_bs)< 20 else list(miss_bs)[:20]} are not found in the bus stop list. Do you want to add them?", QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel) #type: ignore
                if QMessageBox.buttonClicked == QMessageBox.StandardButton.Ok:
                    self.add_bs_from_list(list(miss_bs))
            else:
                QMessageBox.information(self, "Success", "All bus stop lists are valid.", QMessageBox.Ok) #type: ignore
        
        def add_bs_from_list(self,bs:list[str]) -> None:
            for i in bs:
                Main.hof_class.add_stopreporter(f"{i}", "New Stop", 0, 0, -1.0, -1.0)
                self.ui.listWidget_3.addItem(f"{i}")


        def del_bs_from_sel(self):
            item = self.ui.listWidget.currentIndex()
            index = item.row()
            routesel = self.ui.listWidget_2.currentIndex()
            routeindex = routesel.row()
            # current_dir = self.bus_rt_direction
            if self.bus_rt_direction == 1:
                Main.hof_class.infosystem[routeindex].busstop_list1_class._busstops.pop(index)
            else:
                Main.hof_class.infosystem[routeindex].busstop_list2_class._busstops.pop(index)
            self.ui.listWidget.takeItem(index)
            
        def add_bs_from_sel(self):
            item = self.ui.listWidget_3.currentIndex()
            index = item.row()
            routesel = self.ui.listWidget_2.currentIndex()
            routeindex = routesel.row()
            # current_dir = self.bus_rt_direction
            if self.ui.checkBox.isChecked():
                if self.bus_rt_direction == 1:
                    Main.hof_class.infosystem[routeindex].busstop_list1_class._busstops.append(Main.hof_class.stopreporter[index].name)
                    self.ui.listWidget.addItem(Main.hof_class.stopreporter[index].name)
                else:
                    Main.hof_class.infosystem[routeindex].busstop_list2_class._busstops.append(Main.hof_class.stopreporter[index].name)
                    self.ui.listWidget.addItem(Main.hof_class.stopreporter[index].name)
            else:
                cur_bs = self.ui.listWidget.currentIndex()
                cur_index = cur_bs.row()

                if self.bus_rt_direction == 1:
                    Main.hof_class.infosystem[routeindex].busstop_list1_class._busstops.insert(cur_index, Main.hof_class.stopreporter[index].name)
                    self.ui.listWidget.insertItem(cur_index, Main.hof_class.stopreporter[index].name)
                else:
                    Main.hof_class.infosystem[routeindex].busstop_list2_class._busstops.insert(cur_index, Main.hof_class.stopreporter[index].name)
                    self.ui.listWidget.insertItem(cur_index, Main.hof_class.stopreporter[index].name)

        def bsl_goup(self):
            item = self.ui.listWidget.currentIndex()
            index = item.row()
            print(item.data(), index)
            if index > 0:
                # self.ui.listWidget.item(index-1).setText(item.data())
                temp = self.ui.listWidget.item(index-1).text()
                cur = self.ui.listWidget.item(index).text()
                self.ui.listWidget.item(index-1).setText(cur)
                self.ui.listWidget.item(index).setText(temp)
                if self.bus_rt_direction == 1:
                    temp = Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list1_class._busstops[index-1]
                    cur = Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list1_class._busstops[index]
                    Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list1_class._busstops[index-1] = cur
                    Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list1_class._busstops[index] = temp
                else:
                    temp = Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list2_class._busstops[index-1]
                    cur = Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list2_class._busstops[index]
                    Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list2_class._busstops[index-1] = cur
                    Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list2_class._busstops[index] = temp
                self.ui.listWidget.setCurrentRow(index - 1)

                # self.ui.listWidget.setCurrentRow(index - 1)
                # self.ui.listWidget.takeItem(index)
                # self.ui.listWidget.insertItem(index - 1, item.data())
        def bsl_godown(self):
            item = self.ui.listWidget.currentIndex()
            index = item.row()
            
            if index < self.ui.listWidget.count() - 1:
                temp = self.ui.listWidget.item(index+1).text()
                cur = self.ui.listWidget.item(index).text()
                self.ui.listWidget.item(index+1).setText(cur)
                self.ui.listWidget.item(index).setText(temp)
                if self.bus_rt_direction == 1:
                    temp = Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list1_class._busstops[index+1]
                    cur = Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list1_class._busstops[index]
                    Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list1_class._busstops[index+1] = cur
                    Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list1_class._busstops[index] = temp
                else:
                    temp = Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list2_class._busstops[index+1]
                    cur = Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list2_class._busstops[index]
                    Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list2_class._busstops[index+1] = cur
                    Main.hof_class.infosystem[self.ui.listWidget_2.currentIndex().row()].busstop_list2_class._busstops[index] = temp
                self.ui.listWidget.setCurrentRow(index + 1)


        def change_bs_FromSel(self):
            item = self.ui.listWidget.currentIndex()
            index = item.row()
            routesel = self.ui.listWidget_2.currentIndex()
            routeindex = routesel.row()
            # current_dir = self.bus_rt_direction
            cur_bs = self.ui.listWidget_3.currentIndex()
            cur_index = cur_bs.row()
            if self.bus_rt_direction == 1:
                Main.hof_class.infosystem[routeindex].busstop_list1_class._busstops[index] = Main.hof_class.stopreporter[cur_index].name
            else:
                Main.hof_class.infosystem[routeindex].busstop_list2_class._busstops[index] = Main.hof_class.stopreporter[cur_index].name
            self.ui.listWidget.item(index).setText(Main.hof_class.stopreporter[cur_index].name)
            # if current_dir == 1:
            #     Main.hof_class.infosystem[routeindex].busstop_list1_class._busstops[index] = Main.hof_class.stopreporter[index].name
            # else:
            #     Main.hof_class.infosystem[routeindex].busstop_list2_class._busstops[index] = Main.hof_class.stopreporter[index].name
            # self.ui.listWidget.item(index).setText(Main.hof_class.stopreporter[index].name)
        def open_rt(self):
            item = self.ui.listWidget_2.currentIndex()
            index = item.row()
            Main.opened_windows.append(Main.AddRouteEntry(None,False,Main.hof_class.infosystem[index].route, 
                                                          Main.hof_class.infosystem[index].direction1,
                                                          Main.hof_class.infosystem[index].direction2,curindex=index))
            Main.opened_windows[-1].show()
        def open_bs(self):
            def search_bs(name: str, threads: int):
                ls = Main.hof_class.stopreporter
                slices = list(split(ls, threads))
                with multiprocessing.Pool(threads) as pool:
                    results = pool.starmap(search_in_slice, [(slice, name) for slice in slices])

                for slice_index, result in enumerate(results):
                    if result[0] is not None:
                        stop, index_in_slice = result
                        offset = sum(len(slices[i]) for i in range(slice_index))
                        actual_index = offset + index_in_slice
                        return stop, actual_index
                return None, -1

            item = self.ui.listWidget.currentItem()
            index = item.text()
            stop, actual_index = search_bs(index, multiprocessing.cpu_count())
            if stop is not None:
                Main.opened_windows.append(Main.AddBusStop(None,stop.name, 
                                                           stop.EngDisplay,
                                                           stop.ChiSeconds,
                                                           stop.EngSeconds,
                                                           stop.Outbound_sectionfare if isinstance(stop.Outbound_sectionfare,float) else -1.0,
                                                           stop.Inbound_sectionfare if isinstance(stop.Inbound_sectionfare,float) else -1.0,
                                                           curindex=actual_index))
                Main.opened_windows[-1].show()
            else:
                QMessageBox.warning(self, "Error", f"Bus stop {index} not found.", QMessageBox.Ok) #type: ignore

        def open_bs_lw3(self):
            item = self.ui.listWidget_3.currentIndex()
            index = item.row()
            Main.opened_windows.append(
                Main.AddBusStop(None,Main.hof_class.stopreporter[index].name, 
                                Main.hof_class.stopreporter[index].EngDisplay,
                                Main.hof_class.stopreporter[index].ChiSeconds,
                                Main.hof_class.stopreporter[index].EngSeconds,
                                Main.hof_class.stopreporter[index].Outbound_sectionfare if isinstance(Main.hof_class.stopreporter[index].Outbound_sectionfare,float) else -1.0, #type: ignore
                                Main.hof_class.stopreporter[index].Inbound_sectionfare if isinstance(Main.hof_class.stopreporter[index].Inbound_sectionfare,float) else -1.0, #type: ignore
                                curindex=index)) #type: ignore
            Main.opened_windows[-1].show()


        def open_ddu(self):
            item = self.ui.listWidget_4.currentIndex()
            index = item.row()
            Main.opened_windows.append(Main.AddDDU(None,Main.hof_class.ddu[index].RTNO, 
                                                   Main.hof_class.ddu[index].Outbound_dir,
                                                   Main.hof_class.ddu[index].Inbound_dir,
                                                   Main.hof_class.ddu[index].Outbound_price if isinstance(Main.hof_class.ddu[index].Outbound_price,float) else -1.0, #type: ignore
                                                   Main.hof_class.ddu[index].Inbound_price if isinstance(Main.hof_class.ddu[index].Inbound_price,float) else -1.0, #type: ignore
                                                   Main.hof_class.ddu[index].sectiontimes_Y,
                                                   Main.hof_class.ddu[index].sectiontimes_Z,curindex=index)) #type: ignore
            Main.opened_windows[-1].show()

        def open_termini(self):
            item = self.ui.listWidget_5.currentIndex()
            index = item.row()
            Main.opened_windows.append(Main.AddTermini(None,Main.hof_class.termini[index].eric, 
                                                       Main.hof_class.termini[index].destination,
                                                       Main.hof_class.termini[index].busfull,
                                                       Main.hof_class.termini[index].flip,curindex=index))
            Main.opened_windows[-1].show()
        def dirchange_Y(self):
            self.bus_rt_direction = 1
            # print(self.bus_rt_direction)
            self.get_bsl()
        def dirchange_Z(self):
            self.bus_rt_direction = 2
            # print(self.bus_rt_direction)
            self.get_bsl()
        def get_bsl(self):
            # print("hi")
            item =  self.ui.listWidget_2.currentIndex()
            index = item.row()
            self.ui.listWidget.clear()
            # for i in (Main.hof_class.infosystem[index].db_export_bsl1 if Main.HOFView.bus_rt_direction == 1 else Main.hof_class.infosystem[index].db_export_bsl2):
            #     self.ui.listWidget.addItem(i)
            # print(Main.hof_class.infosystem[index].busstop_list1 if Main.bus_rt_direction == 1 else Main.hof_class.infosystem[index].busstop_list2_class.db_export)
            self.ui.listWidget.addItems(Main.hof_class.infosystem[index].db_export_bsl1 if self.bus_rt_direction == 1 else Main.hof_class.infosystem[index].db_export_bsl2) 
        def change_rt_info(self):
            self.bus_rt_direction = 1
            item =  self.ui.listWidget_2.currentIndex()
            index = item.row()
            # self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(Main.hof_class.infosystem[index].route))
            # self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(Main.hof_class.infosystem[index].direction1))
            # self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(Main.hof_class.infosystem[index].direction2))
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
            c.execute("delete from prefs where key = 'export_path'")
            c.execute("insert into prefs values ('export_path', ?)", (Main.export_path,))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Saved", "Saved to " + Main.export_path + "/" + Main.hofname + ".db")
        
        def export_hof(self):
            if Main.hofname == "":
                Main.hof_class.name = "Untitled"
            if Main.export_path == "":
                Main.export_path = Main().fileexplorer()
            Main.hof_class.name = Main.hofname
            Main.hof_class.export_hof(Main.export_path + "/" + Main.hofname + ".hof")
            QMessageBox.information(self, "Saved", "Saved to " + Main.export_path + "/" + Main.hofname + ".hof")
        def closeEvent(self, event: QCloseEvent) -> None:
            Main.opened_windows = []
            if hasattr(self, '_updateTimer'):
                self._updateTimer.stop()
            event.accept()
            self.closed = True
            event.accept()

    

    class AddBusStop(QMainWindow):
        sig = Signal(int,int)
        orig_autoskip = True
        def __init__(self, parent=None,name:str = "",engdisp:str="",chisec:int=0,engsec:int=0,osf:float=-1.0,isf:float=-1.0,curindex:int=0):
            super().__init__(parent)
            self.curindex = curindex
            self.ui = AddBusStop_UI()
            self.ui.setupUi(self)
            self.ui.lineEdit.setText(name)
            self.ui.lineEdit_2.setText(engdisp)
            self.ui.spinBox.setValue(chisec)
            self.ui.spinBox_2.setValue(engsec)
            self.ui.doubleSpinBox.setValue(osf)
            self.ui.doubleSpinBox_2.setValue(isf)
            self.ui.checkBox.setChecked(True if name[0] == "_" else False)
            orig_autoskip = (True if name[0] == "_" else False)
            self.hofview = Main.opened_windows[0]
        def get_bs(self):
            Main.raise_unimplemented()
        def closeEvent(self,event):


            
            #             self._name = name
            # self._EngDisplay = EngDisplay
            # self._ChiSeconds = str(ChiSeconds).rjust(2,'0')
            # self._EngSeconds = str(EngSeconds).rjust(2,'0')
            # self._Outbound_sectionfare = f"${Outbound_sectionfare:.1f}" if isinstance(Outbound_sectionfare,float) and Outbound_sectionfare != -1.0 else name
            # self._Inbound_sectionfare = f"${Inbound_sectionfare:.1f}" if isinstance(Inbound_sectionfare,float) and Inbound_sectionfare != -1.0 else name

            # lst = [self.ui.plainTextEdit.document().isModified(), self.ui.plainTextEdit_2.document().isModified(), self.ui.spinBox.value() != 0, self.ui.spinBox_2.value() != 0, self.ui.doubleSpinBox.value() != 0.0, self.ui.doubleSpinBox_2.value() != 0.0]

            # if 
            Main.hof_class.stopreporter[self.curindex].name = self.ui.lineEdit.text()
            Main.hof_class.stopreporter[self.curindex].EngDisplay = self.ui.lineEdit_2.text()
            Main.hof_class.stopreporter[self.curindex].ChiSeconds = self.ui.spinBox.value()
            Main.hof_class.stopreporter[self.curindex].EngSeconds = self.ui.spinBox_2.value()
            Main.hof_class.stopreporter[self.curindex].Outbound_sectionfare = self.ui.doubleSpinBox.value()
            Main.hof_class.stopreporter[self.curindex].Inbound_sectionfare = self.ui.doubleSpinBox_2.value()
            Main.hof_class.stopreporter[self.curindex].comment = f"{self.ui.lineEdit_3.text()}|{self.ui.lineEdit_4.text()}"
            # if self.ui.checkBox.isChecked() and not self.orig_autoskip:
            #     Main.hof_class.add_stopreporter(f"_{self.ui.lineEdit.text()}", self.ui.lineEdit_2.text(), self.ui.spinBox.value(), self.ui.spinBox_2.value(), self.ui.doubleSpinBox.value(), self.ui.doubleSpinBox_2.value())
            #     Main.hof_class.stopreporter[-1].comment = f"{self.ui.lineEdit_3.text()}|{self.ui.lineEdit_4.text()}"
            self.sig.connect(self.hofview.update_listviews)
            self.sig.emit(self.curindex,1)
            # Main.HOFView().ui.listWidget_3.item(self.curindex).setText(self.ui.plainTextEdit.toPlainText())
            # item.setText(Main.hof_class.stopreporter[self.curindex].name)
            event.accept() # let the window close

    class AddDDU(QMainWindow):
        sig = Signal(int,int)
        def __init__(self, parent=None,RTNO:str="",OutDir:str="",InDir:str="",OutSecFare:float=-1.0,InSecFare:float=-1.0,Out_SectionCount:int=0,In_SectionCount:int=0,curindex:int=0):
            super().__init__(parent)
            self.curindex = curindex
            # self.sig = Signal(int)
            self.hofview = Main.opened_windows[0]
            self.ui = AddDDU_UI()
            self.ui.setupUi(self)
            self.ui.lineEdit.setText(RTNO)
            self.ui.lineEdit_2.setText(OutDir)
            self.ui.lineEdit_3.setText(InDir)
            self.ui.doubleSpinBox.setValue(OutSecFare)
            self.ui.doubleSpinBox_2.setValue(InSecFare)
            self.ui.spinBox.setValue(Out_SectionCount)
            self.ui.spinBox_2.setValue(In_SectionCount)
        
        def closeEvent(self,event):
            # lst = [self.ui.plainTextEdit.document().isModified(), self.ui.plainTextEdit_2.document().isModified(), self.ui.plainTextEdit_3.document().isModified(), self.ui.doubleSpinBox.value() != 0.0, self.ui.doubleSpinBox_2.value() != 0.0, self.ui.spinBox.value() != 0, self.ui.spinBox_2.value() != 0]
            # if Main.maybeSave(lst):

            Main.hof_class.ddu[self.curindex].RTNO = self.ui.lineEdit.text()
            Main.hof_class.ddu[self.curindex].Outbound_dir = self.ui.lineEdit_2.text()
            Main.hof_class.ddu[self.curindex].Inbound_dir = self.ui.lineEdit_3.text()
            Main.hof_class.ddu[self.curindex].Outbound_price = self.ui.doubleSpinBox.value()
            Main.hof_class.ddu[self.curindex].Inbound_price = self.ui.doubleSpinBox_2.value()
            Main.hof_class.ddu[self.curindex].sectiontimes_Y = self.ui.spinBox.value()
            Main.hof_class.ddu[self.curindex].sectiontimes_Z = self.ui.spinBox_2.value()
            
            self.sig.connect(self.hofview.update_listviews)
            self.sig.emit(self.curindex,2)
            event.accept()
            # else:
            #     event.ignore()
            # self.close()



    class AddRouteEntry(QMainWindow):
        sig = Signal(int,int)
        def __init__(self, parent=None,single_dual:bool=False,route:str="",Outbound_dir:str="",Inbound_dir:str="",curindex:int=0):
            super().__init__(parent)
            self.ui = AddRouteEntry_UI()
            self.ui.setupUi(self)
            self.curindex = curindex
            self.ui.lineEdit.setText(route)
            self.ui.lineEdit_2.setText(Outbound_dir)
            self.ui.lineEdit_3.setText(Inbound_dir)
            self.ui.checkBox.setChecked(single_dual)
        
        def closeEvent(self,event):
            Main.hof_class.infosystem[self.curindex].route = self.ui.lineEdit.text()
            Main.hof_class.infosystem[self.curindex].direction1 = self.ui.lineEdit_2.text()
            Main.hof_class.infosystem[self.curindex].direction2 = self.ui.lineEdit_3.text()
            self.sig.connect(Main.opened_windows[0].update_listviews)
            self.sig.emit(self.curindex,4)
            event.accept()


            

    class AddTermini(QMainWindow):
        sig = Signal(int,int)
        def __init__(self, parent=None,eric:str="", Destination:str="",busfull:str="",disps:list=[],curindex:int=0):
            super().__init__(parent)
            self.ui = AddTermini_UI()
            self.ui.setupUi(self)
            self.ui.lineEdit.setText(eric)
            self.ui.lineEdit_2.setText(Destination)
            self.ui.lineEdit_3.setText(busfull)
            self.curindex = curindex
            
            # self.ui.tableWidget.setItem
            for i in range(len(disps)):
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(disps[i]))

        def select_flip(self):
            files = QFileDialog.getOpenFileNames(self, 'Select Desti Display', 'C:\\', 'Destination Display Files (*.bmp)')
            self.ui.tableWidget.clear()
            for i in range(4,4-len(files),-1):
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(files[0][4-i]))

        def closeEvent(self,event):
            Main.hof_class.termini[self.curindex].eric = self.ui.lineEdit.text()
            Main.hof_class.termini[self.curindex].destination = self.ui.lineEdit_2.text()
            Main.hof_class.termini[self.curindex].busfull = self.ui.lineEdit_3.text()
            disps = []
            for i in range(4,0,-1):
                if self.ui.tableWidget.item(i,0) is not None:
                    disps.append(self.ui.tableWidget.item(i,0).text()) #type: ignore
            Main.hof_class.termini[self.curindex].flip = disps
            self.sig.connect(Main.opened_windows[0].update_listviews)
            self.sig.emit(self.curindex,3)
            event.accept()

        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main.Entrypoint()
    widget.show()
    sys.exit(app.exec())
