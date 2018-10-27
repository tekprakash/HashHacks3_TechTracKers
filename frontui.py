import sys
from PyQt4 import QtCore,QtGui

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
        self.addLnOnly=True
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        self.go=True
        MainWindow.resize(500, 554)
        MainWindow.setMinimumSize(QtCore.QSize(490, 510))
        MainWindow.setMaximumSize(QtCore.QSize(500, 554))
        MainWindow.setStyleSheet(_fromUtf8("font: 8pt \"MS Shell Dlg 2\";"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 250, 81, 31))
        self.pushButton.setStyleSheet(_fromUtf8(" background-color: rgb(255, 255, 255);\n""border: 1px solid black;\n""color: rgb(0, 0, 0);\n""font: 75 12pt \"MS Shell Dlg 2\";\n""border-radius:5px;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        #self.pushButton.clicked.connect(self.space)
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 0, 411, 241))
        self.textBrowser.setStyleSheet(_fromUtf8("background-color:rgba(85, 255, 0,180);\n""color: rgba(0, 0, 0,190);\n""font: 22pt \"MS Sans Serif\";\n""border-radius:5px;"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 250, 81, 31))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n""border: 1px solid black;\n""color: rgb(0, 0, 0);\n""font: 75 12pt \"MS Shell Dlg 2\";\n""border-radius:5px;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        #self.pushButton_2.clicked.connect(self.delLet)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 250, 81, 31))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n""border: 1px solid black;\n""color: rgb(0, 0, 0);\n""font: 75 12pt \"MS Shell Dlg 2\";\n""border-radius:5px;"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        #self.pushButton_3.clicked.connect(self.pushSentenceToBody)
        self.textBrowser_2 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 350, 431, 51))
        self.textBrowser_2.setStyleSheet(_fromUtf8("background-color:rgba(85, 255, 0,180);\n""border-radius:10px;\n""font: 12pt \"MS Sans Serif\";\n""color: rgb(0, 0, 0);"))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 430, 351, 91))
        self.textBrowser_3.setStyleSheet(_fromUtf8("background-color:rgba(85, 255, 0,180);\n""color: rgb(0, 0, 0);\n""font: 75 12pt \"MS Shell Dlg 2\";\n""border-radius:5px;"))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        # self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        # self.pushButton_4.setGeometry(QtCore.QRect(370, 300, 81, 31))
        # self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n""border: 1px solid black;\n""color: rgb(0, 0, 0);\n""font: 75 12pt \"MS Shell Dlg 2\";\n""border-radius:5px;"))
        # self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        #self.pushButton_4.clicked.connect(self.smsButton)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 430, 81, 81))
        self.pushButton_5.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n""border: 1px solid black;\n""color: rgb(0, 0, 0);\n""font: 75 12pt \"MS Shell Dlg 2\";\n""border-radius:5px;"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        #self.pushButton_5.clicked.connect(self.getEmail)
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 250, 81, 31))
        self.pushButton_6.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n""border: 1px solid black;\n""color: rgb(0, 0, 0);\n""font: 75 12pt \"MS Shell Dlg 2\";\n""border-radius:5px;"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        #self.pushButton_6.clicked.connect(self.recite)
        self.textBrowser_4 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 300, 301, 31))
        self.textBrowser_4.setStyleSheet(_fromUtf8("background-color:rgba(85, 255, 0,180);\n""border-radius:10px;\n""color: rgb(0, 0, 0);\n""font: 12pt \"MS Sans Serif\";"))
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.buts = [[self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_6], [self.textBrowser_4], [self.pushButton_5]]

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Blink-2-Voice", None))
        self.pushButton.setText(_translate("MainWindow", "Space", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:22pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt;\">        A B C D E</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt;\">         F G H I J</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt;\">        K L M N O</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt;\">        P Q R S T</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt;\">      U V W X Y Z</span></p></body></html>", None))
        self.pushButton_2.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_3.setText(_translate("MainWindow", "Push", None))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        # self.pushButton_4.setText(_translate("MainWindow", "SMS", None))
        self.pushButton_5.setText(_translate("MainWindow", "E-MAIL", None))
        self.pushButton_6.setText(_translate("MainWindow", "Recite", None))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
