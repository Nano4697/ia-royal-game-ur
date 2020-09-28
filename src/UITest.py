from PySide2 import QtWidgets

from UI import mainWindow

import game


class GameBoard(mainWindow.Ui_MainWindow, QtWidgets.QMainWindow):

    button_names = [["btn00", "btn01", "btn02", "btn03", "new", "out", "btn06", "btn07"],
                    ["btn10", "btn11", "btn12", "btn13",
                        "btn14", "btn15", "btn16", "btn17"],
                    ["btn20", "btn21", "btn22", "btn23", "new", "out", "btn26", "btn27"]]

    button_pos = {
        "btn20": 4, "btn21": 3, "btn22": 2, "btn23": 1, "btn10": 5, "btn11": 6, "btn12": 7, "btn13": 8,
        "btn14": 9, "btn15": 10, "btn16": 11, "btn17": 12, "btn26": 14, "btn27": 13
    }

    def __init__(self):
        super(GameBoard, self).__init__()
        self.currentGame = game.Game()
        self.setupUi(self)
        self.deactivateAll()
        self.btnNewGame.clicked.connect(self.newGame)
        self.btnRollDice.clicked.connect(self.diceRolled)
        self.btnWhite1.clicked.connect(self.movement)
        # self.findChild(QPushButton,)

    def deactivateAll(self):
        self.btnBlack1.setEnabled(False)
        self.btnBlack2.setEnabled(False)
        self.btnBlack3.setEnabled(False)
        self.btnBlack4.setEnabled(False)
        self.btnBlack5.setEnabled(False)
        self.btnBlack6.setEnabled(False)
        self.btnBlack7.setEnabled(False)

        self.btn00.setEnabled(False)
        self.btn01.setEnabled(False)
        self.btn02.setEnabled(False)
        self.btn03.setEnabled(False)
        self.btn06.setEnabled(False)
        self.btn07.setEnabled(False)

        self.btn10.setEnabled(False)
        self.btn11.setEnabled(False)
        self.btn12.setEnabled(False)
        self.btn13.setEnabled(False)
        self.btn14.setEnabled(False)
        self.btn15.setEnabled(False)
        self.btn16.setEnabled(False)
        self.btn17.setEnabled(False)

        self.btn20.setEnabled(False)
        self.btn21.setEnabled(False)
        self.btn22.setEnabled(False)
        self.btn23.setEnabled(False)
        self.btn26.setEnabled(False)
        self.btn27.setEnabled(False)

        self.btnWhite1.setEnabled(False)
        self.btnWhite2.setEnabled(False)
        self.btnWhite3.setEnabled(False)
        self.btnWhite4.setEnabled(False)
        self.btnWhite5.setEnabled(False)
        self.btnWhite6.setEnabled(False)
        self.btnWhite7.setEnabled(False)

        self.btnRollDice.setEnabled(False)
        self.lblDice1.setText("0")
        self.lblDice2.setText("0")
        self.lblDice3.setText("0")

    def newGame(self):
        self.btnRollDice.setEnabled(True)
        self.lblDice1.setText("0")
        self.lblDice2.setText("0")
        self.lblDice3.setText("0")

        self.btn00.setEnabled(False)
        self.btn01.setEnabled(False)
        self.btn02.setEnabled(False)
        self.btn03.setEnabled(False)
        self.btn06.setEnabled(False)
        self.btn07.setEnabled(False)

        self.btn10.setEnabled(False)
        self.btn11.setEnabled(False)
        self.btn12.setEnabled(False)
        self.btn13.setEnabled(False)
        self.btn14.setEnabled(False)
        self.btn15.setEnabled(False)
        self.btn16.setEnabled(False)
        self.btn17.setEnabled(False)

        self.btn20.setEnabled(False)
        self.btn21.setEnabled(False)
        self.btn22.setEnabled(False)
        self.btn23.setEnabled(False)
        self.btn26.setEnabled(False)
        self.btn27.setEnabled(False)

        self.btnWhite1.setEnabled(False)
        self.btnWhite2.setEnabled(False)
        self.btnWhite3.setEnabled(False)
        self.btnWhite4.setEnabled(False)
        self.btnWhite5.setEnabled(False)
        self.btnWhite6.setEnabled(False)
        self.btnWhite7.setEnabled(False)

    def diceRolled(self):
        self.btnRollDice.setEnabled(False)

        self.btnWhite1.setEnabled(True)
        self.btnWhite2.setEnabled(True)
        self.btnWhite3.setEnabled(True)
        self.btnWhite4.setEnabled(True)
        self.btnWhite5.setEnabled(True)
        self.btnWhite6.setEnabled(True)
        self.btnWhite7.setEnabled(True)

        self.lblDice1.setText("Dado1")
        self.lblDice2.setText("Dado2")
        self.lblDice3.setText("Dado3")

    def movement(self):
        self.btn10.setEnabled(True)
        self.btn11.setEnabled(True)
        self.btn12.setEnabled(True)
        self.btn13.setEnabled(True)
        self.btn14.setEnabled(True)
        self.btn15.setEnabled(True)
        self.btn16.setEnabled(True)
        self.btn17.setEnabled(True)

        self.btn20.setEnabled(True)
        self.btn21.setEnabled(True)
        self.btn22.setEnabled(True)
        self.btn23.setEnabled(True)
        self.btn26.setEnabled(True)
        self.btn27.setEnabled(True)

        self.btn23.setStyleSheet(u"background-color: rgba(255, 0, 0, 50);")

    # returns the button instance for the given coordinate
    def getButtonByCoord(self, row, column):
        if 0 > row > 6:
            # error
            return null
        if row == 0 and column == 5:
            # new token
            return "NEW_TOKEN"
        if row == 0 and column == 6:
            # token out of board
            return "OUT_TOKEN"
        # return button by name

        return self.GameBoard.findChild(mainWindow.QPushButton, self.button_names[row][column])

    # returns the id of the token corresponding to the pressed button name, returns -1
    # if no token was found in the position the button was pressed
    def getTokenIdbyBtnName(self, btnName):
        pos = self.button_pos[btnName]
        return self.currentGame.currentBoard.getTokenID(pos)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = GameBoard()
    btn = qt_app.getButtonByCoord(0, 0)
    btn.setStyleSheet(u"background-color: rgba(255, 0, 0, 50);")
    print(qt_app.getTokenIdbyBtnName("btn20"))
    qt_app.show()
    app.exec_()
