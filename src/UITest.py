from PySide2 import QtWidgets
from PySide2.QtGui import *

from UI import mainWindow

from game import *

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
        self.currentGame = Game()
        self.setupUi(self)
        self.deactivateAll()
        self.btnNewGame.clicked.connect(self.newGame)
        self.btnRollDice.clicked.connect(self.diceRolled)
        # self.btnWhite1.clicked.connect(self.movement)
        self.set_button_handlers()
        self.lastClickedButton = ""
        # self.findChild(QPushButton,)

    def clear_dice_result(self):
        self.lblTotalDice.setText('0')

    # sets the handler function for the token buttons
    def set_button_handlers(self):

        for wbutton in self.new_wtoken_buttons:
            wbutton.clicked.connect(self.wtoken_button_handler)

        for button in self.board_buttons[1]:
            if button == 0:
                pass
            else:
                button.clicked.connect(self.board_button_handler)
        for button in self.board_buttons[2]:
            if button == 0:
                pass
            else:
                button.clicked.connect(self.board_button_handler)

        # self.btn20.clicked.connect(
        #     lambda x: self.board_button_handler(self.btn20.objectName()))

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

    def activateAll(self):
        self.btnBlack1.setEnabled(True)
        self.btnBlack2.setEnabled(True)
        self.btnBlack3.setEnabled(True)
        self.btnBlack4.setEnabled(True)
        self.btnBlack5.setEnabled(True)
        self.btnBlack6.setEnabled(True)
        self.btnBlack7.setEnabled(True)

        self.btn00.setEnabled(True)
        self.btn01.setEnabled(True)
        self.btn02.setEnabled(True)
        self.btn03.setEnabled(True)
        self.btn06.setEnabled(True)
        self.btn07.setEnabled(True)

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

        self.btnWhite1.setEnabled(True)
        self.btnWhite2.setEnabled(True)
        self.btnWhite3.setEnabled(True)
        self.btnWhite4.setEnabled(True)
        self.btnWhite5.setEnabled(True)
        self.btnWhite6.setEnabled(True)
        self.btnWhite7.setEnabled(True)

        self.btnRollDice.setEnabled(True)

    def new_token_buttons_enabled(self, enable):
        self.btnWhite1.setEnabled(enable)
        self.btnWhite2.setEnabled(enable)
        self.btnWhite3.setEnabled(enable)
        self.btnWhite4.setEnabled(enable)
        self.btnWhite5.setEnabled(enable)
        self.btnWhite6.setEnabled(enable)
        self.btnWhite7.setEnabled(enable)

    def highlight_new_wtoken_button(self):
        for wbutton in self.new_wtoken_buttons:
            wbutton.setStyleSheet(u"background-color: rgba(100, 0, 255, 50);\n"
                                  "border-color: rgb(255, 0, 0); \n")

    def deactivate_board_buttons(self):
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

    def activate_posible_moves(self):
        # deactivate all buttons first
        # self.deactivate_board_buttons()
        # self.new_token_buttons_enabled(False)

        # calculate possible moves
        self.currentGame.calculate_possible_moves()

        for move in self.currentGame.possibleMoves:
            if move == self.currentGame.ADD_TOKEN_BOARD:
                # self.new_token_buttons_enabled(True)
                self.highlight_new_wtoken_button()
            else:
                token_pos = self.currentGame.currentBoard.wTokens[move]
                button_coord = self.currentGame.W_PATH[token_pos]
                button = self.getButtonByCoord(
                    button_coord[0], button_coord[1])

                # enable and highlight icon somehow
                # button.setEnabled(True)
                button.setStyleSheet(u"background-color: rgba(100, 0, 255, 50);\n"
                                     "border-color: rgb(255, 0, 0); \n")

    def highlight_move_landing(self, move):
        self.clear_higlights()

        if move == self.currentGame.ADD_TOKEN_BOARD:
            new_pos_coord = self.currentGame.W_PATH[self.currentGame.diceRollResult]
            button = self.getButtonByCoord(new_pos_coord[0], new_pos_coord[1])
            button.setStyleSheet(u"background-color: rgba(255, 0, 0, 50);")
        else:
            new_pos = self.currentGame.currentBoard.wTokens[move] + \
                self.currentGame.diceRollResult
            if new_pos < self.currentGame.END_POSITION:
                new_pos_coord = self.currentGame.W_PATH[new_pos]
                button = self.getButtonByCoord(
                    new_pos_coord[0], new_pos_coord[1])
                button.setStyleSheet(u"background-color: rgba(255, 0, 0, 50);")

    def clear_higlights(self):
        self.btn10.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn11.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn12.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn13.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn14.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn15.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn16.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn17.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")

        self.btn20.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn21.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn22.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn23.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn26.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        self.btn27.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                 "border-color: rgb(255, 0, 0);")
        for wbutton in self.new_wtoken_buttons:
            wbutton.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
                                  "border-color: rgb(255, 0, 0);")

    def refreshUI(self):
        self.delete_icons()
        self.drawIcons()

    def drawIcons(self):
        new_wtoken_counter = 0
        new_btoken_counter = 0
        for token in range(0, 7):
            wtoken_pos = self.currentGame.currentBoard.wTokens[token]
            btoken_pos = self.currentGame.currentBoard.bTokens[token]
            if wtoken_pos == 0:
                self.new_wtoken_buttons[new_wtoken_counter].setIcon(
                    self.white_icon)
                new_wtoken_counter += 1

            elif wtoken_pos == 15:
                pass
            else:
                wtoken_coord = self.currentGame.W_PATH[wtoken_pos]
                button = self.getButtonByCoord(
                    wtoken_coord[0], wtoken_coord[1])
                button.setIcon(self.white_icon)

            if btoken_pos == 0:
                self.new_btoken_buttons[new_btoken_counter].setIcon(
                    self.black_icon)
                new_btoken_counter += 1
            elif btoken_pos == 15:
                pass
            else:
                btoken_coord = self.currentGame.B_PATH[btoken_pos]
                button = self.getButtonByCoord(
                    btoken_coord[0], btoken_coord[1])
                button.setIcon(self.black_icon)

    def newGame(self):
        self.btnRollDice.setEnabled(True)
        self.lblDice1.setText("0")
        self.lblDice2.setText("0")
        self.lblDice3.setText("0")

        # self.btn00.setEnabled(False)
        # self.btn01.setEnabled(False)
        # self.btn02.setEnabled(False)
        # self.btn03.setEnabled(False)
        # self.btn06.setEnabled(False)
        # self.btn07.setEnabled(False)
        # # self.btn03.setIcon(self.white_icon)

        # self.btn10.setEnabled(False)
        # self.btn11.setEnabled(False)
        # self.btn12.setEnabled(False)
        # self.btn13.setEnabled(False)
        # self.btn14.setEnabled(False)
        # self.btn15.setEnabled(False)
        # self.btn16.setEnabled(False)
        # self.btn17.setEnabled(False)

        # self.btn20.setEnabled(False)
        # self.btn21.setEnabled(False)
        # self.btn22.setEnabled(False)
        # self.btn23.setEnabled(False)
        # self.btn26.setEnabled(False)
        # self.btn27.setEnabled(False)

        # self.btnWhite1.setEnabled(False)
        # self.btnWhite2.setEnabled(False)
        # self.btnWhite3.setEnabled(False)
        # self.btnWhite4.setEnabled(False)
        # self.btnWhite5.setEnabled(False)
        # self.btnWhite6.setEnabled(False)
        # self.btnWhite7.setEnabled(False)
        self.clear_higlights()
        self.refreshUI()
        self.activateAll()

    def diceRolled(self):
        self.currentGame.roll_dice()
        # self.currentGame.currentStatec = States.PLAYER_MOVE
        # self.currentGame.currentTurn = self.currentGame.WHITE_TURN
        self.btnRollDice.setEnabled(False)
        self.currentGame.currentState = States.PLAYER_MOVE

        # ###########################test board #####################################
        # self.currentGame.currentBoard.wTokens = [3, 0, 7, 11, 0, 10, 6]
        # self.currentGame.currentBoard.bTokens = [0, 0, 2, 9, 13, 8, 15]

        # self.drawIcons()
        self.activate_posible_moves()
        print("Dice Roll: ", self.currentGame.diceRollResult)
        print("Possible Moves: ", self.currentGame.possibleMoves)
        self.currentGame.currentBoard.print_board()
        # self.highlight_move_landing(10)
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
        self.lblTotalDice.setText(f'{self.currentGame.diceRollResult}')

    # handles the click of a button in the board
    def board_button_handler(self):
        btnName = self.sender().objectName()
        print("clicked board button: ", btnName)
        if self.currentGame.currentState != States.PLAYER_MOVE:
            print("It's not your turn yet, be patient")
            return
        print("clicked board button: ", btnName)
        self.clear_dice_result()
        token_id = self.getTokenIdbyBtnName(btnName)
        if token_id == -1:
            return
        if token_id not in self.currentGame.possibleMoves:
            return

        # token_id should be on the possible moves list
        self.currentGame.commit_player_action(token_id)
        self.clear_higlights()

        if self.currentGame.currentBoard.has_white_won():
            self.player_won()
            return
        # set the next player turn
        self.currentGame.next_turn()
        self.refreshUI()
        # if it's the player turn again
        if self.currentGame.currentTurn == self.currentGame.WHITE_TURN:
            self.currentGame.currentState = States.DICE_ROLL
            self.btnRollDice.setEnabled(True)
            # self.refreshUI()
        else:

            # make AI move
            self.currentGame.currentState = States.AI_MOVE

            # probably thread this to avoid blocking the UI
            self.computerTurn()
            # self.currentGame.currentState = States.DICE_ROLL

        # self.btnRollDice.setEnabled(True)
        # self.refreshUI()

    def computerTurn(self):
        self.currentGame.ai_turn()
        if self.currentGame.currentBoard.has_black_won():
            self.ai_won()
            return

        # set the next player turn
        self.currentGame.next_turn()

        # if it's the computer turn again
        if self.currentGame.currentTurn == self.currentGame.BLACK_TURN:
            self.refreshUI()
            self.computerTurn()
        else:
            self.currentGame.currentState = States.DICE_ROLL
            self.btnRollDice.setEnabled(True)
            self.refreshUI()

    # handles the click of a button in new tokens space

    def wtoken_button_handler(self):
        btnName = self.sender().objectName()
        print("clicked new token button: ", btnName)
        if self.currentGame.currentState != States.PLAYER_MOVE:
            print("It's not your turn yet, be patient")
            return
        # if adding a new token to the board is not an option
        if self.currentGame.ADD_TOKEN_BOARD not in self.currentGame.possibleMoves:
            return
        print("clicked new token button: ", btnName)
        self.clear_dice_result()
        self.currentGame.commit_player_action(self.currentGame.ADD_TOKEN_BOARD)
        self.clear_higlights()

        if self.currentGame.currentBoard.has_white_won():
            self.player_won()
            return
        # set the next player turn
        self.currentGame.next_turn()
        self.refreshUI()
        # if it's the player turn again
        if self.currentGame.currentTurn == self.currentGame.WHITE_TURN:
            self.currentGame.currentState = States.DICE_ROLL
            self.btnRollDice.setEnabled(True)
            # self.refreshUI()
        else:
            # make AI move
            self.currentGame.currentState = States.AI_MOVE

            # probably thread this to avoid blocking the UI
            self.computerTurn()

    def player_won(self):
        return

    def ai_won(self):
        return

    # removes all token icons from the buttons in the board

    def delete_icons(self):
        for i in range(0, 7):
            bbutton = self.new_btoken_buttons[i]
            wbutton = self.new_wtoken_buttons[i]
            bbutton.setIcon(QIcon())
            wbutton.setIcon(QIcon())
        for row in self.board_buttons:
            for button in row:
                if button == 0:
                    pass
                else:
                    button.setIcon(QIcon())

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

        # self.btn23.setStyleSheet(u"background-color: rgba(255, 0, 0, 50);")

    # returns the button instance for the given coordinate
    def getButtonByCoord(self, row, column):
        return self.board_buttons[row][column]
        # if 0 > row > 6:
        #     # error
        #     return null
        # if row == 0 and column == 5:
        #     # new token
        #     return "NEW_TOKEN"
        # if row == 0 and column == 6:
        #     # token out of board
        #     return "OUT_TOKEN"
        # # return button by name

        # return self.GameBoard.findChild(mainWindow.QPushButton, self.button_names[row][column])

    # returns the id of the token corresponding to the pressed button name, returns -1
    # if no token was found in the position the button was pressed
    def getTokenIdbyBtnName(self, btnName):
        pos = self.button_pos[btnName]
        return self.currentGame.currentBoard.getTokenIDWhite(pos)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = GameBoard()
    # btn = qt_app.getButtonByCoord(0, 0)
    # btn.setStyleSheet(u"background-color: rgba(255, 0, 0, 50);")
    # print(qt_app.getTokenIdbyBtnName("btn20"))
    qt_app.show()
    app.exec_()
