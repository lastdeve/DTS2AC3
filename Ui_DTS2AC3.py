# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_DTS2AC3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        MainWindow.setMinimumSize(QtCore.QSize(500, 300))
        MainWindow.setMaximumSize(QtCore.QSize(500, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: rgb(25, 25, 25);\n"
"    text-align: center;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 100, 91, 16))
        self.label_2.setStyleSheet("font-weight: bold;\n"
"background-color: transparent;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 150, 101, 16))
        self.label_3.setStyleSheet("font-weight: bold;\n"
"background-color: transparent;")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 220, 141, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QWidget{\n"
"background: rgb(56, 56, 56);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QWidget:hover {\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgb(81, 81, 81)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(56, 56, 56);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 260, 441, 21))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: center;\n"
"    color: rgb(255, 255, 255);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(207, 22, 25);\n"
"    border-radius: 7px;\n"
"}")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 120, 431, 20))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(148, 148, 148);\n"
"border-radius: 3px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 170, 431, 20))
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(148, 148, 148);\n"
"border-radius: 3px;\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 190, 151, 21))
        self.checkBox.setMouseTracking(True)
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 120, 31, 21))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_2.setStyleSheet("QWidget{\n"
"background: rgb(56, 56, 56);\n"
"color: rgb(255, 255, 255);\n"
"text-align: top;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QWidget:hover {\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgb(81, 81, 81)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(56, 56, 56);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 170, 31, 21))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QWidget{\n"
"background: rgb(56, 56, 56);\n"
"color: rgb(255, 255, 255);\n"
"text-align: top;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QWidget:hover {\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgb(81, 81, 81)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(56, 56, 56);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, -10, 141, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 20, 41, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(207, 22, 25);\n"
"background-color: transparent;")
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, -10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(380, -10, 51, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.progressBar.raise_()
        self.checkBox.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DTS2AC3"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Input MKV file :</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Output directory :</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Convert"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.checkBox.setText(_translate("MainWindow", "Save output directory"))
        self.pushButton_2.setText(_translate("MainWindow", "..."))
        self.pushButton_3.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "DTS"))
        self.label_4.setText(_translate("MainWindow", "2"))
        self.label_5.setText(_translate("MainWindow", "AC"))
        self.label_6.setText(_translate("MainWindow", "3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
