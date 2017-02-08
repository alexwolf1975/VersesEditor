# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/alexwolf/study/python/aboutdialog.ui'
#
# Created: Fri Feb  3 23:34:33 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AboutDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(AboutDialog)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(AboutDialog)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(AboutDialog)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialog)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AboutDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AboutDialog", "Verses Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AboutDialog", "Текстовый редактор\n"
"с подсветкой гласных букв\n"
"и подсчётом слогов по каждой строке", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AboutDialog", "Автор: Патрашов Алексей Сергеевич", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AboutDialog", "Лицензия: GPL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AboutDialog", "<html><head/><body><p>Сайт программы: <a href=\"http://verses-editor.sourceforge.net\"><span style=\" text-decoration: underline; color:#0000ff;\">http://verses-editor.sourceforge.net</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AboutDialog", "<html><head/><body><p>e-mail: <a href=\"mailto:alex-wolf-75@users.sourceforge.net\"><span style=\" text-decoration: underline; color:#0000ff;\">alex-wolf-75@users.sourceforge.net</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

