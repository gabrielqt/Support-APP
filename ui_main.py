# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(431, 546)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-10, -20, 891, 601))
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"")
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy1)
        self.menu.setStyleSheet(u"background: #01323d")
        self.options = QFrame(self.menu)
        self.options.setObjectName(u"options")
        self.options.setGeometry(QRect(90, 230, 281, 191))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.options.sizePolicy().hasHeightForWidth())
        self.options.setSizePolicy(sizePolicy2)
        self.options.setStyleSheet(u"background-color: transparent;\n"
"border-radius: 0px solid;\n"
"")
        self.options.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.options)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_page_infopc = QPushButton(self.options)
        self.btn_page_infopc.setObjectName(u"btn_page_infopc")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_page_infopc.sizePolicy().hasHeightForWidth())
        self.btn_page_infopc.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setFamilies([u"Fixedsys"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.btn_page_infopc.setFont(font)
        self.btn_page_infopc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_infopc.setStyleSheet(u"QPushButton{\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"	background-color: rgb(0, 77, 93);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 37, 45);\n"
"color: white;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_page_infopc)

        self.btn_page_laps = QPushButton(self.options)
        self.btn_page_laps.setObjectName(u"btn_page_laps")
        sizePolicy3.setHeightForWidth(self.btn_page_laps.sizePolicy().hasHeightForWidth())
        self.btn_page_laps.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamilies([u"Fixedsys"])
        font1.setPointSize(15)
        font1.setBold(False)
        self.btn_page_laps.setFont(font1)
        self.btn_page_laps.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_laps.setStyleSheet(u"QPushButton{\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"	background-color: rgb(0, 77, 93);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 37, 45);\n"
"color: white;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_page_laps)

        self.btn_page_pingtest = QPushButton(self.options)
        self.btn_page_pingtest.setObjectName(u"btn_page_pingtest")
        sizePolicy3.setHeightForWidth(self.btn_page_pingtest.sizePolicy().hasHeightForWidth())
        self.btn_page_pingtest.setSizePolicy(sizePolicy3)
        self.btn_page_pingtest.setFont(font1)
        self.btn_page_pingtest.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_pingtest.setStyleSheet(u"QPushButton{\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"	background-color: rgb(0, 77, 93);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 37, 45);\n"
"color: white;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_page_pingtest)

        self.label_2 = QLabel(self.menu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 70, 334, 96))
        self.label_2.setStyleSheet(u"background-color:black")
        self.btnquit = QPushButton(self.menu)
        self.btnquit.setObjectName(u"btnquit")
        self.btnquit.setGeometry(QRect(210, 420, 41, 41))
        sizePolicy3.setHeightForWidth(self.btnquit.sizePolicy().hasHeightForWidth())
        self.btnquit.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setBold(False)
        self.btnquit.setFont(font2)
        self.btnquit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnquit.setStyleSheet(u"QPushButton{\n"
"border: 0px\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid white;\n"
"border-radius: 20px\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/images/desligar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnquit.setIcon(icon)
        self.btnquit.setIconSize(QSize(40, 35))
        self.stackedWidget.addWidget(self.menu)
        self.page_laps = QWidget()
        self.page_laps.setObjectName(u"page_laps")
        self.page_laps.setStyleSheet(u"background: #01323d")
        self.linepcname = QLineEdit(self.page_laps)
        self.linepcname.setObjectName(u"linepcname")
        self.linepcname.setGeometry(QRect(80, 220, 221, 31))
        self.linepcname.setStyleSheet(u"color: black;\n"
"background-color: aliceblue;\n"
"border-radius: 10px")
        self.label_3 = QLabel(self.page_laps)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 180, 221, 51))
        font3 = QFont()
        font3.setFamilies([u"Fixedsys"])
        font3.setPointSize(15)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color:white")
        self.label_5 = QLabel(self.page_laps)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 300, 351, 51))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color:white\n"
"")
        self.linepassword = QLineEdit(self.page_laps)
        self.linepassword.setObjectName(u"linepassword")
        self.linepassword.setGeometry(QRect(80, 340, 271, 31))
        self.linepassword.setStyleSheet(u"color: grey;\n"
"background-color: aliceblue;\n"
"border-radius: 10px\n"
"")
        self.label_4 = QLabel(self.page_laps)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 50, 49, 41))
        self.label_4.setStyleSheet(u"background-color:black")
        self.btn_backtomenu = QPushButton(self.page_laps)
        self.btn_backtomenu.setObjectName(u"btn_backtomenu")
        self.btn_backtomenu.setGeometry(QRect(190, 500, 75, 41))
        self.btn_backtomenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_backtomenu.setStyleSheet(u"QPushButton:hover{\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/casa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backtomenu.setIcon(icon1)
        self.btn_backtomenu.setIconSize(QSize(32, 32))
        self.submitbutton_laps = QPushButton(self.page_laps)
        self.submitbutton_laps.setObjectName(u"submitbutton_laps")
        self.submitbutton_laps.setGeometry(QRect(310, 220, 31, 31))
        self.submitbutton_laps.setCursor(QCursor(Qt.PointingHandCursor))
        self.submitbutton_laps.setStyleSheet(u"background-color: aliceblue;\n"
"border-radius: 10px")
        icon2 = QIcon()
        icon2.addFile(u"../Documents/SicoobSupportAPP-main/SicoobSupportAPP-main/images/aceitar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.submitbutton_laps.setIcon(icon2)
        self.submitbutton_laps.setIconSize(QSize(25, 25))
        self.stackedWidget.addWidget(self.page_laps)
        self.label_3.raise_()
        self.label_5.raise_()
        self.linepassword.raise_()
        self.label_4.raise_()
        self.btn_backtomenu.raise_()
        self.linepcname.raise_()
        self.submitbutton_laps.raise_()
        self.page_ping = QWidget()
        self.page_ping.setObjectName(u"page_ping")
        self.page_ping.setStyleSheet(u"background: #01323d;\n"
"color :white")
        self.label_16 = QLabel(self.page_ping)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 50, 49, 41))
        self.label_16.setStyleSheet(u"background-color:black")
        self.btn_backtomenu_3 = QPushButton(self.page_ping)
        self.btn_backtomenu_3.setObjectName(u"btn_backtomenu_3")
        self.btn_backtomenu_3.setGeometry(QRect(190, 500, 75, 41))
        self.btn_backtomenu_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_backtomenu_3.setStyleSheet(u"QPushButton:hover{\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"}")
        self.btn_backtomenu_3.setIcon(icon1)
        self.btn_backtomenu_3.setIconSize(QSize(32, 32))
        self.submitbutton_ping = QPushButton(self.page_ping)
        self.submitbutton_ping.setObjectName(u"submitbutton_ping")
        self.submitbutton_ping.setGeometry(QRect(350, 150, 31, 31))
        self.submitbutton_ping.setCursor(QCursor(Qt.PointingHandCursor))
        self.submitbutton_ping.setStyleSheet(u"background-color: aliceblue;\n"
"border-radius: 10px")
        self.submitbutton_ping.setIcon(icon2)
        self.submitbutton_ping.setIconSize(QSize(25, 25))
        self.label_17 = QLabel(self.page_ping)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(120, 20, 221, 51))
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"color:white")
        self.linepa = QLineEdit(self.page_ping)
        self.linepa.setObjectName(u"linepa")
        self.linepa.setGeometry(QRect(120, 70, 221, 31))
        self.linepa.setStyleSheet(u"color: black;\n"
"background-color: aliceblue;\n"
"border-radius: 10px")
        self.linepcname_ = QLineEdit(self.page_ping)
        self.linepcname_.setObjectName(u"linepcname_")
        self.linepcname_.setGeometry(QRect(120, 150, 221, 31))
        self.linepcname_.setStyleSheet(u"color: black;\n"
"background-color: aliceblue;\n"
"border-radius: 10px")
        self.label_18 = QLabel(self.page_ping)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(120, 120, 221, 21))
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"color:white")
        self.frame = QFrame(self.page_ping)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(160, 240, 131, 151))
        self.frame.setStyleSheet(u"border-radius: 0")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"color:white")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_19)

        self.label_39 = QLabel(self.frame)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font3)
        self.label_39.setStyleSheet(u"color:white")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_39)

        self.label_40 = QLabel(self.frame)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font3)
        self.label_40.setStyleSheet(u"color:white")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_40)

        self.label_43 = QLabel(self.frame)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font3)
        self.label_43.setStyleSheet(u"color:white")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_43)

        self.label_44 = QLabel(self.frame)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font3)
        self.label_44.setStyleSheet(u"color:white")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_44)

        self.firewallcheck = QLabel(self.frame)
        self.firewallcheck.setObjectName(u"firewallcheck")
        self.firewallcheck.setStyleSheet(u"background-color: aliceblue;\n"
"border-radius: 10px\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.firewallcheck)

        self.playcheck = QLabel(self.frame)
        self.playcheck.setObjectName(u"playcheck")
        self.playcheck.setStyleSheet(u"background-color: aliceblue;\n"
"border-radius: 10px\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.playcheck)

        self.ccscheck = QLabel(self.frame)
        self.ccscheck.setObjectName(u"ccscheck")
        self.ccscheck.setStyleSheet(u"background-color: aliceblue;\n"
"border-radius: 10px\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ccscheck)

        self.centralcheck = QLabel(self.frame)
        self.centralcheck.setObjectName(u"centralcheck")
        self.centralcheck.setStyleSheet(u"background-color: aliceblue;\n"
"border-radius: 10px\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.centralcheck)

        self.uadcheck = QLabel(self.frame)
        self.uadcheck.setObjectName(u"uadcheck")
        self.uadcheck.setStyleSheet(u"background-color: aliceblue;\n"
"border-radius: 10px\n"
"")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.uadcheck)

        self.stackedWidget.addWidget(self.page_ping)
        self.page_infopc = QWidget()
        self.page_infopc.setObjectName(u"page_infopc")
        self.page_infopc.setStyleSheet(u"background: #01323d;\n"
"color :white")
        self.btn_backtomenu_2 = QPushButton(self.page_infopc)
        self.btn_backtomenu_2.setObjectName(u"btn_backtomenu_2")
        self.btn_backtomenu_2.setGeometry(QRect(190, 520, 61, 41))
        self.btn_backtomenu_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_backtomenu_2.setStyleSheet(u"QPushButton:hover{\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"}")
        self.btn_backtomenu_2.setIcon(icon1)
        self.btn_backtomenu_2.setIconSize(QSize(32, 32))
        self.label_6 = QLabel(self.page_infopc)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 50, 49, 41))
        self.label_6.setStyleSheet(u"background-color:black")
        self.label_7 = QLabel(self.page_infopc)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(120, 30, 221, 51))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color:white")
        self.lineEdit_3 = QLineEdit(self.page_infopc)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(120, 70, 221, 31))
        self.lineEdit_3.setStyleSheet(u"color: black;\n"
"background-color: aliceblue;\n"
"border-radius: 10px")
        self.btn_cleaner = QPushButton(self.page_infopc)
        self.btn_cleaner.setObjectName(u"btn_cleaner")
        self.btn_cleaner.setGeometry(QRect(100, 360, 263, 31))
        sizePolicy3.setHeightForWidth(self.btn_cleaner.sizePolicy().hasHeightForWidth())
        self.btn_cleaner.setSizePolicy(sizePolicy3)
        self.btn_cleaner.setFont(font)
        self.btn_cleaner.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cleaner.setStyleSheet(u"QPushButton{\n"
"border: 2px solid;\n"
"border-radius: 10px;\n"
"	background-color: rgb(0, 77, 93);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 37, 45);\n"
"color: white;\n"
"}")
        self.btn_gpupdate = QPushButton(self.page_infopc)
        self.btn_gpupdate.setObjectName(u"btn_gpupdate")
        self.btn_gpupdate.setGeometry(QRect(100, 400, 263, 31))
        sizePolicy3.setHeightForWidth(self.btn_gpupdate.sizePolicy().hasHeightForWidth())
        self.btn_gpupdate.setSizePolicy(sizePolicy3)
        self.btn_gpupdate.setFont(font)
        self.btn_gpupdate.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gpupdate.setStyleSheet(u"QPushButton{\n"
"border: 2px solid;\n"
"border-radius: 10px;\n"
"	background-color: rgb(0, 77, 93);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 37, 45);\n"
"color: white;\n"
"}")
        self.btn_shutdownr = QPushButton(self.page_infopc)
        self.btn_shutdownr.setObjectName(u"btn_shutdownr")
        self.btn_shutdownr.setGeometry(QRect(100, 440, 263, 31))
        sizePolicy3.setHeightForWidth(self.btn_shutdownr.sizePolicy().hasHeightForWidth())
        self.btn_shutdownr.setSizePolicy(sizePolicy3)
        self.btn_shutdownr.setFont(font)
        self.btn_shutdownr.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_shutdownr.setStyleSheet(u"QPushButton{\n"
"border: 2px solid;\n"
"border-radius: 10px;\n"
"	background-color: rgb(0, 77, 93);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 37, 45);\n"
"color: white;\n"
"}")
        self.btn_shutdowns = QPushButton(self.page_infopc)
        self.btn_shutdowns.setObjectName(u"btn_shutdowns")
        self.btn_shutdowns.setGeometry(QRect(100, 480, 263, 31))
        sizePolicy3.setHeightForWidth(self.btn_shutdowns.sizePolicy().hasHeightForWidth())
        self.btn_shutdowns.setSizePolicy(sizePolicy3)
        self.btn_shutdowns.setFont(font)
        self.btn_shutdowns.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_shutdowns.setStyleSheet(u"QPushButton{\n"
"border: 2px solid;\n"
"border-radius: 10px;\n"
"	background-color: rgb(0, 77, 93);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 37, 45);\n"
"color: white;\n"
"}")
        self.submitbutton_info = QPushButton(self.page_infopc)
        self.submitbutton_info.setObjectName(u"submitbutton_info")
        self.submitbutton_info.setGeometry(QRect(350, 70, 31, 31))
        self.submitbutton_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.submitbutton_info.setStyleSheet(u"background-color: aliceblue;\n"
"border-radius: 10px")
        self.submitbutton_info.setIcon(icon2)
        self.submitbutton_info.setIconSize(QSize(25, 25))
        self.frame_2 = QFrame(self.page_infopc)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 130, 201, 211))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        font4 = QFont()
        font4.setFamilies([u"Cascadia Code SemiBold"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.label_8.setFont(font4)

        self.verticalLayout.addWidget(self.label_8)

        self.linemodelo = QLineEdit(self.frame_2)
        self.linemodelo.setObjectName(u"linemodelo")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setKerning(False)
        self.linemodelo.setFont(font5)
        self.linemodelo.setStyleSheet(u"background-color: snow;\n"
"color: black")

        self.verticalLayout.addWidget(self.linemodelo)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)

        self.verticalLayout.addWidget(self.label_10)

        self.linecpu = QLineEdit(self.frame_2)
        self.linecpu.setObjectName(u"linecpu")
        self.linecpu.setFont(font5)
        self.linecpu.setStyleSheet(u"background-color: snow;\n"
"color: black")

        self.verticalLayout.addWidget(self.linecpu)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)

        self.verticalLayout.addWidget(self.label_11)

        self.lineram = QLineEdit(self.frame_2)
        self.lineram.setObjectName(u"lineram")
        self.lineram.setFont(font5)
        self.lineram.setStyleSheet(u"background-color: snow;\n"
"color: black")

        self.verticalLayout.addWidget(self.lineram)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)

        self.verticalLayout.addWidget(self.label_12)

        self.linetotaldisk = QLineEdit(self.frame_2)
        self.linetotaldisk.setObjectName(u"linetotaldisk")
        self.linetotaldisk.setFont(font5)
        self.linetotaldisk.setStyleSheet(u"background-color: snow;\n"
"color: black")

        self.verticalLayout.addWidget(self.linetotaldisk)

        self.frame_3 = QFrame(self.page_infopc)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(220, 130, 201, 211))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.verticalLayout_4.addWidget(self.label_9)

        self.lineip = QLineEdit(self.frame_3)
        self.lineip.setObjectName(u"lineip")
        self.lineip.setFont(font5)
        self.lineip.setStyleSheet(u"background-color: snow;\n"
"color: black")

        self.verticalLayout_4.addWidget(self.lineip)

        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)

        self.verticalLayout_4.addWidget(self.label_13)

        self.linemac = QLineEdit(self.frame_3)
        self.linemac.setObjectName(u"linemac")
        self.linemac.setFont(font5)
        self.linemac.setStyleSheet(u"background-color: snow;\n"
"color: black")

        self.verticalLayout_4.addWidget(self.linemac)

        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)

        self.verticalLayout_4.addWidget(self.label_14)

        self.lineuser = QLineEdit(self.frame_3)
        self.lineuser.setObjectName(u"lineuser")
        self.lineuser.setFont(font5)
        self.lineuser.setStyleSheet(u"background-color: snow;\n"
"color: black")

        self.verticalLayout_4.addWidget(self.lineuser)

        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)

        self.verticalLayout_4.addWidget(self.label_15)

        self.linefreedisk = QLineEdit(self.frame_3)
        self.linefreedisk.setObjectName(u"linefreedisk")
        self.linefreedisk.setFont(font5)
        self.linefreedisk.setStyleSheet(u"background-color: snow;\n"
"color: black")

        self.verticalLayout_4.addWidget(self.linefreedisk)

        self.stackedWidget.addWidget(self.page_infopc)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_page_infopc.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.btn_page_laps.setText(QCoreApplication.translate("MainWindow", u"LAPS", None))
        self.btn_page_pingtest.setText(QCoreApplication.translate("MainWindow", u"Ping Test", None))
        self.label_2.setText("")
#if QT_CONFIG(whatsthis)
        self.btnquit.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/images/desligar.png\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btnquit.setText("")
        self.linepcname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: (4342_99_NB46)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Digite o nome do PC:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password provis\u00f3ria gerada:", None))
        self.linepassword.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.linepassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: (4342_99_NB46)", None))
        self.label_4.setText("")
        self.btn_backtomenu.setText("")
        self.submitbutton_laps.setText("")
        self.label_16.setText("")
        self.btn_backtomenu_3.setText("")
        self.submitbutton_ping.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Digite o n\u00famero do PA:", None))
        self.linepa.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Ex: (15)", None))
        self.linepcname_.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Ex: (4342_99_NB46)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Digite o nome do PC:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"FIREWALL", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"CCS", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"2009", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"UAD", None))
        self.firewallcheck.setText("")
        self.playcheck.setText("")
        self.ccscheck.setText("")
        self.centralcheck.setText("")
        self.uadcheck.setText("")
        self.btn_backtomenu_2.setText("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Digite o nome do PC:", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: (4342_99_NB46)", None))
        self.btn_cleaner.setText(QCoreApplication.translate("MainWindow", u"Cleaner", None))
        self.btn_gpupdate.setText(QCoreApplication.translate("MainWindow", u"GP Update", None))
        self.btn_shutdownr.setText(QCoreApplication.translate("MainWindow", u"Turn Off", None))
        self.btn_shutdowns.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.submitbutton_info.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"RAM", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Disco total", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"MAC", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"USER", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Disco livre", None))
    # retranslateUi

