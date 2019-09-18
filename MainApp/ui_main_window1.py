#!/usr/bin/python
# -*- coding: utf8 -*-
#!/bin/bash
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from login1 import *
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
import sys






class Ui_Form(QMainWindow):
    def login1(self):
        super(Ui_Form,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        
        
        
    def setupUi(self, Form):
        #self.statusBar()
        #menubar=self.menuBar()
        #Status = menubar.addMenu("Status")
        #Setting = menubar.addMenu("Setting")
        
        Form.setObjectName("Form")
        Form.resize(480, 360)
        


        
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setObjectName("image_label")
        self.image_label.setGeometry(QtCore.QRect(10, 10,218 ,250))
        #self.verticalLayout.addWidget(self.image_label)

        self.image_label1 = QtWidgets.QLabel(Form)
        self.image_label1.setObjectName("image_label1")
        self.image_label1.setGeometry(QtCore.QRect(300,10,480 ,120))
        
        #self.control_bt = QtWidgets.QPushButton(Form)
        #self.control_bt.setObjectName("control_bt")
        #self.control_bt.setGeometry(QtCore.QRect(250, 240, 75, 25))
        #self.verticalLayout.addWidget(self.control_bt)
        #self.horizontalLayout.addLayout(self.verticalLayout)

        #self.control_bt.clicked.connect(self.login1)

        
        #self.control_bt1 = QtWidgets.QPushButton(Form)
        #self.control_bt1.setObjectName("control_bt")
        #self.control_bt1.setGeometry(QtCore.QRect(250, 100, 75, 23))
        #self.verticalLayout.addWidget(self.control_bt1)
        #self.horizontalLayout.addLayout(self.verticalLayout)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 160, 111, 16))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(250, 180, 111, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 200, 111, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(250, 220, 111, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(350, 220, 130, 16))
        self.label_6.setObjectName("label_6")
        
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(350, 200, 130, 16))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(350, 180, 130, 16))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(350, 160, 130, 16))
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(10, 260, 111, 16))
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(60, 260, 111, 16))
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(250, 240, 230, 16))
        self.label_12.setObjectName("label_12")

        #self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        #self.plainTextEdit.setGeometry(QtCore.QRect(350, 220, 104, 31))
        #self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "HE THONG CHAM CONG"))
        #self.image_label.setText(_translate("Form", "HE THONG CHAM CONG"))
        #self.control_bt.setText(_translate("Form", "CAI DAT"))
        #self.control_bt1.setText(_translate("Form", "BAT DAU2"))
        self.label_2.setText(_translate("Form", "CÔNG TY:"))
        self.label_3.setText(_translate("Form", "TÊN:"))
        self.label_4.setText(_translate("Form", "ID:"))
        self.label_5.setText(_translate("Form", "THÔNG BÁO:"))
        #self.label_6.setText(_translate("Form", "1412103"))
        self.label_10.setText(_translate("Form", "WIFI"))
        self.label_11.setText(_translate("Form", "SERVER"))
