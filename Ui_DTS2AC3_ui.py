# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DTS2AC3.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 300)
        MainWindow.setMinimumSize(QSize(500, 300))
        MainWindow.setMaximumSize(QSize(500, 300))
        icon = QIcon()
        icon.addFile(u"icons/icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"    background-color: rgb(25, 25, 25);\n"
"	text-align: center;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 100, 91, 16))
        self.label_2.setStyleSheet(u"font-weight: bold;\n"
"background-color: transparent;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 150, 101, 16))
        self.label_3.setStyleSheet(u"font-weight: bold;\n"
"background-color: transparent;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 210, 141, 31))
        font = QFont()
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QWidget{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 173, 0, 255), stop:1 rgba(255, 54, 0, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QWidget:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 227, 0, 255), stop:1 rgba(255, 54, 0, 255))\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color:rgb(255, 115, 0);\n"
"}")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 255, 441, 21))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	border: none;\n"
"    background-color: transparent;\n"
"    text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 129, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-radius: 7px;\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 120, 431, 20))
        self.lineEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(148, 148, 148);\n"
"border-radius: 3px;\n"
"")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 170, 431, 20))
        self.lineEdit_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(148, 148, 148);\n"
"border-radius: 3px;\n"
"")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 190, 151, 21))
        self.checkBox.setMouseTracking(True)
        self.checkBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.checkBox.setChecked(True)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(460, 120, 31, 21))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pushButton_2.setStyleSheet(u"QWidget{\n"
"background: rgb(56, 56, 56);\n"
"color: rgb(255, 255, 255);\n"
"text-align: top;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QWidget:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background: rgb(81, 81, 81)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(56, 56, 56);\n"
"}")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(460, 170, 31, 21))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QWidget{\n"
"background: rgb(56, 56, 56);\n"
"color: rgb(255, 255, 255);\n"
"text-align: top;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QWidget:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background: rgb(81, 81, 81)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(56, 56, 56);\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, -10, 141, 120))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(48)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(17, 17, 17);\n"
"background-color: transparent;")
        self.label.setScaledContents(False)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 25, 41, 61))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 67, 10);\n"
"background-color: transparent;")
        self.label_4.setScaledContents(False)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, -7, 151, 111))
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(50)
        font2.setBold(True)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(17, 17, 17);\n"
"background-color: transparent;")
        self.label_5.setScaledContents(False)
        self.converting = QLabel(self.centralwidget)
        self.converting.setObjectName(u"converting")
        self.converting.setGeometry(QRect(215, 280, 101, 16))
        self.converting.setStyleSheet(u"font-size: 12px;\n"
"font-weight: bold;\n"
"color: green;\n"
"background-color: transparent;")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(230, 20, 41, 61))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(255, 171, 3);\n"
"background-color: transparent;")
        self.label_7.setScaledContents(False)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, -10, 141, 101))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.label_8.setScaledContents(False)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(280, -10, 151, 101))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.label_6.setScaledContents(False)
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.converting.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_6.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DTS2AC3", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Input MKV file :</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Output directory :</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Save output directory", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"DTS", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"AC3", None))
        self.converting.setText(QCoreApplication.translate("MainWindow", u"converting...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"DTS", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"AC3", None))
    # retranslateUi

