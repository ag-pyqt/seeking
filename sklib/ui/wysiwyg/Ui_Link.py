# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Link.ui'
#
# Created: Wed Feb 02 23:12:15 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Link(object):
    def setupUi(self, Link):
        Link.setObjectName("Link")
        Link.resize(400, 300)
        Link.setModal(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Link)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(1, 5, 1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab = QtGui.QTabWidget(Link)
        self.tab.setObjectName("tab")
        self.webtab = QtGui.QWidget()
        self.webtab.setObjectName("webtab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.webtab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.webtab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.url = QtGui.QLineEdit(self.webtab)
        self.url.setObjectName("url")
        self.gridLayout.addWidget(self.url, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.webtab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.urltext = QtGui.QLineEdit(self.webtab)
        self.urltext.setObjectName("urltext")
        self.gridLayout.addWidget(self.urltext, 1, 1, 1, 1)
        self.Style = QtGui.QLabel(self.webtab)
        self.Style.setObjectName("Style")
        self.gridLayout.addWidget(self.Style, 2, 0, 1, 1)
        self.urlstyle = QtGui.QLineEdit(self.webtab)
        self.urlstyle.setObjectName("urlstyle")
        self.gridLayout.addWidget(self.urlstyle, 2, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 72, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label_5 = QtGui.QLabel(self.webtab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.tab.addTab(self.webtab, "")
        self.innertab = QtGui.QWidget()
        self.innertab.setObjectName("innertab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.innertab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtGui.QLabel(self.innertab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.search = QtGui.QLineEdit(self.innertab)
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.listWidget = QtGui.QListWidget(self.innertab)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_4.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnpre = QtGui.QPushButton(self.innertab)
        self.btnpre.setEnabled(False)
        self.btnpre.setFlat(True)
        self.btnpre.setObjectName("btnpre")
        self.horizontalLayout_2.addWidget(self.btnpre)
        self.spinBox = QtGui.QSpinBox(self.innertab)
        self.spinBox.setEnabled(False)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.btnnext = QtGui.QPushButton(self.innertab)
        self.btnnext.setEnabled(False)
        self.btnnext.setFlat(True)
        self.btnnext.setObjectName("btnnext")
        self.horizontalLayout_2.addWidget(self.btnnext)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.tab.addTab(self.innertab, "")
        self.verticalLayout.addWidget(self.tab)
        self.btn = QtGui.QDialogButtonBox(Link)
        self.btn.setOrientation(QtCore.Qt.Horizontal)
        self.btn.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btn.setObjectName("btn")
        self.verticalLayout.addWidget(self.btn)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Link)
        self.tab.setCurrentIndex(0)
        QtCore.QObject.connect(self.btn, QtCore.SIGNAL("accepted()"), Link.accept)
        QtCore.QObject.connect(self.btn, QtCore.SIGNAL("rejected()"), Link.reject)
        QtCore.QMetaObject.connectSlotsByName(Link)

    def retranslateUi(self, Link):
        Link.setWindowTitle(QtGui.QApplication.translate("Link", "Link", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Link", "URL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Link", "Text", None, QtGui.QApplication.UnicodeUTF8))
        self.Style.setText(QtGui.QApplication.translate("Link", "Style", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Link", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Add a web type link</span><br />such as:<br />http://www.google.com<br />mailto:lycying@gmail.com</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tab.setTabText(self.tab.indexOf(self.webtab), QtGui.QApplication.translate("Link", "Web URL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Link", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.btnpre.setText(QtGui.QApplication.translate("Link", "<pre", None, QtGui.QApplication.UnicodeUTF8))
        self.btnnext.setText(QtGui.QApplication.translate("Link", ">next", None, QtGui.QApplication.UnicodeUTF8))
        self.tab.setTabText(self.tab.indexOf(self.innertab), QtGui.QApplication.translate("Link", "Inner Linker", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Link = QtGui.QDialog()
    ui = Ui_Link()
    ui.setupUi(Link)
    Link.show()
    sys.exit(app.exec_())
