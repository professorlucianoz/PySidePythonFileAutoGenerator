# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainJfllpA.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(512, 151)
        MainWindow.setMinimumSize(QSize(512, 151))
        MainWindow.setMaximumSize(QSize(512, 151))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.011, stop:0 rgba(0, 0, 127, 255), stop:1 rgba(94, 122, 255, 255))\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-radius: 10px;\n"
"	min-height: 25px;\n"
"	padding-left: 20px;\n"
"	color: rgb(140, 140, 140)\n"
"}\n"
"\n"
"QLabel{\n"
"	color: white;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton#start_button{\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	min-height: 25px;\n"
"	background-color: white;\n"
"	font-weight: bold;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ui_label = QLabel(self.centralwidget)
        self.ui_label.setObjectName(u"ui_label")
        self.ui_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.ui_label, 0, 0, 1, 1)

        self.ui_edit = QLineEdit(self.centralwidget)
        self.ui_edit.setObjectName(u"ui_edit")

        self.gridLayout.addWidget(self.ui_edit, 1, 0, 1, 1)

        self.ui_open_button = QPushButton(self.centralwidget)
        self.ui_open_button.setObjectName(u"ui_open_button")
        icon = QIcon()
        icon.addFile(u"open-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui_open_button.setIcon(icon)

        self.gridLayout.addWidget(self.ui_open_button, 1, 1, 1, 1)

        self.python_label = QLabel(self.centralwidget)
        self.python_label.setObjectName(u"python_label")
        self.python_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.python_label, 2, 0, 1, 1)

        self.python_edit = QLineEdit(self.centralwidget)
        self.python_edit.setObjectName(u"python_edit")

        self.gridLayout.addWidget(self.python_edit, 3, 0, 1, 1)

        self.python_open_button = QPushButton(self.centralwidget)
        self.python_open_button.setObjectName(u"python_open_button")
        self.python_open_button.setIcon(icon)

        self.gridLayout.addWidget(self.python_open_button, 3, 1, 1, 1)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")

        self.gridLayout.addWidget(self.start_button, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ui_label.setText(QCoreApplication.translate("MainWindow", u"Ui Files location", None))
        self.ui_edit.setText("")
        self.ui_open_button.setText("")
        self.python_label.setText(QCoreApplication.translate("MainWindow", u"Python Files location", None))
        self.python_open_button.setText("")
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

