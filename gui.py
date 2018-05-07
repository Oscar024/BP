# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(788, 600)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);\n"
"font: 75 11pt \"Ubuntu\";"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(280, 40, 160, 29))
        self.horizontalSlider.setProperty("value", 13)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 50, 68, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("font: 75 11pt \"Ubuntu\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(470, 40, 64, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet(_fromUtf8("backgroud-color: rgb(255, 255, 255);\n"
""))
        self.lcdNumber.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setNumDigits(2)
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalSlider_2 = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(280, 90, 160, 29))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.lcdNumber_2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(470, 90, 64, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setStyleSheet(_fromUtf8("backgroud-color: rgb(255, 255, 255);\n"
""))
        self.lcdNumber_2.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setNumDigits(2)
        self.lcdNumber_2.setDigitCount(2)
        self.lcdNumber_2.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("intValue", 0)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 100, 68, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("font: 75 11pt \"Ubuntu\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalSlider_3 = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(280, 130, 160, 29))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.lcdNumber_3 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(470, 130, 64, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lcdNumber_3.setFont(font)
        self.lcdNumber_3.setStyleSheet(_fromUtf8("backgroud-color: rgb(255, 255, 255);\n"
""))
        self.lcdNumber_3.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber_3.setSmallDecimalPoint(False)
        self.lcdNumber_3.setNumDigits(2)
        self.lcdNumber_3.setDigitCount(2)
        self.lcdNumber_3.setProperty("value", 0.0)
        self.lcdNumber_3.setProperty("intValue", 0)
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 140, 68, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("font: 75 11pt \"Ubuntu\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txtResult = QtGui.QLineEdit(self.centralwidget)
        self.txtResult.setGeometry(QtCore.QRect(290, 240, 113, 27))
        self.txtResult.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255);"))
        self.txtResult.setObjectName(_fromUtf8("txtResult"))
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(300, 330, 99, 27))
        self.btnClear.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber.display)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber_2.display)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber_3.display)
        QtCore.QObject.connect(self.btnClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.debugear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def debugear(self):
        print("hola from debugear")
        print(self.txtResult.text())
        print("end fn")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Lecturas", None))
        self.label_2.setText(_translate("MainWindow", "Edad", None))
        self.label_3.setText(_translate("MainWindow", "Peso", None))
        self.btnClear.setText(_translate("MainWindow", "Clear", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

