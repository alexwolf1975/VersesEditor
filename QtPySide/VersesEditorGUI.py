# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/alexwolf/study/python/verseseditor.ui'
#
# Created: Sun Feb 19 13:47:51 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 792, 570))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.number = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.number.setFont(font)
        self.number.setText("")
        self.number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.number.setMargin(6)
        self.number.setObjectName("number")
        self.horizontalLayout.addWidget(self.number)
        self.text = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.text.setFont(font)
        self.text.setLineWidth(0)
        self.text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text.setPlainText("")
        self.text.setObjectName("text")
        self.horizontalLayout.addWidget(self.text)
        self.count = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.count.setFont(font)
        self.count.setText("")
        self.count.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.count.setMargin(6)
        self.count.setObjectName("count")
        self.horizontalLayout.addWidget(self.count)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.File = QtGui.QMenu(self.menubar)
        self.File.setObjectName("File")
        self.Options = QtGui.QMenu(self.menubar)
        self.Options.setObjectName("Options")
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.Open = QtGui.QAction(MainWindow)
        self.Open.setObjectName("Open")
        self.Save = QtGui.QAction(MainWindow)
        self.Save.setObjectName("Save")
        self.Color = QtGui.QAction(MainWindow)
        self.Color.setObjectName("Color")
        self.About = QtGui.QAction(MainWindow)
        self.About.setObjectName("About")
        self.File.addAction(self.Open)
        self.File.addAction(self.Save)
        self.Options.addAction(self.Color)
        self.menu.addAction(self.About)
        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Options.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "VersesEditor", None, QtGui.QApplication.UnicodeUTF8))
        self.File.setTitle(QtGui.QApplication.translate("MainWindow", "Файл", None, QtGui.QApplication.UnicodeUTF8))
        self.Options.setTitle(QtGui.QApplication.translate("MainWindow", "Настройки", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "Справка", None, QtGui.QApplication.UnicodeUTF8))
        self.Open.setText(QtGui.QApplication.translate("MainWindow", "Открыть", None, QtGui.QApplication.UnicodeUTF8))
        self.Save.setText(QtGui.QApplication.translate("MainWindow", "Сохранить", None, QtGui.QApplication.UnicodeUTF8))
        self.Color.setText(QtGui.QApplication.translate("MainWindow", "Цвет подсветки", None, QtGui.QApplication.UnicodeUTF8))
        self.About.setText(QtGui.QApplication.translate("MainWindow", "О программе", None, QtGui.QApplication.UnicodeUTF8))

