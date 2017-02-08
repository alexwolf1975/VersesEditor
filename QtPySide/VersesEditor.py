from configparser import ConfigParser

import sys
from PySide import QtCore, QtGui
from VersesEditorGUI import Ui_MainWindow
from VersesEditorAboutDialog import Ui_AboutDialog

expression = QtCore.QRegExp('[АаЕеЁёИиОоУуЫыЭэЮюЯя]')
config = ConfigParser()
ConfigFileName = 'VersesEditor.ini'

def VowelCount(s):
    count = 0
    index = expression.indexIn(s)
    while index >= 0:
        index = expression.pos()
        length = len(expression.cap())
        count += length
        index = expression.indexIn(s, index + length)
    return count

class VowelHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, document):
        QtGui.QSyntaxHighlighter.__init__(self, document)
        config.read(ConfigFileName)
        if 'color' in config['DEFAULT']:
            self.color = QtGui.QColor(int(config['DEFAULT']['color'], 16))
        else:
            self.color = QtGui.QColor(0, 160, 0)

    def highlightBlock(self, text):
        TextFormat = QtGui.QTextCharFormat()
        TextFormat.setForeground(self.color)
        index = expression.indexIn(text)
        while index >= 0:
            index = expression.pos()
            length = len(expression.cap())
            self.setFormat(index, length, TextFormat)
            index = expression.indexIn(text, index + length)

class AboutDialog(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)

class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        def About():
            dialog = AboutDialog(self)
            dialog.exec_()

        def Update(event = None):
            document = self.ui.text.document()
            if document.lineCount() != self.ui.text.lineCount:
                numbers = ''
                counts = ''
                for k in range(document.blockCount()):
                    numbers += '{}\n'.format(k+1)
                    block = document.findBlockByNumber(k)
                    text = block.text()
                    counts += '\n' if text == '' else '{}\n'.format(VowelCount(text))
                    for m in range(block.lineCount()-1):
                        numbers += '\n'
                        counts += '\n'
                self.ui.number.setText(numbers)
                self.ui.count.setText(counts)
                self.ui.text.lineCount = document.lineCount()

        def Color():
            color = QtGui.QColorDialog.getColor(self.ui.highlight.color, self)
            if color.isValid():
                self.ui.highlight.color = color
                config['DEFAULT']['color'] = '{:X}'.format(color.rgba())
                with open(ConfigFileName, 'w') as ConfigFile:
                    config.write(ConfigFile)
                self.ui.highlight.rehighlight()

        def Open():
            FileName = QtGui.QFileDialog.getOpenFileName(
                self, 'Открыть', '', '*.txt', '*.txt')[0]
            if FileName != '':
                with open(FileName, 'r') as VerseFile:
                    self.ui.text.setPlainText(VerseFile.read())

        def Save():
            FileName = QtGui.QFileDialog.getSaveFileName(
                self, 'Сохранить', 'стихи.txt', '*.txt', '*.txt')[0]
            if FileName != '':
                with open(FileName, 'w') as VerseFile:
                    VerseFile.write(self.ui.text.toPlainText())

        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.highlight = VowelHighlighter(self.ui.text.document())
        self.ui.text.textChanged.connect(Update)
        self.ui.text.lineCount = 0
        self.ui.Open.triggered.connect(Open)
        self.ui.Save.triggered.connect(Save)
        self.ui.Color.triggered.connect(Color)
        self.ui.About.triggered.connect(About)
        self.resizeEvent = Update
        Update()

app = QtGui.QApplication(sys.argv)
mySW = ControlMainWindow()
mySW.show()
sys.exit(app.exec_())
