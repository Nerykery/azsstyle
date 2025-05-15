# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainbUkCWr.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1281, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setAcceptDrops(True)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.gridLayout_3 = QGridLayout(self.styleSheet)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/azs.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;")
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setWeight(QFont.Bold)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.kassa = QPushButton(self.topMenu)
        self.kassa.setObjectName(u"kassa")
        sizePolicy.setHeightForWidth(self.kassa.sizePolicy().hasHeightForWidth())
        self.kassa.setSizePolicy(sizePolicy)
        self.kassa.setMinimumSize(QSize(0, 45))
        self.kassa.setFont(font)
        self.kassa.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.kassa.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.kassa.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-credit-card.png);")

        self.verticalLayout_8.addWidget(self.kassa)

        self.logs = QPushButton(self.topMenu)
        self.logs.setObjectName(u"logs")
        sizePolicy.setHeightForWidth(self.logs.sizePolicy().hasHeightForWidth())
        self.logs.setSizePolicy(sizePolicy)
        self.logs.setMinimumSize(QSize(0, 45))
        self.logs.setFont(font)
        self.logs.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logs.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.logs.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-description.png);")

        self.verticalLayout_8.addWidget(self.logs)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"/*  background-image: url(:/icons/images/icons/icon_settings.png);*/")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/azsstyle.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setGeometry(QRect(1, 236, 1156, 110))
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_17.addWidget(self.frame_content_wid_1)

        self.label_4 = QLabel(self.row_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 40, 51, 21))
        self.label_6 = QLabel(self.row_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 70, 51, 21))
        self.groupvibor = QComboBox(self.row_1)
        self.groupvibor.addItem("")
        self.groupvibor.addItem("")
        self.groupvibor.setObjectName(u"groupvibor")
        self.groupvibor.setGeometry(QRect(100, 100, 151, 31))
        self.groupvibor.setFont(font)
        self.groupvibor.setAutoFillBackground(False)
        self.groupvibor.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.groupvibor.setIconSize(QSize(16, 16))
        self.groupvibor.setFrame(True)
        self.password = QLineEdit(self.row_1)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(100, 70, 241, 23))
        self.login = QLineEdit(self.row_1)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(100, 40, 241, 23))
        self.label_13 = QLabel(self.row_1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 100, 101, 21))
        self.sozdatuser = QPushButton(self.row_1)
        self.sozdatuser.setObjectName(u"sozdatuser")
        self.sozdatuser.setGeometry(QRect(270, 100, 75, 31))
        self.label_3 = QLabel(self.row_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 271, 16))
        self.table_users = QTableWidget(self.row_1)
        if (self.table_users.columnCount() < 4):
            self.table_users.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_users.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.table_users.rowCount() < 16):
            self.table_users.setRowCount(16)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.table_users.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_users.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_users.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_users.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_users.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_users.setItem(0, 3, __qtablewidgetitem23)
        self.table_users.setObjectName(u"table_users")
        self.table_users.setGeometry(QRect(370, 0, 500, 201))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.table_users.sizePolicy().hasHeightForWidth())
        self.table_users.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.table_users.setPalette(palette)
        self.table_users.setFrameShape(QFrame.Shape.NoFrame)
        self.table_users.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_users.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_users.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.table_users.setAutoScroll(True)
        self.table_users.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_users.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_users.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_users.setShowGrid(True)
        self.table_users.setGridStyle(Qt.PenStyle.SolidLine)
        self.table_users.setSortingEnabled(False)
        self.table_users.horizontalHeader().setVisible(False)
        self.table_users.horizontalHeader().setCascadingSectionResizes(True)
        self.table_users.horizontalHeader().setMinimumSectionSize(50)
        self.table_users.horizontalHeader().setDefaultSectionSize(200)
        self.table_users.horizontalHeader().setHighlightSections(True)
        self.table_users.horizontalHeader().setStretchLastSection(False)
        self.table_users.verticalHeader().setVisible(False)
        self.table_users.verticalHeader().setCascadingSectionResizes(False)
        self.table_users.verticalHeader().setHighlightSections(False)
        self.table_users.verticalHeader().setStretchLastSection(False)
        self.delluser = QPushButton(self.row_1)
        self.delluser.setObjectName(u"delluser")
        self.delluser.setGeometry(QRect(920, 160, 161, 31))

        self.verticalLayout.addWidget(self.row_1)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.rezervuar1 = QFrame(self.new_page)
        self.rezervuar1.setObjectName(u"rezervuar1")
        self.rezervuar1.setGeometry(QRect(0, 0, 361, 181))
        self.rezervuar1.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"}")
        self.rezervuar1.setFrameShape(QFrame.Shape.NoFrame)
        self.rezervuar1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.rezervuar1)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.rezervuar1)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 30))
        self.frame_34.setMaximumSize(QSize(16777215, 30))
        self.frame_34.setStyleSheet(u"")
        self.frame_34.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 10, 0)
        self.label_22 = QLabel(self.frame_34)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(211, 0))
        self.label_22.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(16)
        font5.setWeight(QFont.Black)
        font5.setItalic(False)
        self.label_22.setFont(font5)
        self.label_22.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_22.setStyleSheet(u"color: rgb(170, 170, 170);\n"
"font: 900 16pt \"Segoe UI\";\n"
"  margin-left: auto;\n"
"  margin-right: auto;")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_22.setMargin(-9)

        self.horizontalLayout_18.addWidget(self.label_22)


        self.verticalLayout_26.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.rezervuar1)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_35.setFrameShape(QFrame.Shape.Panel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"")
        self.frame_36.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_36)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, -20, 131, 181))
        self.table_label_dt = QLabel(self.frame_36)
        self.table_label_dt.setObjectName(u"table_label_dt")
        self.table_label_dt.setGeometry(QRect(300, 10, 49, 81))
        self.dt_switch = QPushButton(self.frame_36)
        self.dt_switch.setObjectName(u"dt_switch")
        self.dt_switch.setGeometry(QRect(20, 100, 301, 41))
        self.dt_locker = QFrame(self.frame_36)
        self.dt_locker.setObjectName(u"dt_locker")
        self.dt_locker.setGeometry(QRect(330, 110, 21, 21))
        self.dt_locker.setStyleSheet(u"border-radius: 10px;\n"
"background-color: red;")
        self.dt_locker.setFrameShape(QFrame.Shape.StyledPanel)
        self.dt_locker.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_19.addWidget(self.frame_36)


        self.verticalLayout_26.addWidget(self.frame_35)

        self.progressBar_rezervuar1 = QProgressBar(self.new_page)
        self.progressBar_rezervuar1.setObjectName(u"progressBar_rezervuar1")
        self.progressBar_rezervuar1.setGeometry(QRect(10, 400, 200, 200))
        self.progressBar_rezervuar1.setMinimumSize(QSize(0, 200))
        self.progressBar_rezervuar1.setMaximumSize(QSize(16777215, 16))
        self.progressBar_rezervuar1.setFont(font)
        self.progressBar_rezervuar1.setAutoFillBackground(False)
        self.progressBar_rezervuar1.setStyleSheet(u"QProgressBar {\n"
"    color: rgb(177, 177, 177);\n"
"    border: none;\n"
"    background-color: rgb(102, 102, 102);\n"
"    border-radius: 4px;\n"
"    height: 200px; /* \u041c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e \u0436\u0435\u043b\u0430\u043d\u0438\u044e */\n"
"    min-height: 12px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.progressBar_rezervuar1.setValue(0)
        self.progressBar_rezervuar1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar_rezervuar1.setTextVisible(False)
        self.progressBar_rezervuar1.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_rezervuar1.setInvertedAppearance(False)
        self.progressBar_rezervuar1.setTextDirection(QProgressBar.Direction.TopToBottom)
        self.progressBar_rezervuar2 = QProgressBar(self.new_page)
        self.progressBar_rezervuar2.setObjectName(u"progressBar_rezervuar2")
        self.progressBar_rezervuar2.setGeometry(QRect(250, 400, 200, 200))
        self.progressBar_rezervuar2.setMinimumSize(QSize(0, 200))
        self.progressBar_rezervuar2.setMaximumSize(QSize(16777215, 16))
        self.progressBar_rezervuar2.setFont(font)
        self.progressBar_rezervuar2.setAutoFillBackground(False)
        self.progressBar_rezervuar2.setStyleSheet(u"QProgressBar {\n"
"    color: rgb(177, 177, 177);\n"
"    border: none;\n"
"    background-color: rgb(102, 102, 102);\n"
"    border-radius: 4px;\n"
"    height: 200px; /* \u041c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e \u0436\u0435\u043b\u0430\u043d\u0438\u044e */\n"
"    min-height: 12px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(255, 255, 0);\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.progressBar_rezervuar2.setMinimum(0)
        self.progressBar_rezervuar2.setValue(0)
        self.progressBar_rezervuar2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar_rezervuar2.setTextVisible(False)
        self.progressBar_rezervuar2.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_rezervuar2.setInvertedAppearance(False)
        self.progressBar_rezervuar2.setTextDirection(QProgressBar.Direction.TopToBottom)
        self.progressBar_rezervuar3 = QProgressBar(self.new_page)
        self.progressBar_rezervuar3.setObjectName(u"progressBar_rezervuar3")
        self.progressBar_rezervuar3.setGeometry(QRect(490, 400, 200, 200))
        self.progressBar_rezervuar3.setMinimumSize(QSize(0, 200))
        self.progressBar_rezervuar3.setMaximumSize(QSize(16777215, 16))
        self.progressBar_rezervuar3.setFont(font)
        self.progressBar_rezervuar3.setAutoFillBackground(False)
        self.progressBar_rezervuar3.setStyleSheet(u"QProgressBar {\n"
"    color: rgb(177, 177, 177);\n"
"    border: none;\n"
"    background-color: rgb(102, 102, 102);\n"
"    border-radius: 4px;\n"
"    height: 200px; /* \u041c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e \u0436\u0435\u043b\u0430\u043d\u0438\u044e */\n"
"    min-height: 12px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(51, 153, 255);\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.progressBar_rezervuar3.setValue(0)
        self.progressBar_rezervuar3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar_rezervuar3.setTextVisible(False)
        self.progressBar_rezervuar3.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_rezervuar3.setInvertedAppearance(False)
        self.progressBar_rezervuar3.setTextDirection(QProgressBar.Direction.TopToBottom)
        self.progressBar_rezervuar4 = QProgressBar(self.new_page)
        self.progressBar_rezervuar4.setObjectName(u"progressBar_rezervuar4")
        self.progressBar_rezervuar4.setGeometry(QRect(730, 400, 200, 200))
        self.progressBar_rezervuar4.setMinimumSize(QSize(0, 200))
        self.progressBar_rezervuar4.setMaximumSize(QSize(16777215, 16))
        self.progressBar_rezervuar4.setFont(font)
        self.progressBar_rezervuar4.setAutoFillBackground(False)
        self.progressBar_rezervuar4.setStyleSheet(u"QProgressBar {\n"
"    color: rgb(177, 177, 177);\n"
"    border: none;\n"
"    background-color: rgb(102, 102, 102);\n"
"    border-radius: 4px;\n"
"    height: 200px; /* \u041c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e \u0436\u0435\u043b\u0430\u043d\u0438\u044e */\n"
"    min-height: 12px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.progressBar_rezervuar4.setValue(0)
        self.progressBar_rezervuar4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar_rezervuar4.setTextVisible(False)
        self.progressBar_rezervuar4.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_rezervuar4.setInvertedAppearance(False)
        self.progressBar_rezervuar4.setTextDirection(QProgressBar.Direction.TopToBottom)
        self.progressBar_rezervuar5 = QProgressBar(self.new_page)
        self.progressBar_rezervuar5.setObjectName(u"progressBar_rezervuar5")
        self.progressBar_rezervuar5.setGeometry(QRect(970, 400, 200, 200))
        self.progressBar_rezervuar5.setMinimumSize(QSize(0, 200))
        self.progressBar_rezervuar5.setMaximumSize(QSize(16777215, 16))
        self.progressBar_rezervuar5.setFont(font)
        self.progressBar_rezervuar5.setAutoFillBackground(False)
        self.progressBar_rezervuar5.setStyleSheet(u"QProgressBar {\n"
"    color: rgb(177, 177, 177);\n"
"    border: none;\n"
"    background-color: rgb(102, 102, 102);\n"
"    border-radius: 4px;\n"
"    height: 200px; /* \u041c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e \u0436\u0435\u043b\u0430\u043d\u0438\u044e */\n"
"    min-height: 12px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color: rgb(0, 153, 0);\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.progressBar_rezervuar5.setValue(0)
        self.progressBar_rezervuar5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar_rezervuar5.setTextVisible(False)
        self.progressBar_rezervuar5.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_rezervuar5.setInvertedAppearance(False)
        self.progressBar_rezervuar5.setTextDirection(QProgressBar.Direction.TopToBottom)
        self.rezervuar1_2 = QFrame(self.new_page)
        self.rezervuar1_2.setObjectName(u"rezervuar1_2")
        self.rezervuar1_2.setGeometry(QRect(0, 190, 361, 181))
        self.rezervuar1_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"}")
        self.rezervuar1_2.setFrameShape(QFrame.Shape.NoFrame)
        self.rezervuar1_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.rezervuar1_2)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.rezervuar1_2)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(0, 30))
        self.frame_37.setMaximumSize(QSize(16777215, 30))
        self.frame_37.setStyleSheet(u"")
        self.frame_37.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 10, 0)
        self.label_23 = QLabel(self.frame_37)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(211, 0))
        self.label_23.setMaximumSize(QSize(16777215, 16777215))
        self.label_23.setFont(font5)
        self.label_23.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_23.setStyleSheet(u"color: rgb(170, 170, 170);\n"
"font: 900 16pt \"Segoe UI\";\n"
"  margin-left: auto;\n"
"  margin-right: auto;")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_23.setMargin(-9)

        self.horizontalLayout_20.addWidget(self.label_23)


        self.verticalLayout_27.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.rezervuar1_2)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_38.setFrameShape(QFrame.Shape.Panel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"")
        self.frame_39.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame_39)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, -20, 131, 181))
        self.table_label_a80 = QLabel(self.frame_39)
        self.table_label_a80.setObjectName(u"table_label_a80")
        self.table_label_a80.setGeometry(QRect(300, 0, 49, 141))
        self.a80_switch = QPushButton(self.frame_39)
        self.a80_switch.setObjectName(u"a80_switch")
        self.a80_switch.setGeometry(QRect(20, 100, 301, 41))
        self.a80_locker = QFrame(self.frame_39)
        self.a80_locker.setObjectName(u"a80_locker")
        self.a80_locker.setGeometry(QRect(330, 110, 21, 21))
        self.a80_locker.setStyleSheet(u"border-radius: 10px;\n"
"background-color: red;")
        self.a80_locker.setFrameShape(QFrame.Shape.StyledPanel)
        self.a80_locker.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_21.addWidget(self.frame_39)


        self.verticalLayout_27.addWidget(self.frame_38)

        self.label_dt = QLabel(self.new_page)
        self.label_dt.setObjectName(u"label_dt")
        self.label_dt.setGeometry(QRect(60, 430, 91, 161))
        self.rezervuar1_3 = QFrame(self.new_page)
        self.rezervuar1_3.setObjectName(u"rezervuar1_3")
        self.rezervuar1_3.setGeometry(QRect(400, 0, 361, 181))
        self.rezervuar1_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"}")
        self.rezervuar1_3.setFrameShape(QFrame.Shape.NoFrame)
        self.rezervuar1_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.rezervuar1_3)
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.rezervuar1_3)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 30))
        self.frame_40.setMaximumSize(QSize(16777215, 30))
        self.frame_40.setStyleSheet(u"")
        self.frame_40.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 10, 0)
        self.label_24 = QLabel(self.frame_40)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(211, 0))
        self.label_24.setMaximumSize(QSize(16777215, 16777215))
        self.label_24.setFont(font5)
        self.label_24.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_24.setStyleSheet(u"color: rgb(170, 170, 170);\n"
"font: 900 16pt \"Segoe UI\";\n"
"  margin-left: auto;\n"
"  margin-right: auto;")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_24.setMargin(-9)

        self.horizontalLayout_22.addWidget(self.label_24)


        self.verticalLayout_28.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.rezervuar1_3)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_41.setFrameShape(QFrame.Shape.Panel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"")
        self.frame_42.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame_42)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, -20, 131, 181))
        self.table_label_ai92 = QLabel(self.frame_42)
        self.table_label_ai92.setObjectName(u"table_label_ai92")
        self.table_label_ai92.setGeometry(QRect(300, 0, 49, 141))
        self.ai92_switch = QPushButton(self.frame_42)
        self.ai92_switch.setObjectName(u"ai92_switch")
        self.ai92_switch.setGeometry(QRect(20, 100, 301, 41))
        self.ai92_locker = QFrame(self.frame_42)
        self.ai92_locker.setObjectName(u"ai92_locker")
        self.ai92_locker.setGeometry(QRect(330, 110, 21, 21))
        self.ai92_locker.setStyleSheet(u"border-radius: 10px;\n"
"background-color: red;")
        self.ai92_locker.setFrameShape(QFrame.Shape.StyledPanel)
        self.ai92_locker.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_23.addWidget(self.frame_42)


        self.verticalLayout_28.addWidget(self.frame_41)

        self.rezervuar1_4 = QFrame(self.new_page)
        self.rezervuar1_4.setObjectName(u"rezervuar1_4")
        self.rezervuar1_4.setGeometry(QRect(800, 0, 361, 181))
        self.rezervuar1_4.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"}")
        self.rezervuar1_4.setFrameShape(QFrame.Shape.NoFrame)
        self.rezervuar1_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.rezervuar1_4)
        self.verticalLayout_29.setSpacing(5)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.rezervuar1_4)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 30))
        self.frame_43.setMaximumSize(QSize(16777215, 30))
        self.frame_43.setStyleSheet(u"")
        self.frame_43.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 10, 0)
        self.label_25 = QLabel(self.frame_43)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(211, 0))
        self.label_25.setMaximumSize(QSize(16777215, 16777215))
        self.label_25.setFont(font5)
        self.label_25.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_25.setStyleSheet(u"color: rgb(170, 170, 170);\n"
"font: 900 16pt \"Segoe UI\";\n"
"  margin-left: auto;\n"
"  margin-right: auto;")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_25.setMargin(-9)

        self.horizontalLayout_24.addWidget(self.label_25)


        self.verticalLayout_29.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.rezervuar1_4)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_44.setFrameShape(QFrame.Shape.Panel)
        self.frame_44.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"")
        self.frame_45.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7 = QLabel(self.frame_45)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, -20, 131, 181))
        self.table_label_ai95 = QLabel(self.frame_45)
        self.table_label_ai95.setObjectName(u"table_label_ai95")
        self.table_label_ai95.setGeometry(QRect(300, 0, 49, 141))
        self.ai95_switch = QPushButton(self.frame_45)
        self.ai95_switch.setObjectName(u"ai95_switch")
        self.ai95_switch.setGeometry(QRect(20, 100, 301, 41))
        self.ai95_locker = QFrame(self.frame_45)
        self.ai95_locker.setObjectName(u"ai95_locker")
        self.ai95_locker.setGeometry(QRect(330, 110, 21, 21))
        self.ai95_locker.setStyleSheet(u"border-radius: 10px;\n"
"background-color: red;")
        self.ai95_locker.setFrameShape(QFrame.Shape.StyledPanel)
        self.ai95_locker.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_25.addWidget(self.frame_45)


        self.verticalLayout_29.addWidget(self.frame_44)

        self.rezervuar1_5 = QFrame(self.new_page)
        self.rezervuar1_5.setObjectName(u"rezervuar1_5")
        self.rezervuar1_5.setGeometry(QRect(800, 190, 361, 181))
        self.rezervuar1_5.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"}")
        self.rezervuar1_5.setFrameShape(QFrame.Shape.NoFrame)
        self.rezervuar1_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.rezervuar1_5)
        self.verticalLayout_30.setSpacing(5)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.rezervuar1_5)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(0, 30))
        self.frame_46.setMaximumSize(QSize(16777215, 30))
        self.frame_46.setStyleSheet(u"")
        self.frame_46.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_46.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 10, 0)
        self.label_26 = QLabel(self.frame_46)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(211, 0))
        self.label_26.setMaximumSize(QSize(16777215, 16777215))
        self.label_26.setFont(font5)
        self.label_26.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_26.setStyleSheet(u"color: rgb(170, 170, 170);\n"
"font: 900 16pt \"Segoe UI\";\n"
"  margin-left: auto;\n"
"  margin-right: auto;")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_26.setMargin(-9)

        self.horizontalLayout_26.addWidget(self.label_26)


        self.verticalLayout_30.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.rezervuar1_5)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_47.setFrameShape(QFrame.Shape.Panel)
        self.frame_47.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"")
        self.frame_48.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Shadow.Raised)
        self.label_9 = QLabel(self.frame_48)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, -20, 131, 181))
        self.table_label_ai98 = QLabel(self.frame_48)
        self.table_label_ai98.setObjectName(u"table_label_ai98")
        self.table_label_ai98.setGeometry(QRect(300, 0, 49, 141))
        self.ai98_switch = QPushButton(self.frame_48)
        self.ai98_switch.setObjectName(u"ai98_switch")
        self.ai98_switch.setGeometry(QRect(20, 100, 301, 41))
        self.ai98_locker = QFrame(self.frame_48)
        self.ai98_locker.setObjectName(u"ai98_locker")
        self.ai98_locker.setGeometry(QRect(330, 110, 21, 21))
        self.ai98_locker.setStyleSheet(u"border-radius: 10px;\n"
"background-color: red;")
        self.ai98_locker.setFrameShape(QFrame.Shape.StyledPanel)
        self.ai98_locker.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_27.addWidget(self.frame_48)


        self.verticalLayout_30.addWidget(self.frame_47)

        self.label_a80 = QLabel(self.new_page)
        self.label_a80.setObjectName(u"label_a80")
        self.label_a80.setGeometry(QRect(300, 430, 91, 161))
        self.label_a80.setStyleSheet(u"")
        self.label_ai92 = QLabel(self.new_page)
        self.label_ai92.setObjectName(u"label_ai92")
        self.label_ai92.setGeometry(QRect(540, 430, 91, 161))
        self.label_ai95 = QLabel(self.new_page)
        self.label_ai95.setObjectName(u"label_ai95")
        self.label_ai95.setGeometry(QRect(780, 430, 91, 161))
        self.label_ai98 = QLabel(self.new_page)
        self.label_ai98.setObjectName(u"label_ai98")
        self.label_ai98.setGeometry(QRect(1020, 430, 91, 161))
        self.testradiobutton = QRadioButton(self.new_page)
        self.testradiobutton.setObjectName(u"testradiobutton")
        self.testradiobutton.setGeometry(QRect(530, 380, 98, 21))
        self.testradiobutton.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.new_page)
        self.kase_page = QWidget()
        self.kase_page.setObjectName(u"kase_page")
        self.kassa_cifra1_button = QPushButton(self.kase_page)
        self.kassa_cifra1_button.setObjectName(u"kassa_cifra1_button")
        self.kassa_cifra1_button.setGeometry(QRect(640, 160, 101, 81))
        self.kassa_cifra1_button.setStyleSheet(u"QPushButton {\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weight: bold;          /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 2px solid #2980b9;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 (\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f) */\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px 16px;          /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(41, 128, 185, 0.7);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 (\u0430"
                        "\u043b\u044c\u0444\u0430 = 0.7) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.kassa_cifra2_button = QPushButton(self.kase_page)
        self.kassa_cifra2_button.setObjectName(u"kassa_cifra2_button")
        self.kassa_cifra2_button.setGeometry(QRect(750, 160, 101, 81))
        self.kassa_cifra2_button.setStyleSheet(u"QPushButton {\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weight: bold;          /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 2px solid #2980b9;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 (\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f) */\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px 16px;          /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(41, 128, 185, 0.7);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 (\u0430"
                        "\u043b\u044c\u0444\u0430 = 0.7) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.kassa_cifra3_button = QPushButton(self.kase_page)
        self.kassa_cifra3_button.setObjectName(u"kassa_cifra3_button")
        self.kassa_cifra3_button.setGeometry(QRect(860, 160, 101, 81))
        self.kassa_cifra3_button.setStyleSheet(u"QPushButton {\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weight: bold;          /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 2px solid #2980b9;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 (\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f) */\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px 16px;          /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(41, 128, 185, 0.7);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 (\u0430"
                        "\u043b\u044c\u0444\u0430 = 0.7) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.kassa_cifra4_button = QPushButton(self.kase_page)
        self.kassa_cifra4_button.setObjectName(u"kassa_cifra4_button")
        self.kassa_cifra4_button.setGeometry(QRect(640, 250, 101, 81))
        self.kassa_cifra4_button.setStyleSheet(u"QPushButton {\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weight: bold;          /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 2px solid #2980b9;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 (\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f) */\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px 16px;          /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(41, 128, 185, 0.7);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 (\u0430"
                        "\u043b\u044c\u0444\u0430 = 0.7) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.kassa_cifra6_button = QPushButton(self.kase_page)
        self.kassa_cifra6_button.setObjectName(u"kassa_cifra6_button")
        self.kassa_cifra6_button.setGeometry(QRect(860, 250, 101, 81))
        self.kassa_cifra6_button.setStyleSheet(u"QPushButton {\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weight: bold;          /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 2px solid #2980b9;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 (\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f) */\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px 16px;          /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(41, 128, 185, 0.7);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 (\u0430"
                        "\u043b\u044c\u0444\u0430 = 0.7) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.kassa_cifra5_button = QPushButton(self.kase_page)
        self.kassa_cifra5_button.setObjectName(u"kassa_cifra5_button")
        self.kassa_cifra5_button.setGeometry(QRect(750, 250, 101, 81))
        self.kassa_cifra5_button.setStyleSheet(u"QPushButton {\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weight: bold;          /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 2px solid #2980b9;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 (\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f) */\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px 16px;          /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(41, 128, 185, 0.7);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 (\u0430"
                        "\u043b\u044c\u0444\u0430 = 0.7) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.kassa_cifra7_button = QPushButton(self.kase_page)
        self.kassa_cifra7_button.setObjectName(u"kassa_cifra7_button")
        self.kassa_cifra7_button.setGeometry(QRect(640, 340, 101, 81))
        self.kassa_cifra7_button.setStyleSheet(u"QPushButton {\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weight: bold;          /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 2px solid #2980b9;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 (\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f) */\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px 16px;          /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(41, 128, 185, 0.7);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 (\u0430"
                        "\u043b\u044c\u0444\u0430 = 0.7) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.kassa_cifra9_button = QPushButton(self.kase_page)
        self.kassa_cifra9_button.setObjectName(u"kassa_cifra9_button")
        self.kassa_cifra9_button.setGeometry(QRect(860, 340, 101, 81))
        self.kassa_cifra9_button.setStyleSheet(u"QPushButton {\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weight: bold;          /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 2px solid #2980b9;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 (\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f) */\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px 16px;          /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(41, 128, 185, 0.7);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 (\u0430"
                        "\u043b\u044c\u0444\u0430 = 0.7) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.kassa_cifra8_button = QPushButton(self.kase_page)
        self.kassa_cifra8_button.setObjectName(u"kassa_cifra8_button")
        self.kassa_cifra8_button.setGeometry(QRect(750, 340, 101, 81))
        self.kassa_cifra8_button.setStyleSheet(u"QPushButton {\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weight: bold;          /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 2px solid #2980b9;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 (\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f) */\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px 16px;          /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(41, 128, 185, 0.7);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 (\u0430"
                        "\u043b\u044c\u0444\u0430 = 0.7) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.kassa_cifra0_button = QPushButton(self.kase_page)
        self.kassa_cifra0_button.setObjectName(u"kassa_cifra0_button")
        self.kassa_cifra0_button.setGeometry(QRect(640, 430, 101, 81))
        self.kassa_cifra0_button.setStyleSheet(u"QPushButton {\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weight: bold;          /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 2px solid #2980b9;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 (\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f) */\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px 16px;          /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(41, 128, 185, 0.7);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 (\u0430"
                        "\u043b\u044c\u0444\u0430 = 0.7) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.kassa_dot_button = QPushButton(self.kase_page)
        self.kassa_dot_button.setObjectName(u"kassa_dot_button")
        self.kassa_dot_button.setGeometry(QRect(860, 430, 101, 81))
        self.kassa_dot_button.setStyleSheet(u"QPushButton {\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weight: bold;          /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 2px solid #2980b9;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 (\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f) */\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px 16px;          /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(41, 128, 185, 0.7);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 (\u0430"
                        "\u043b\u044c\u0444\u0430 = 0.7) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.kassa_cifra00_button = QPushButton(self.kase_page)
        self.kassa_cifra00_button.setObjectName(u"kassa_cifra00_button")
        self.kassa_cifra00_button.setGeometry(QRect(750, 430, 101, 81))
        self.kassa_cifra00_button.setStyleSheet(u"QPushButton {\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weight: bold;          /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 2px solid #2980b9;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 (\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f) */\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px 16px;          /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(41, 128, 185, 0.7);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 (\u0430"
                        "\u043b\u044c\u0444\u0430 = 0.7) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.kassa_enter_button = QPushButton(self.kase_page)
        self.kassa_enter_button.setObjectName(u"kassa_enter_button")
        self.kassa_enter_button.setGeometry(QRect(970, 340, 161, 171))
        self.kassa_enter_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;  /* \u0421\u0438\u043d\u0438\u0439 \u0444\u043e\u043d */\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weight: bold;          /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 2px solid #2980b9;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 (\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f) */\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px 16px;          /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(41, 128, 185, 0.7);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e"
                        "\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 (\u0430\u043b\u044c\u0444\u0430 = 0.7) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.kassa_clear_button = QPushButton(self.kase_page)
        self.kassa_clear_button.setObjectName(u"kassa_clear_button")
        self.kassa_clear_button.setGeometry(QRect(970, 160, 161, 171))
        self.kassa_clear_button.setStyleSheet(u"QPushButton {\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weight: bold;          /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 2px solid #2980b9;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 (\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f) */\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 8px 16px;          /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(41, 128, 185, 0.7);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 (\u0430"
                        "\u043b\u044c\u0444\u0430 = 0.7) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.kassa_dt_label = QLabel(self.kase_page)
        self.kassa_dt_label.setObjectName(u"kassa_dt_label")
        self.kassa_dt_label.setGeometry(QRect(20, 70, 341, 81))
        self.kassa_dt_label.setStyleSheet(u"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 30px;\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    display: flex;\n"
"    justify-content: center;\n"
"    align-items: center;\n"
"    padding: 9px;")
        self.kassa_ai92_label = QLabel(self.kase_page)
        self.kassa_ai92_label.setObjectName(u"kassa_ai92_label")
        self.kassa_ai92_label.setGeometry(QRect(20, 150, 341, 81))
        self.kassa_ai92_label.setStyleSheet(u"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 30px;\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    display: flex;\n"
"    justify-content: center;\n"
"    align-items: center;\n"
"    padding: 9px;")
        self.kassa_ai95_label = QLabel(self.kase_page)
        self.kassa_ai95_label.setObjectName(u"kassa_ai95_label")
        self.kassa_ai95_label.setGeometry(QRect(20, 230, 341, 81))
        self.kassa_ai95_label.setStyleSheet(u"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 30px;\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    display: flex;\n"
"    justify-content: center;\n"
"    align-items: center;\n"
"    padding: 9px;")
        self.kassa_a80_label = QLabel(self.kase_page)
        self.kassa_a80_label.setObjectName(u"kassa_a80_label")
        self.kassa_a80_label.setGeometry(QRect(20, 310, 341, 81))
        self.kassa_a80_label.setStyleSheet(u"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 30px;\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    display: flex;\n"
"    justify-content: center;\n"
"    align-items: center;\n"
"    padding: 9px;")
        self.kassa_ai98_label = QLabel(self.kase_page)
        self.kassa_ai98_label.setObjectName(u"kassa_ai98_label")
        self.kassa_ai98_label.setGeometry(QRect(20, 390, 341, 81))
        self.kassa_ai98_label.setStyleSheet(u"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 30px;\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    display: flex;\n"
"    justify-content: center;\n"
"    align-items: center;\n"
"    padding: 9px;")
        self.litri_dt = QLineEdit(self.kase_page)
        self.litri_dt.setObjectName(u"litri_dt")
        self.litri_dt.setGeometry(QRect(150, 92, 151, 31))
        self.litri_dt.setStyleSheet(u"    font-weight: bold;\n"
"    font-size: 16px;\n"
"")
        self.label_8 = QLabel(self.kase_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 90, 20, 31))
        self.label_10 = QLabel(self.kase_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(300, 178, 20, 31))
        self.litri_ai92 = QLineEdit(self.kase_page)
        self.litri_ai92.setObjectName(u"litri_ai92")
        self.litri_ai92.setGeometry(QRect(150, 180, 151, 31))
        self.litri_ai92.setStyleSheet(u"    font-weight: bold;\n"
"    font-size: 16px;\n"
"")
        self.label_11 = QLabel(self.kase_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(300, 258, 20, 31))
        self.litri_ai95 = QLineEdit(self.kase_page)
        self.litri_ai95.setObjectName(u"litri_ai95")
        self.litri_ai95.setGeometry(QRect(150, 260, 151, 31))
        self.litri_ai95.setStyleSheet(u"    font-weight: bold;\n"
"    font-size: 16px;\n"
"")
        self.label_12 = QLabel(self.kase_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(300, 338, 20, 31))
        self.litri_a80 = QLineEdit(self.kase_page)
        self.litri_a80.setObjectName(u"litri_a80")
        self.litri_a80.setGeometry(QRect(150, 340, 151, 31))
        self.litri_a80.setStyleSheet(u"    font-weight: bold;\n"
"    font-size: 16px;\n"
"")
        self.label_14 = QLabel(self.kase_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(300, 410, 20, 31))
        self.litri_ai98 = QLineEdit(self.kase_page)
        self.litri_ai98.setObjectName(u"litri_ai98")
        self.litri_ai98.setGeometry(QRect(150, 412, 151, 31))
        self.litri_ai98.setStyleSheet(u"    font-weight: bold;\n"
"    font-size: 16px;\n"
"")
        self.radioButton_dt = QRadioButton(self.kase_page)
        self.radioButton_dt.setObjectName(u"radioButton_dt")
        self.radioButton_dt.setGeometry(QRect(320, 90, 21, 31))
        self.radioButton_ai92 = QRadioButton(self.kase_page)
        self.radioButton_ai92.setObjectName(u"radioButton_ai92")
        self.radioButton_ai92.setGeometry(QRect(320, 180, 21, 31))
        self.radioButton_ai95 = QRadioButton(self.kase_page)
        self.radioButton_ai95.setObjectName(u"radioButton_ai95")
        self.radioButton_ai95.setGeometry(QRect(320, 264, 21, 21))
        self.radioButton_a80 = QRadioButton(self.kase_page)
        self.radioButton_a80.setObjectName(u"radioButton_a80")
        self.radioButton_a80.setGeometry(QRect(320, 340, 21, 31))
        self.radioButton_98 = QRadioButton(self.kase_page)
        self.radioButton_98.setObjectName(u"radioButton_98")
        self.radioButton_98.setGeometry(QRect(321, 413, 21, 31))
        self.kassa_oknovvoda = QLineEdit(self.kase_page)
        self.kassa_oknovvoda.setObjectName(u"kassa_oknovvoda")
        self.kassa_oknovvoda.setGeometry(QRect(640, 80, 491, 71))
        self.kassa_oknovvoda.setStyleSheet(u"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 30px;\n"
"    border: 2px solid #2980b9;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    display: flex;\n"
"    justify-content: center;\n"
"    align-items: center;\n"
"    padding: 9px;")
        self.stackedWidget.addWidget(self.kase_page)
        self.logs_page = QWidget()
        self.logs_page.setObjectName(u"logs_page")
        self.table_logs = QTableWidget(self.logs_page)
        if (self.table_logs.columnCount() < 4):
            self.table_logs.setColumnCount(4)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_logs.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_logs.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_logs.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_logs.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        if (self.table_logs.rowCount() < 16):
            self.table_logs.setRowCount(16)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font4);
        self.table_logs.setVerticalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(8, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(9, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(10, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(11, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(12, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(13, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(14, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.table_logs.setVerticalHeaderItem(15, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.table_logs.setItem(0, 0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.table_logs.setItem(0, 1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.table_logs.setItem(0, 2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.table_logs.setItem(0, 3, __qtablewidgetitem47)
        self.table_logs.setObjectName(u"table_logs")
        self.table_logs.setGeometry(QRect(120, 0, 1001, 601))
        sizePolicy3.setHeightForWidth(self.table_logs.sizePolicy().hasHeightForWidth())
        self.table_logs.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.table_logs.setPalette(palette1)
        self.table_logs.setFrameShape(QFrame.Shape.NoFrame)
        self.table_logs.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_logs.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_logs.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.table_logs.setAutoScroll(True)
        self.table_logs.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_logs.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_logs.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_logs.setShowGrid(True)
        self.table_logs.setGridStyle(Qt.PenStyle.SolidLine)
        self.table_logs.setSortingEnabled(False)
        self.table_logs.horizontalHeader().setVisible(False)
        self.table_logs.horizontalHeader().setCascadingSectionResizes(True)
        self.table_logs.horizontalHeader().setMinimumSectionSize(50)
        self.table_logs.horizontalHeader().setDefaultSectionSize(200)
        self.table_logs.horizontalHeader().setHighlightSections(True)
        self.table_logs.horizontalHeader().setStretchLastSection(False)
        self.table_logs.verticalHeader().setVisible(False)
        self.table_logs.verticalHeader().setCascadingSectionResizes(False)
        self.table_logs.verticalHeader().setHighlightSections(False)
        self.table_logs.verticalHeader().setStretchLastSection(False)
        self.stackedWidget.addWidget(self.logs_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.gridLayout_3.addWidget(self.bgApp, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u044b\u0442\u044c", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043d\u0435\u043b\u044c \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.kassa.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0441\u0441\u0430", None))
        self.logs.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">AZS style</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Nerykery</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.p"
                        "y</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"AZS style", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0440\u043d\u0443\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u044b\u0439 \u044d\u043a\u0440\u0430\u043d", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.groupvibor.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.groupvibor.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u043b\u044c", None))
        self.sozdatuser.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        ___qtablewidgetitem = self.table_users.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.table_users.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.table_users.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.table_users.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.table_users.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.table_users.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.table_users.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.table_users.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.table_users.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.table_users.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.table_users.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.table_users.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.table_users.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.table_users.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.table_users.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.table_users.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.table_users.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.table_users.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.table_users.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.table_users.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.table_users.isSortingEnabled()
        self.table_users.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.table_users.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.table_users.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.table_users.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.table_users.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.table_users.setSortingEnabled(__sortingEnabled)

        self.delluser.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0422", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u0440\u043e\u0432\u0435\u043d\u044c, \u043c\u043c</p><p>\u0422\u043e\u043f\u043b\u0438\u0432\u043e \u043a \u0434\u043e\u043f\u0443\u0441\u043a\u0443, \u043b</p><p>\u0422\u043e\u043f\u043b\u0438\u0432\u043e \u043a \u043f\u0440\u0438\u0435\u043c\u0443, \u043b</p><p><br/></p></body></html>", None))
        self.table_label_dt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">1</p><p align=\"right\">2</p><p align=\"right\">3</p><p align=\"right\"><br/></p></body></html>", None))
        self.dt_switch.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u043a\u0430 \u043f\u0438\u0441\u0442\u043e\u043b\u0435\u0442\u0430", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0410-80", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u0440\u043e\u0432\u0435\u043d\u044c, \u043c\u043c</p><p>\u0422\u043e\u043f\u043b\u0438\u0432\u043e \u043a \u0434\u043e\u043f\u0443\u0441\u043a\u0443, \u043b</p><p>\u0422\u043e\u043f\u043b\u0438\u0432\u043e \u043a \u043f\u0440\u0438\u0435\u043c\u0443, \u043b</p><p><br/></p></body></html>", None))
        self.table_label_a80.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">1</p><p align=\"right\">2</p><p align=\"right\">3</p><p align=\"right\"><br/></p></body></html>", None))
        self.a80_switch.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u043a\u0430 \u043f\u0438\u0441\u0442\u043e\u043b\u0435\u0442\u0430", None))
        self.label_dt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">\u0414\u0422</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">------</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">00 \u043c\u043c</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">00 \u043b</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0418-92", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u0440\u043e\u0432\u0435\u043d\u044c, \u043c\u043c</p><p>\u0422\u043e\u043f\u043b\u0438\u0432\u043e \u043a \u0434\u043e\u043f\u0443\u0441\u043a\u0443, \u043b</p><p>\u0422\u043e\u043f\u043b\u0438\u0432\u043e \u043a \u043f\u0440\u0438\u0435\u043c\u0443, \u043b</p><p><br/></p></body></html>", None))
        self.table_label_ai92.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">1</p><p align=\"right\">2</p><p align=\"right\">3</p><p align=\"right\"><br/></p></body></html>", None))
        self.ai92_switch.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u043a\u0430 \u043f\u0438\u0441\u0442\u043e\u043b\u0435\u0442\u0430", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0418-95", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u0440\u043e\u0432\u0435\u043d\u044c, \u043c\u043c</p><p>\u0422\u043e\u043f\u043b\u0438\u0432\u043e \u043a \u0434\u043e\u043f\u0443\u0441\u043a\u0443, \u043b</p><p>\u0422\u043e\u043f\u043b\u0438\u0432\u043e \u043a \u043f\u0440\u0438\u0435\u043c\u0443, \u043b</p><p><br/></p></body></html>", None))
        self.table_label_ai95.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">1</p><p align=\"right\">2</p><p align=\"right\">3</p><p align=\"right\"><br/></p></body></html>", None))
        self.ai95_switch.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u043a\u0430 \u043f\u0438\u0441\u0442\u043e\u043b\u0435\u0442\u0430", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0418-98", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u0440\u043e\u0432\u0435\u043d\u044c, \u043c\u043c</p><p>\u0422\u043e\u043f\u043b\u0438\u0432\u043e \u043a \u0434\u043e\u043f\u0443\u0441\u043a\u0443, \u043b</p><p>\u0422\u043e\u043f\u043b\u0438\u0432\u043e \u043a \u043f\u0440\u0438\u0435\u043c\u0443, \u043b</p><p><br/></p></body></html>", None))
        self.table_label_ai98.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">1</p><p align=\"right\">2</p><p align=\"right\">3</p><p align=\"right\"><br/></p></body></html>", None))
        self.ai98_switch.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u043a\u0430 \u043f\u0438\u0441\u0442\u043e\u043b\u0435\u0442\u0430", None))
        self.label_a80.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#000000;\">A-80</span></p><p align=\"center\"><span style=\" font-weight:700; color:#000000;\">------</span></p><p align=\"center\"><span style=\" font-weight:700; color:#000000;\">00 \u043c\u043c</span></p><p align=\"center\"><span style=\" font-weight:700; color:#000000;\">00 \u043b</span></p></body></html>", None))
        self.label_ai92.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">\u0410\u0418-92</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">------</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">00 \u043c\u043c</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">00 \u043b</span></p></body></html>", None))
        self.label_ai95.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">\u0410\u0418-95</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">------</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">00 \u043c\u043c</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">00 \u043b</span></p></body></html>", None))
        self.label_ai98.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">\u0410\u0418-98</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">------</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">00 \u043c\u043c</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">00 \u043b</span></p><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">00 \u043c\u043c</span></p></body></html>", None))
        self.testradiobutton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.kassa_cifra1_button.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.kassa_cifra2_button.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.kassa_cifra3_button.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.kassa_cifra4_button.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.kassa_cifra6_button.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.kassa_cifra5_button.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.kassa_cifra7_button.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.kassa_cifra9_button.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.kassa_cifra8_button.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.kassa_cifra0_button.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.kassa_dot_button.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.kassa_cifra00_button.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.kassa_enter_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0412\u041e\u0414", None))
        self.kassa_clear_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0411\u0420\u041e\u0421", None))
        self.kassa_dt_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0422", None))
        self.kassa_ai92_label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0418-92", None))
        self.kassa_ai95_label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0418-95", None))
        self.kassa_a80_label.setText(QCoreApplication.translate("MainWindow", u"\u0410-80", None))
        self.kassa_ai98_label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0418-98", None))
        self.litri_dt.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u043b</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u043b</span></p></body></html>", None))
        self.litri_ai92.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u043b</span></p></body></html>", None))
        self.litri_ai95.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u043b</span></p></body></html>", None))
        self.litri_a80.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u043b</span></p></body></html>", None))
        self.litri_ai98.setText("")
        self.radioButton_dt.setText("")
        self.radioButton_ai92.setText("")
        self.radioButton_ai95.setText("")
        self.radioButton_a80.setText("")
        self.radioButton_98.setText("")
        ___qtablewidgetitem24 = self.table_logs.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem25 = self.table_logs.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem26 = self.table_logs.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem27 = self.table_logs.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem28 = self.table_logs.verticalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem29 = self.table_logs.verticalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem30 = self.table_logs.verticalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.table_logs.verticalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem32 = self.table_logs.verticalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem33 = self.table_logs.verticalHeaderItem(5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem34 = self.table_logs.verticalHeaderItem(6)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem35 = self.table_logs.verticalHeaderItem(7)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem36 = self.table_logs.verticalHeaderItem(8)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem37 = self.table_logs.verticalHeaderItem(9)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem38 = self.table_logs.verticalHeaderItem(10)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem39 = self.table_logs.verticalHeaderItem(11)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem40 = self.table_logs.verticalHeaderItem(12)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem41 = self.table_logs.verticalHeaderItem(13)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem42 = self.table_logs.verticalHeaderItem(14)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem43 = self.table_logs.verticalHeaderItem(15)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.table_logs.isSortingEnabled()
        self.table_logs.setSortingEnabled(False)
        ___qtablewidgetitem44 = self.table_logs.item(0, 0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem45 = self.table_logs.item(0, 1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem46 = self.table_logs.item(0, 2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem47 = self.table_logs.item(0, 3)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.table_logs.setSortingEnabled(__sortingEnabled1)

        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Nerykery", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

