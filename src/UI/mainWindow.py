# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main.ui'
##
# Created by: Qt User Interface Compiler version 5.15.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Images_rc


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.new_wtoken_buttons = []
        self.new_btoken_buttons = []

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1269, 947)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.GameBoard = QGroupBox(self.centralwidget)
        self.GameBoard.setObjectName(u"GameBoard")
        self.GameBoard.setGeometry(QRect(0, 0, 1271, 921))
        self.GameBoard.setAutoFillBackground(False)
        self.GameBoard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.GameBoard.setFlat(False)
        self.lblGameboard = QLabel(self.GameBoard)
        self.lblGameboard.setObjectName(u"lblGameboard")
        self.lblGameboard.setGeometry(QRect(30, 230, 1001, 361))
        self.lblGameboard.setCursor(QCursor(Qt.ArrowCursor))
        self.lblGameboard.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.lblGameboard.setPixmap(
            QPixmap(u":/Gameboard/Images/game20of20ur.png"))
        self.lblGameboard.setScaledContents(True)

        # ------------------ new token white button --------------------------------
        self.btnWhite1 = QPushButton(self.GameBoard)
        self.btnWhite1.setObjectName(u"btnWhite1")
        self.btnWhite1.setEnabled(True)
        self.btnWhite1.setGeometry(QRect(430, 590, 91, 81))
        self.btnWhite1.setFocusPolicy(Qt.NoFocus)
        self.btnWhite1.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnWhite1.setAcceptDrops(False)
        self.btnWhite1.setAutoFillBackground(False)
        self.btnWhite1.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 50);")
        self.white_icon = QIcon()
        self.white_icon.addFile(u":/Gameboard/Images/Blancas1.png",
                                QSize(), QIcon.Normal, QIcon.Off)
        self.btnWhite1.setIcon(self.white_icon)
        self.btnWhite1.setIconSize(QSize(75, 80))
        self.new_wtoken_buttons.append(self.btnWhite1)

        self.btnWhite2 = QPushButton(self.GameBoard)
        self.btnWhite2.setObjectName(u"btnWhite2")
        self.btnWhite2.setEnabled(True)
        self.btnWhite2.setGeometry(QRect(340, 590, 91, 81))
        self.btnWhite2.setFocusPolicy(Qt.NoFocus)
        self.btnWhite2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnWhite2.setAcceptDrops(False)
        self.btnWhite2.setAutoFillBackground(False)
        self.btnWhite2.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 50);")
        icon1 = QIcon()
        icon1.addFile(u":/Gameboard/Images/Blancas2.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btnWhite2.setIcon(icon1)
        self.btnWhite2.setIconSize(QSize(75, 80))
        self.new_wtoken_buttons.append(self.btnWhite2)

        self.btnWhite3 = QPushButton(self.GameBoard)
        self.btnWhite3.setObjectName(u"btnWhite3")
        self.btnWhite3.setEnabled(True)
        self.btnWhite3.setGeometry(QRect(250, 590, 91, 81))
        self.btnWhite3.setFocusPolicy(Qt.NoFocus)
        self.btnWhite3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnWhite3.setAcceptDrops(False)
        self.btnWhite3.setAutoFillBackground(False)
        self.btnWhite3.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 50);")
        icon2 = QIcon()
        icon2.addFile(u":/Gameboard/Images/Blancas3.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btnWhite3.setIcon(icon2)
        self.btnWhite3.setIconSize(QSize(75, 80))
        self.new_wtoken_buttons.append(self.btnWhite3)

        self.btnWhite4 = QPushButton(self.GameBoard)
        self.btnWhite4.setObjectName(u"btnWhite4")
        self.btnWhite4.setEnabled(True)
        self.btnWhite4.setGeometry(QRect(160, 590, 91, 81))
        self.btnWhite4.setFocusPolicy(Qt.NoFocus)
        self.btnWhite4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnWhite4.setAcceptDrops(False)
        self.btnWhite4.setAutoFillBackground(False)
        self.btnWhite4.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 50);")
        icon3 = QIcon()
        icon3.addFile(u":/Gameboard/Images/Blancas4.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btnWhite4.setIcon(icon3)
        self.btnWhite4.setIconSize(QSize(75, 80))
        self.new_wtoken_buttons.append(self.btnWhite4)

        self.btnWhite5 = QPushButton(self.GameBoard)
        self.btnWhite5.setObjectName(u"btnWhite5")
        self.btnWhite5.setEnabled(True)
        self.btnWhite5.setGeometry(QRect(70, 590, 91, 81))
        self.btnWhite5.setFocusPolicy(Qt.NoFocus)
        self.btnWhite5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnWhite5.setAcceptDrops(False)
        self.btnWhite5.setAutoFillBackground(False)
        self.btnWhite5.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 50);")
        icon4 = QIcon()
        icon4.addFile(u":/Gameboard/Images/Blancas5.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btnWhite5.setIcon(icon4)
        self.btnWhite5.setIconSize(QSize(75, 80))
        self.new_wtoken_buttons.append(self.btnWhite5)

        self.btnWhite6 = QPushButton(self.GameBoard)
        self.btnWhite6.setObjectName(u"btnWhite6")
        self.btnWhite6.setEnabled(True)
        self.btnWhite6.setGeometry(QRect(430, 670, 91, 81))
        self.btnWhite6.setFocusPolicy(Qt.NoFocus)
        self.btnWhite6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnWhite6.setAcceptDrops(False)
        self.btnWhite6.setAutoFillBackground(False)
        self.btnWhite6.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 50);")
        icon5 = QIcon()
        icon5.addFile(u":/Gameboard/Images/Blancas6.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btnWhite6.setIcon(icon5)
        self.btnWhite6.setIconSize(QSize(75, 80))
        self.new_wtoken_buttons.append(self.btnWhite6)

        self.btnWhite7 = QPushButton(self.GameBoard)
        self.btnWhite7.setObjectName(u"btnWhite7")
        self.btnWhite7.setEnabled(True)
        self.btnWhite7.setGeometry(QRect(340, 670, 91, 81))
        self.btnWhite7.setFocusPolicy(Qt.NoFocus)
        self.btnWhite7.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnWhite7.setAcceptDrops(False)
        self.btnWhite7.setAutoFillBackground(False)
        self.btnWhite7.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 50);")
        icon6 = QIcon()
        icon6.addFile(u":/Gameboard/Images/Blancas7.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btnWhite7.setIcon(icon6)
        self.btnWhite7.setIconSize(QSize(75, 80))
        self.new_wtoken_buttons.append(self.btnWhite7)

        # ------------------ new token black buttons --------------------------------
        self.btnBlack1 = QPushButton(self.GameBoard)
        self.btnBlack1.setObjectName(u"btnBlack1")
        self.btnBlack1.setEnabled(True)
        self.btnBlack1.setGeometry(QRect(430, 150, 91, 81))
        self.btnBlack1.setFocusPolicy(Qt.NoFocus)
        self.btnBlack1.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnBlack1.setAcceptDrops(False)
        self.btnBlack1.setAutoFillBackground(False)
        self.btnBlack1.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 50);")
        self.black_icon = QIcon()
        self.black_icon.addFile(u":/Gameboard/Images/Negras1.png",
                                QSize(), QIcon.Normal, QIcon.Off)
        self.btnBlack1.setIcon(self.black_icon)
        self.btnBlack1.setIconSize(QSize(75, 80))
        self.new_btoken_buttons.append(self.btnBlack1)

        self.btnBlack2 = QPushButton(self.GameBoard)
        self.btnBlack2.setObjectName(u"btnBlack2")
        self.btnBlack2.setEnabled(True)
        self.btnBlack2.setGeometry(QRect(340, 150, 91, 81))
        self.btnBlack2.setFocusPolicy(Qt.NoFocus)
        self.btnBlack2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnBlack2.setAcceptDrops(False)
        self.btnBlack2.setAutoFillBackground(False)
        self.btnBlack2.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 50);")
        icon9 = QIcon()
        icon9.addFile(u":/Gameboard/Images/Negras2.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btnBlack2.setIcon(icon9)
        self.btnBlack2.setIconSize(QSize(75, 80))
        self.new_btoken_buttons.append(self.btnBlack2)

        self.btnBlack3 = QPushButton(self.GameBoard)
        self.btnBlack3.setObjectName(u"btnBlack3")
        self.btnBlack3.setEnabled(True)
        self.btnBlack3.setGeometry(QRect(250, 150, 91, 81))
        self.btnBlack3.setFocusPolicy(Qt.NoFocus)
        self.btnBlack3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnBlack3.setAcceptDrops(False)
        self.btnBlack3.setAutoFillBackground(False)
        self.btnBlack3.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 50);")
        icon11 = QIcon()
        icon11.addFile(u":/Gameboard/Images/Negras3.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.btnBlack3.setIcon(icon11)
        self.btnBlack3.setIconSize(QSize(75, 80))
        self.new_btoken_buttons.append(self.btnBlack3)

        self.btnBlack4 = QPushButton(self.GameBoard)
        self.btnBlack4.setObjectName(u"btnBlack4")
        self.btnBlack4.setEnabled(True)
        self.btnBlack4.setGeometry(QRect(160, 150, 91, 81))
        self.btnBlack4.setFocusPolicy(Qt.NoFocus)
        self.btnBlack4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnBlack4.setAcceptDrops(False)
        self.btnBlack4.setAutoFillBackground(False)
        self.btnBlack4.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 50);")
        icon12 = QIcon()
        icon12.addFile(u":/Gameboard/Images/Negras4.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.btnBlack4.setIcon(icon12)
        self.btnBlack4.setIconSize(QSize(75, 80))
        self.new_btoken_buttons.append(self.btnBlack4)

        self.btnBlack5 = QPushButton(self.GameBoard)
        self.btnBlack5.setObjectName(u"btnBlack5")
        self.btnBlack5.setEnabled(True)
        self.btnBlack5.setGeometry(QRect(70, 150, 91, 81))
        self.btnBlack5.setFocusPolicy(Qt.NoFocus)
        self.btnBlack5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnBlack5.setAcceptDrops(False)
        self.btnBlack5.setAutoFillBackground(False)
        self.btnBlack5.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 50);")
        icon13 = QIcon()
        icon13.addFile(u":/Gameboard/Images/Negras5.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.btnBlack5.setIcon(icon13)
        self.btnBlack5.setIconSize(QSize(75, 80))
        self.new_btoken_buttons.append(self.btnBlack5)

        self.btnBlack6 = QPushButton(self.GameBoard)
        self.btnBlack6.setObjectName(u"btnBlack6")
        self.btnBlack6.setEnabled(True)
        self.btnBlack6.setGeometry(QRect(430, 70, 91, 81))
        self.btnBlack6.setFocusPolicy(Qt.NoFocus)
        self.btnBlack6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnBlack6.setAcceptDrops(False)
        self.btnBlack6.setAutoFillBackground(False)
        self.btnBlack6.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 50);")
        icon8 = QIcon()
        icon8.addFile(u":/Gameboard/Images/Negras6.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btnBlack6.setIcon(icon8)
        self.btnBlack6.setIconSize(QSize(75, 80))
        self.new_btoken_buttons.append(self.btnBlack6)

        self.btnBlack7 = QPushButton(self.GameBoard)
        self.btnBlack7.setObjectName(u"btnBlack7")
        self.btnBlack7.setEnabled(True)
        self.btnBlack7.setGeometry(QRect(340, 70, 91, 81))
        self.btnBlack7.setFocusPolicy(Qt.NoFocus)
        self.btnBlack7.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnBlack7.setAcceptDrops(False)
        self.btnBlack7.setAutoFillBackground(False)
        self.btnBlack7.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 50);")
        icon10 = QIcon()
        icon10.addFile(u":/Gameboard/Images/Negras7.png",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.btnBlack7.setIcon(icon10)
        self.btnBlack7.setIconSize(QSize(75, 80))
        self.new_btoken_buttons.append(self.btnBlack7)

        # ------------------------------- dice labels ----------------------------------------------
        self.lblDice1 = QLabel(self.GameBoard)
        self.lblDice1.setObjectName(u"lblDice1")
        self.lblDice1.setGeometry(QRect(1130, 280, 47, 41))
        font = QFont()
        font.setPointSize(12)
        self.lblDice1.setFont(font)
        self.btnRollDice = QPushButton(self.GameBoard)
        self.btnRollDice.setObjectName(u"btnRollDice")
        self.btnRollDice.setGeometry(QRect(1090, 170, 101, 41))
        self.btnRollDice.setFont(font)

        self.btnPassTurn = QPushButton(self.GameBoard)
        self.btnPassTurn.setObjectName(u"btnPassTurn")
        # QRect(1090, 170, 101, 41))
        self.btnPassTurn.setGeometry(QRect(1090, 220, 101, 41))
        self.btnPassTurn.setFont(font)
        self.btnPassTurn.setVisible(False)

        self.btnNewGame = QPushButton(self.GameBoard)
        self.btnNewGame.setObjectName(u"btnNewGame")
        self.btnNewGame.setGeometry(QRect(20, 30, 101, 41))
        self.btnNewGame.setFont(font)
        self.btnNewGame.setStyleSheet(u"border-color: rgb(0, 85, 255);")

        # -------------------------- 3rd row buttons -------------------------
        self.btn20 = QPushButton(self.GameBoard)
        self.btn20.setObjectName(u"btn20")
        self.btn20.setEnabled(True)
        self.btn20.setGeometry(QRect(50, 480, 101, 91))
        self.btn20.setFocusPolicy(Qt.NoFocus)
        self.btn20.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn20.setAcceptDrops(False)
        self.btn20.setAutoFillBackground(False)
        self.btn20.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn20.setIconSize(QSize(75, 80))

        self.btn21 = QPushButton(self.GameBoard)
        self.btn21.setObjectName(u"btn21")
        self.btn21.setEnabled(True)
        self.btn21.setGeometry(QRect(170, 480, 101, 91))
        self.btn21.setFocusPolicy(Qt.NoFocus)
        self.btn21.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn21.setAcceptDrops(False)
        self.btn21.setAutoFillBackground(False)
        self.btn21.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn21.setIconSize(QSize(75, 80))

        self.btn22 = QPushButton(self.GameBoard)
        self.btn22.setObjectName(u"btn22")
        self.btn22.setEnabled(True)
        self.btn22.setGeometry(QRect(290, 480, 101, 91))
        self.btn22.setFocusPolicy(Qt.NoFocus)
        self.btn22.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn22.setAcceptDrops(False)
        self.btn22.setAutoFillBackground(False)
        self.btn22.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn22.setIconSize(QSize(75, 80))

        self.btn23 = QPushButton(self.GameBoard)
        self.btn23.setObjectName(u"btn23")
        self.btn23.setEnabled(True)
        self.btn23.setGeometry(QRect(410, 480, 101, 91))
        self.btn23.setFocusPolicy(Qt.NoFocus)
        self.btn23.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn23.setAcceptDrops(False)
        self.btn23.setAutoFillBackground(False)
        self.btn23.setStyleSheet(u"background-color: rgba(255, 255, 255, 5);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn23.setIconSize(QSize(75, 80))

        self.btn26 = QPushButton(self.GameBoard)
        self.btn26.setObjectName(u"btn26")
        self.btn26.setEnabled(True)
        self.btn26.setGeometry(QRect(800, 480, 101, 91))
        self.btn26.setFocusPolicy(Qt.NoFocus)
        self.btn26.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn26.setAcceptDrops(False)
        self.btn26.setAutoFillBackground(False)
        self.btn26.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn26.setIconSize(QSize(75, 80))

        self.btn27 = QPushButton(self.GameBoard)
        self.btn27.setObjectName(u"btn27")
        self.btn27.setEnabled(True)
        self.btn27.setGeometry(QRect(920, 480, 91, 91))
        self.btn27.setFocusPolicy(Qt.NoFocus)
        self.btn27.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn27.setAcceptDrops(False)
        self.btn27.setAutoFillBackground(False)
        self.btn27.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn27.setIconSize(QSize(75, 80))

        self.btn11 = QPushButton(self.GameBoard)
        self.btn11.setObjectName(u"btn11")
        self.btn11.setEnabled(True)
        self.btn11.setGeometry(QRect(170, 370, 101, 91))
        self.btn11.setFocusPolicy(Qt.NoFocus)
        self.btn11.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn11.setAcceptDrops(False)
        self.btn11.setAutoFillBackground(False)
        self.btn11.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn11.setIconSize(QSize(75, 80))
        self.btn12 = QPushButton(self.GameBoard)
        self.btn12.setObjectName(u"btn12")
        self.btn12.setEnabled(True)
        self.btn12.setGeometry(QRect(290, 370, 101, 91))
        self.btn12.setFocusPolicy(Qt.NoFocus)
        self.btn12.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn12.setAcceptDrops(False)
        self.btn12.setAutoFillBackground(False)
        self.btn12.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn12.setIconSize(QSize(75, 80))
        self.btn00 = QPushButton(self.GameBoard)
        self.btn00.setObjectName(u"btn00")
        self.btn00.setEnabled(True)
        self.btn00.setGeometry(QRect(50, 250, 101, 91))
        self.btn00.setFocusPolicy(Qt.NoFocus)
        self.btn00.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn00.setAcceptDrops(False)
        self.btn00.setAutoFillBackground(False)
        self.btn00.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn00.setIconSize(QSize(75, 80))
        self.btn01 = QPushButton(self.GameBoard)
        self.btn01.setObjectName(u"btn01")
        self.btn01.setEnabled(True)
        self.btn01.setGeometry(QRect(170, 250, 101, 91))
        self.btn01.setFocusPolicy(Qt.NoFocus)
        self.btn01.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn01.setAcceptDrops(False)
        self.btn01.setAutoFillBackground(False)
        self.btn01.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn01.setIconSize(QSize(75, 80))
        self.btn02 = QPushButton(self.GameBoard)
        self.btn02.setObjectName(u"btn02")
        self.btn02.setEnabled(True)
        self.btn02.setGeometry(QRect(290, 250, 101, 91))
        self.btn02.setFocusPolicy(Qt.NoFocus)
        self.btn02.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn02.setAcceptDrops(False)
        self.btn02.setAutoFillBackground(False)
        self.btn02.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn02.setIconSize(QSize(75, 80))
        self.btn03 = QPushButton(self.GameBoard)
        self.btn03.setObjectName(u"btn03")
        self.btn03.setEnabled(True)
        self.btn03.setGeometry(QRect(410, 250, 101, 91))
        self.btn03.setFocusPolicy(Qt.NoFocus)
        self.btn03.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn03.setAcceptDrops(False)
        self.btn03.setAutoFillBackground(False)
        self.btn03.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn03.setIconSize(QSize(75, 80))
        self.btn06 = QPushButton(self.GameBoard)
        self.btn06.setObjectName(u"btn06")
        self.btn06.setEnabled(True)
        self.btn06.setGeometry(QRect(800, 250, 101, 91))
        self.btn06.setFocusPolicy(Qt.NoFocus)
        self.btn06.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn06.setAcceptDrops(False)
        self.btn06.setAutoFillBackground(False)
        self.btn06.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn06.setIconSize(QSize(75, 80))
        self.btn07 = QPushButton(self.GameBoard)
        self.btn07.setObjectName(u"btn07")
        self.btn07.setEnabled(True)
        self.btn07.setGeometry(QRect(920, 250, 91, 91))
        self.btn07.setFocusPolicy(Qt.NoFocus)
        self.btn07.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn07.setAcceptDrops(False)
        self.btn07.setAutoFillBackground(False)
        self.btn07.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn07.setIconSize(QSize(75, 80))
        self.btn10 = QPushButton(self.GameBoard)
        self.btn10.setObjectName(u"btn10")
        self.btn10.setEnabled(True)
        self.btn10.setGeometry(QRect(50, 370, 101, 91))
        self.btn10.setFocusPolicy(Qt.NoFocus)
        self.btn10.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn10.setAcceptDrops(False)
        self.btn10.setAutoFillBackground(False)
        self.btn10.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn10.setIconSize(QSize(75, 80))
        self.btn13 = QPushButton(self.GameBoard)
        self.btn13.setObjectName(u"btn13")
        self.btn13.setEnabled(True)
        self.btn13.setGeometry(QRect(410, 370, 101, 91))
        self.btn13.setFocusPolicy(Qt.NoFocus)
        self.btn13.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn13.setAcceptDrops(False)
        self.btn13.setAutoFillBackground(False)
        self.btn13.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn13.setIconSize(QSize(75, 80))

        self.btn14 = QPushButton(self.GameBoard)
        self.btn14.setObjectName(u"btn14")
        self.btn14.setEnabled(True)
        self.btn14.setGeometry(QRect(550, 370, 91, 81))
        self.btn14.setFocusPolicy(Qt.NoFocus)
        self.btn14.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn14.setAcceptDrops(False)
        self.btn14.setAutoFillBackground(False)
        self.btn14.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn14.setIconSize(QSize(75, 80))
        self.btn15 = QPushButton(self.GameBoard)
        self.btn15.setObjectName(u"btn15")
        self.btn15.setEnabled(True)
        self.btn15.setGeometry(QRect(670, 370, 91, 81))
        self.btn15.setFocusPolicy(Qt.NoFocus)
        self.btn15.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn15.setAcceptDrops(False)
        self.btn15.setAutoFillBackground(False)
        self.btn15.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn15.setIconSize(QSize(75, 80))
        self.btn16 = QPushButton(self.GameBoard)
        self.btn16.setObjectName(u"btn16")
        self.btn16.setEnabled(True)
        self.btn16.setGeometry(QRect(800, 360, 101, 101))
        self.btn16.setFocusPolicy(Qt.NoFocus)
        self.btn16.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn16.setAcceptDrops(False)
        self.btn16.setAutoFillBackground(False)
        self.btn16.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn16.setIconSize(QSize(75, 80))
        self.btn17 = QPushButton(self.GameBoard)
        self.btn17.setObjectName(u"btn17")
        self.btn17.setEnabled(True)
        self.btn17.setGeometry(QRect(920, 360, 91, 101))
        self.btn17.setFocusPolicy(Qt.NoFocus)
        self.btn17.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn17.setAcceptDrops(False)
        self.btn17.setAutoFillBackground(False)
        self.btn17.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(0, 0, 0);\n"
                                 "")
        self.btn17.setIconSize(QSize(75, 80))

        self.lblDice2 = QLabel(self.GameBoard)
        self.lblDice2.setObjectName(u"lblDice2")
        self.lblDice2.setGeometry(QRect(1130, 380, 47, 41))
        self.lblDice2.setFont(font)
        self.lblDice3 = QLabel(self.GameBoard)
        self.lblDice3.setObjectName(u"lblDice3")
        self.lblDice3.setGeometry(QRect(1130, 510, 47, 41))
        self.lblDice3.setFont(font)
        self.lblTotalDice = QLabel(self.GameBoard)
        self.lblTotalDice.setObjectName(u"lblTotalDice")
        self.lblTotalDice.setGeometry(QRect(1130, 620, 47, 41))
        self.lblTotalDice.setFont(font)
        self.lblTotal = QLabel(self.GameBoard)
        self.lblTotal.setObjectName(u"lblTotal")
        self.lblTotal.setGeometry(QRect(1020, 620, 87, 41))
        self.lblTotal.setFont(font)
        self.lblTurn = QLabel(self.GameBoard)
        self.lblTurn.setObjectName(u"lblTurn")
        self.lblTurn.setGeometry(QRect(600, 220, 141, 51))
        self.lblTurn.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1269, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # setup board button matrix
        self.board_buttons = [[self.btn00, self.btn01, self.btn02, self.btn03, 0, 0, self.btn06, self.btn07],
                              [self.btn10, self.btn11, self.btn12, self.btn13,
                                  self.btn14, self.btn15, self.btn16, self.btn17],
                              [self.btn20, self.btn21, self.btn22, self.btn23, 0, 0, self.btn26, self.btn27]]
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(u"MainWindow")
        self.GameBoard.setTitle(u"Gameboard")
        self.lblGameboard.setText("")
        self.btnWhite1.setText("")
        self.btnWhite2.setText("")
        self.btnWhite3.setText("")
        self.btnWhite4.setText("")
        self.btnWhite5.setText("")
        self.btnWhite6.setText("")
        self.btnWhite7.setText("")
        self.btnBlack1.setText("")
        self.btnBlack6.setText("")
        self.btnBlack2.setText("")
        self.btnBlack7.setText("")
        self.btnBlack3.setText("")
        self.btnBlack4.setText("")
        self.btnBlack5.setText("")
        self.lblDice1.setText(u"")
        self.btnRollDice.setText(u"Roll Dice")
        self.btnPassTurn.setText(u"Pass Turn")
        self.btnNewGame.setText(u"New Game")
        self.btn23.setText("")
        self.btn22.setText("")
        self.btn11.setText("")
        self.btn12.setText("")
        self.btn00.setText("")
        self.btn01.setText("")
        self.btn02.setText("")
        self.btn03.setText("")
        self.btn06.setText("")
        self.btn07.setText("")
        self.btn10.setText("")
        self.btn13.setText("")
        self.btn20.setText("")
        self.btn21.setText("")
        self.btn14.setText("")
        self.btn15.setText("")
        self.btn16.setText("")
        self.btn17.setText("")
        self.btn26.setText("")
        self.btn27.setText("")
        self.lblDice2.setText(u"")
        self.lblDice3.setText(u"")
        self.lblTotalDice.setText(u"")
        self.lblTotal.setText(u"")
        self.lblTurn.setText(u"Turn of:")
    # retranslateUi
