# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mwindow.ui'
#
# Created: Thu May  4 19:41:50 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(764, 554)
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_3.setMinimumSize(QtCore.QSize(145, 150))
        self.dockWidget_3.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget_3.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.data_listwidget = QtGui.QTreeWidget(self.dockWidgetContents)
        self.data_listwidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.data_listwidget.setObjectName("data_listwidget")
        self.data_listwidget.headerItem().setText(0, "1")
        self.horizontalLayout_8.addWidget(self.data_listwidget)
        self.dockWidget_3.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_3)
        self.dockWidget_4 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_4.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget_4.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_4.setObjectName("dockWidget_4")
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.dockWidgetContents_5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.eq_tab = QtGui.QTabWidget(self.dockWidgetContents_5)
        self.eq_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.eq_tab.setObjectName("eq_tab")
        self.shovel_tab = QtGui.QWidget()
        self.shovel_tab.setObjectName("shovel_tab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.shovel_tab)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.shovel_listwidget = QtGui.QListWidget(self.shovel_tab)
        self.shovel_listwidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.shovel_listwidget.setFrameShadow(QtGui.QFrame.Plain)
        self.shovel_listwidget.setObjectName("shovel_listwidget")
        self.horizontalLayout_2.addWidget(self.shovel_listwidget)
        self.eq_tab.addTab(self.shovel_tab, "")
        self.truck_tab = QtGui.QWidget()
        self.truck_tab.setObjectName("truck_tab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.truck_tab)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.truck_listwidget = QtGui.QListWidget(self.truck_tab)
        self.truck_listwidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.truck_listwidget.setObjectName("truck_listwidget")
        self.horizontalLayout.addWidget(self.truck_listwidget)
        self.eq_tab.addTab(self.truck_tab, "")
        self.horizontalLayout_13.addWidget(self.eq_tab)
        self.dockWidget_4.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_4)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_2 = QtGui.QFrame(self.dockWidgetContents_2)
        self.frame_2.setMaximumSize(QtCore.QSize(266, 220))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtGui.QGroupBox(self.frame_2)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.availability_checkbox = QtGui.QCheckBox(self.groupBox)
        self.availability_checkbox.setObjectName("availability_checkbox")
        self.verticalLayout_5.addWidget(self.availability_checkbox)
        self.utilization_checkbox = QtGui.QCheckBox(self.groupBox)
        self.utilization_checkbox.setObjectName("utilization_checkbox")
        self.verticalLayout_5.addWidget(self.utilization_checkbox)
        self.eff_checkbox = QtGui.QCheckBox(self.groupBox)
        self.eff_checkbox.setObjectName("eff_checkbox")
        self.verticalLayout_5.addWidget(self.eff_checkbox)
        self.oee_checkbox = QtGui.QCheckBox(self.groupBox)
        self.oee_checkbox.setChecked(True)
        self.oee_checkbox.setObjectName("oee_checkbox")
        self.verticalLayout_5.addWidget(self.oee_checkbox)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.dataframe_groupbox = QtGui.QGroupBox(self.frame_2)
        self.dataframe_groupbox.setFlat(False)
        self.dataframe_groupbox.setObjectName("dataframe_groupbox")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.dataframe_groupbox)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.shift_rb = QtGui.QRadioButton(self.dataframe_groupbox)
        self.shift_rb.setChecked(True)
        self.shift_rb.setObjectName("shift_rb")
        self.verticalLayout_8.addWidget(self.shift_rb)
        self.day_rb = QtGui.QRadioButton(self.dataframe_groupbox)
        self.day_rb.setObjectName("day_rb")
        self.verticalLayout_8.addWidget(self.day_rb)
        self.week_rb = QtGui.QRadioButton(self.dataframe_groupbox)
        self.week_rb.setObjectName("week_rb")
        self.verticalLayout_8.addWidget(self.week_rb)
        self.month_rb = QtGui.QRadioButton(self.dataframe_groupbox)
        self.month_rb.setObjectName("month_rb")
        self.verticalLayout_8.addWidget(self.month_rb)
        self.horizontalLayout_9.addLayout(self.verticalLayout_8)
        self.horizontalLayout_5.addWidget(self.dataframe_groupbox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(15, -1, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ma_spinBox = QtGui.QSpinBox(self.frame_2)
        self.ma_spinBox.setObjectName("ma_spinBox")
        self.horizontalLayout_7.addWidget(self.ma_spinBox)
        self.ma_checkbox = QtGui.QCheckBox(self.frame_2)
        self.ma_checkbox.setObjectName("ma_checkbox")
        self.horizontalLayout_7.addWidget(self.ma_checkbox)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_11.addWidget(self.frame_2)
        self.dockWidget.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_2.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget_2.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.calendarWidget = QtGui.QCalendarWidget(self.dockWidgetContents_3)
        self.calendarWidget.setMaximumSize(QtCore.QSize(266, 220))
        self.calendarWidget.setStyleSheet("")
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_12.addWidget(self.calendarWidget)
        self.dockWidget_2.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionNewEquipment = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/backup/flaticons/icons/png/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewEquipment.setIcon(icon)
        self.actionNewEquipment.setObjectName("actionNewEquipment")
        self.actionDelete = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../.designer/backup/flaticons/icons/png/cancel-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon1)
        self.actionDelete.setObjectName("actionDelete")
        self.actionAdd_Shift = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../.designer/backup/flaticons/icons/png/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Shift.setIcon(icon2)
        self.actionAdd_Shift.setObjectName("actionAdd_Shift")
        self.actionPlot = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../.designer/backup/flaticons/icons/png/next-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot.setIcon(icon3)
        self.actionPlot.setObjectName("actionPlot")
        self.actionExport = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../.designer/backup/flaticons/icons/png/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport.setIcon(icon4)
        self.actionExport.setObjectName("actionExport")
        self.toolBar.addAction(self.actionNewEquipment)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addAction(self.actionAdd_Shift)
        self.toolBar.addAction(self.actionExport)
        self.toolBar.addAction(self.actionPlot)

        self.retranslateUi(MainWindow)
        self.eq_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MineLog", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_3.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Equipment Data", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_4.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Equipment List", None, QtGui.QApplication.UnicodeUTF8))
        self.eq_tab.setTabText(self.eq_tab.indexOf(self.shovel_tab), QtGui.QApplication.translate("MainWindow", "Shovel", None, QtGui.QApplication.UnicodeUTF8))
        self.eq_tab.setTabText(self.eq_tab.indexOf(self.truck_tab), QtGui.QApplication.translate("MainWindow", "Truck", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Data Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.availability_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Availability", None, QtGui.QApplication.UnicodeUTF8))
        self.utilization_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Utilization", None, QtGui.QApplication.UnicodeUTF8))
        self.eff_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Efficiency", None, QtGui.QApplication.UnicodeUTF8))
        self.oee_checkbox.setText(QtGui.QApplication.translate("MainWindow", "OEE", None, QtGui.QApplication.UnicodeUTF8))
        self.dataframe_groupbox.setTitle(QtGui.QApplication.translate("MainWindow", "Data Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.shift_rb.setText(QtGui.QApplication.translate("MainWindow", "Per Shift", None, QtGui.QApplication.UnicodeUTF8))
        self.day_rb.setText(QtGui.QApplication.translate("MainWindow", "Per Day", None, QtGui.QApplication.UnicodeUTF8))
        self.week_rb.setText(QtGui.QApplication.translate("MainWindow", "Per Week", None, QtGui.QApplication.UnicodeUTF8))
        self.month_rb.setText(QtGui.QApplication.translate("MainWindow", "Per Month", None, QtGui.QApplication.UnicodeUTF8))
        self.ma_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Moving Average", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_2.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Calendar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewEquipment.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Shift.setText(QtGui.QApplication.translate("MainWindow", "Add Shift", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Shift.setToolTip(QtGui.QApplication.translate("MainWindow", "AddShift", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlot.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))

