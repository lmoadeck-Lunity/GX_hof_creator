# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HOFView.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(625, 778)
        MainWindow.setMinimumSize(QSize(625, 778))
        self.actionOpen_Project_Folder = QAction(MainWindow)
        self.actionOpen_Project_Folder.setObjectName(u"actionOpen_Project_Folder")
        self.actionOpen_HOF = QAction(MainWindow)
        self.actionOpen_HOF.setObjectName(u"actionOpen_HOF")
        self.actionOpen_TTL_for_Route = QAction(MainWindow)
        self.actionOpen_TTL_for_Route.setObjectName(u"actionOpen_TTL_for_Route")
        self.actionSave_to_DB = QAction(MainWindow)
        self.actionSave_to_DB.setObjectName(u"actionSave_to_DB")
        self.actionOpen_global_cfg = QAction(MainWindow)
        self.actionOpen_global_cfg.setObjectName(u"actionOpen_global_cfg")
        self.actionExport_HOF = QAction(MainWindow)
        self.actionExport_HOF.setObjectName(u"actionExport_HOF")
        self.actionGenerate_8w_6w_LCD = QAction(MainWindow)
        self.actionGenerate_8w_6w_LCD.setObjectName(u"actionGenerate_8w_6w_LCD")
        self.actionGenerate_DPIPv2 = QAction(MainWindow)
        self.actionGenerate_DPIPv2.setObjectName(u"actionGenerate_DPIPv2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(126, 69))
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 3, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(60, 23))
        self.pushButton_3.setMaximumSize(QSize(60, 23))

        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(14, 279))
        self.line.setMaximumSize(QSize(14, 279))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 0, 2, 4, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(125, 69))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 3, 3, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(60, 23))
        self.pushButton_7.setMaximumSize(QSize(60, 23))

        self.gridLayout.addWidget(self.pushButton_7, 0, 4, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(14, 279))
        self.line_2.setMaximumSize(QSize(14, 279))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 0, 5, 4, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(126, 69))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 6, 3, 1)

        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(60, 23))
        self.pushButton_14.setMaximumSize(QSize(60, 23))

        self.gridLayout.addWidget(self.pushButton_14, 0, 7, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(60, 23))
        self.pushButton_5.setMaximumSize(QSize(60, 23))

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(60, 23))
        self.pushButton_8.setMaximumSize(QSize(60, 23))

        self.gridLayout.addWidget(self.pushButton_8, 1, 4, 1, 1)

        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(60, 23))
        self.pushButton_15.setMaximumSize(QSize(60, 23))

        self.gridLayout.addWidget(self.pushButton_15, 1, 7, 1, 1)

        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(60, 23))
        self.pushButton_11.setMaximumSize(QSize(60, 23))

        self.gridLayout.addWidget(self.pushButton_11, 2, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(60, 23))
        self.pushButton_13.setMaximumSize(QSize(60, 23))

        self.gridLayout.addWidget(self.pushButton_13, 2, 4, 1, 1)

        self.pushButton_16 = QPushButton(self.centralwidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(60, 23))
        self.pushButton_16.setMaximumSize(QSize(60, 23))

        self.gridLayout.addWidget(self.pushButton_16, 2, 7, 1, 1)

        self.listWidget_3 = QListWidget(self.centralwidget)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setMinimumSize(QSize(186, 210))

        self.gridLayout.addWidget(self.listWidget_3, 3, 0, 1, 2)

        self.listWidget_4 = QListWidget(self.centralwidget)
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setMinimumSize(QSize(185, 210))

        self.gridLayout.addWidget(self.listWidget_4, 3, 3, 1, 2)

        self.listWidget_5 = QListWidget(self.centralwidget)
        self.listWidget_5.setObjectName(u"listWidget_5")
        self.listWidget_5.setMinimumSize(QSize(186, 210))

        self.gridLayout.addWidget(self.listWidget_5, 3, 6, 1, 2)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(581, 0))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 4, 0, 1, 8)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(63, 25))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 2, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(66, 23))
        self.pushButton_9.setMaximumSize(QSize(66, 23))

        self.gridLayout_3.addWidget(self.pushButton_9, 0, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(66, 23))
        self.pushButton_12.setMaximumSize(QSize(66, 32768))

        self.gridLayout_3.addWidget(self.pushButton_12, 0, 2, 2, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(92, 25))
        self.label_4.setMaximumSize(QSize(92, 25))
        self.label_4.setFont(font)

        self.gridLayout_3.addWidget(self.label_4, 0, 3, 2, 1)

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(66, 23))
        self.pushButton_10.setMaximumSize(QSize(66, 23))

        self.gridLayout_3.addWidget(self.pushButton_10, 1, 1, 1, 1)

        self.listWidget_2 = QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setMinimumSize(QSize(221, 231))

        self.gridLayout_3.addWidget(self.listWidget_2, 2, 0, 1, 3)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(211, 351))
        self.listWidget.setMaximumSize(QSize(16777215, 351))

        self.gridLayout_3.addWidget(self.listWidget, 2, 3, 2, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(80, 56))

        self.gridLayout_2.addWidget(self.pushButton_6, 2, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.centralwidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMaximumSize(QSize(80, 56))

        self.gridLayout_2.addWidget(self.pushButton_17, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(80, 56))

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 5, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(221, 111))
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.ContiguousSelection)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty(u"showSortIndicator", False)

        self.gridLayout_3.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(35, 30))
        self.pushButton.setMaximumSize(QSize(35, 30))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(35, 30))
        self.pushButton_2.setMaximumSize(QSize(35, 30))

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 5, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 625, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuMap = QMenu(self.menubar)
        self.menuMap.setObjectName(u"menuMap")
        self.menuLED = QMenu(self.menubar)
        self.menuLED.setObjectName(u"menuLED")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMap.menuAction())
        self.menubar.addAction(self.menuLED.menuAction())
        self.menuFile.addAction(self.actionOpen_Project_Folder)
        self.menuFile.addAction(self.actionOpen_HOF)
        self.menuFile.addAction(self.actionSave_to_DB)
        self.menuFile.addAction(self.actionExport_HOF)
        self.menuMap.addAction(self.actionOpen_TTL_for_Route)
        self.menuMap.addAction(self.actionOpen_global_cfg)
        self.menuLED.addAction(self.actionGenerate_8w_6w_LCD)
        self.menuLED.addAction(self.actionGenerate_DPIPv2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HOF View", None))
        self.actionOpen_Project_Folder.setText(QCoreApplication.translate("MainWindow", u"Open Project Folder", None))
        self.actionOpen_HOF.setText(QCoreApplication.translate("MainWindow", u"Open HOF", None))
        self.actionOpen_TTL_for_Route.setText(QCoreApplication.translate("MainWindow", u"Open TTL for Route", None))
        self.actionSave_to_DB.setText(QCoreApplication.translate("MainWindow", u"Save to DB", None))
        self.actionOpen_global_cfg.setText(QCoreApplication.translate("MainWindow", u"Open global.cfg", None))
        self.actionExport_HOF.setText(QCoreApplication.translate("MainWindow", u"Export HOF", None))
        self.actionGenerate_8w_6w_LCD.setText(QCoreApplication.translate("MainWindow", u"Generate 8w,6w", None))
        self.actionGenerate_DPIPv2.setText(QCoreApplication.translate("MainWindow", u"Generate DPIPv2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bus Stops", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"DDU", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Termini", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Duplicate", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Duplicate", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Duplicate", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Routes", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Duplicate", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bus Stops", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Remove\n"
"Selected\n"
"Bus Stop", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Duplicate\n"
"Without\n"
"Autoskip", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Add from\n"
"selected\n"
"Bus Stop", None))
        ___qtablewidgetitem = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Route Number", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Outbound Direction", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Inbound Direction", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuMap.setTitle(QCoreApplication.translate("MainWindow", u"Map", None))
        self.menuLED.setTitle(QCoreApplication.translate("MainWindow", u"LED", None))
    # retranslateUi

