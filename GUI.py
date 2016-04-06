# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Wed Apr 06 12:04:19 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(949, 660)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Table = QtGui.QTableWidget(self.centralwidget)
        self.Table.setMinimumSize(QtCore.QSize(671, 0))
        self.Table.setMaximumSize(QtCore.QSize(671, 16777215))
        self.Table.setObjectName(_fromUtf8("Table"))
        self.Table.setColumnCount(5)
        self.Table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.Table, 2, 0, 1, 1)
        self.EnterScore = QtGui.QPushButton(self.centralwidget)
        self.EnterScore.setObjectName(_fromUtf8("EnterScore"))
        self.gridLayout.addWidget(self.EnterScore, 5, 0, 1, 1)
        self.CreateNewPlayer = QtGui.QPushButton(self.centralwidget)
        self.CreateNewPlayer.setObjectName(_fromUtf8("CreateNewPlayer"))
        self.gridLayout.addWidget(self.CreateNewPlayer, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sammys BP", None))
        item = self.Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Player", None))
        item = self.Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ELO", None))
        item = self.Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sink per Game", None))
        item = self.Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Points per Sink", None))
        item = self.Table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Avg Opponent ELO", None))
        self.EnterScore.setText(_translate("MainWindow", "Enter Score", None))
        self.CreateNewPlayer.setText(_translate("MainWindow", "Create New Player", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

