# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'l4gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(214, 269)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.runBtn = QtWidgets.QPushButton(self.centralwidget)
        self.runBtn.setGeometry(QtCore.QRect(70, 190, 75, 23))
        self.runBtn.setObjectName("runBtn")
        self.inputJson = QtWidgets.QLineEdit(self.centralwidget)
        self.inputJson.setGeometry(QtCore.QRect(10, 30, 171, 20))
        self.inputJson.setObjectName("inputJson")
        self.openFile = QtWidgets.QToolButton(self.centralwidget)
        self.openFile.setGeometry(QtCore.QRect(180, 30, 25, 19))
        self.openFile.setObjectName("openFile")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName("label")
        self.output1 = QtWidgets.QLineEdit(self.centralwidget)
        self.output1.setGeometry(QtCore.QRect(10, 90, 171, 20))
        self.output1.setObjectName("output1")
        self.save1 = QtWidgets.QToolButton(self.centralwidget)
        self.save1.setGeometry(QtCore.QRect(180, 90, 25, 19))
        self.save1.setObjectName("save1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 111, 16))
        self.label_2.setObjectName("label_2")
        self.output2 = QtWidgets.QLineEdit(self.centralwidget)
        self.output2.setGeometry(QtCore.QRect(10, 150, 171, 20))
        self.output2.setObjectName("output2")
        self.save2 = QtWidgets.QToolButton(self.centralwidget)
        self.save2.setGeometry(QtCore.QRect(180, 150, 25, 19))
        self.save2.setObjectName("save2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 111, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 214, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Waterbody Processing"))
        self.runBtn.setText(_translate("MainWindow", "Start"))
        self.openFile.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Input JSON"))
        self.save1.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Linear Output"))
        self.save2.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "Areal Output"))

