# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\GitHub\CompetitionResponderClient\MainWindow.ui'
#
# Created: Fri Oct 31 14:52:29 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

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

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(535, 414)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_title = QtGui.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(60, 10, 421, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setTextFormat(QtCore.Qt.AutoText)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setMargin(0)
        self.label_title.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 180, 351, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(40)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_bind = QtGui.QPushButton(self.centralwidget)
        self.pushButton_bind.setGeometry(QtCore.QRect(90, 120, 351, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(20)
        self.pushButton_bind.setFont(font)
        self.pushButton_bind.setObjectName(_fromUtf8("pushButton_bind"))
        self.lineEdit_Name = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Name.setGeometry(QtCore.QRect(150, 80, 291, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑 Light"))
        font.setPointSize(12)
        self.lineEdit_Name.setFont(font)
        self.lineEdit_Name.setObjectName(_fromUtf8("lineEdit_Name"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑 Light"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setMargin(0)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 350, 41, 16))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p>清华创客空间 万圣节游戏夜！</p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "抢答！！", None))
        self.pushButton_bind.setText(_translate("MainWindow", "先要绑定一下", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>队名</p></body></html>", None))
        self.label.setText(_translate("MainWindow", "By 毕滢", None))

