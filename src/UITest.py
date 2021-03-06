from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from UI import mainWindow

from game import *

class GameBoard(mainWindow.Ui_MainWindow, QMainWindow):

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
        self.set_button_handlers()
        self.lastClickedButton = ""
        self.is_game_running = False

    def clear_dice_result(self):
        self.lblTotalDice.setText('0')

    # sets the handler function for the token buttons
    def set_button_handlers(self):

        self.btnPassTurn.clicked.connect(self.pass_button_handler)
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

    def pass_button_handler(self):
        self.btnPassTurn.setVisible(False)
        self.computerTurn()

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
        self.lblDice1.setText("")
        self.lblDice2.setText("")
        self.lblDice3.setText("")

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
        self.currentGame.calculate_possible_moves()

        # if there are no possible moves, make a pass button
        if len(self.currentGame.possibleMoves) == 0:
            self.btnPassTurn.setVisible(True)

        for move in self.currentGame.possibleMoves:
            if move == self.currentGame.ADD_TOKEN_BOARD:
                self.highlight_new_wtoken_button()
            else:
                token_pos = self.currentGame.currentBoard.wTokens[move]
                button_coord = self.currentGame.W_PATH[token_pos]
                button = self.getButtonByCoord(button_coord[0], button_coord[1])

                # enable and highlight icon somehow
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
                button = self.getButtonByCoord(new_pos_coord[0], new_pos_coord[1])
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
                self.new_wtoken_buttons[new_wtoken_counter].setIcon(self.white_icon)
                new_wtoken_counter += 1

            elif wtoken_pos == 15:
                pass
            else:
                wtoken_coord = self.currentGame.W_PATH[wtoken_pos]
                button = self.getButtonByCoord(wtoken_coord[0], wtoken_coord[1])
                button.setIcon(self.white_icon)

            if btoken_pos == 0:
                self.new_btoken_buttons[new_btoken_counter].setIcon(self.black_icon)
                new_btoken_counter += 1
            elif btoken_pos == 15:
                pass
            else:
                btoken_coord = self.currentGame.B_PATH[btoken_pos]
                button = self.getButtonByCoord(btoken_coord[0], btoken_coord[1])
                button.setIcon(self.black_icon)

    def newGame(self):

        if self.is_game_running:
            cancel = self.confirm_game_cancel()
            if not cancel:
                return

        self.currentGame = Game()
        self.clear_higlights()
        self.refreshUI()

        self.activateAll()
        self.lblDice1.setText("")
        self.lblDice2.setText("")
        self.lblDice3.setText("")
        self.is_game_running = True
        self.select_player()

        if self.currentGame.currentTurn == Game.WHITE_TURN:
            self.btnRollDice.setEnabled(True)
            self.lblTurn.setText('Player\'s turn')

        else:
            # make AI move
            self.currentGame.currentState = States.AI_MOVE

            # probably thread this to avoid blocking the UI
            self.computerTurn()

    def select_player(self):
        msg = QMessageBox(self)
        msg.setText("Select player to move first")
        msg.setInformativeText("Player : white tokens (bottom)\nComp: black tokens (top)")
        msg.setWindowTitle("Player Select")

        black_button = msg.addButton("Black", QMessageBox.YesRole)
        white_button = msg.addButton("White", QMessageBox.NoRole)
        random_button = msg.addButton("Random", QMessageBox.RejectRole)

        ret = msg.exec_()
        if msg.clickedButton() == white_button:
            self.currentGame.currentTurn = Game.WHITE_TURN
        elif msg.clickedButton() == black_button:
            self.currentGame.currentTurn = Game.BLACK_TURN
        else:
            self.currentGame.set_random_player_turn()

    def confirm_game_cancel(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Would you like to start a new game?")
        msg.setInformativeText("Current progress will be lost")
        msg.setWindowTitle("Confirm New Game")
        yes_button = msg.addButton("Yes", QMessageBox.YesRole)
        msg.addButton("No", QMessageBox.NoRole)

        ret = msg.exec_()

        return msg.clickedButton() == yes_button

    def diceRolled(self):
        self.currentGame.roll_dice()
        self.btnRollDice.setEnabled(False)
        self.currentGame.currentState = States.PLAYER_MOVE

        # For testing and setting the game to a certi state
        # self.currentGame.currentBoard.bTokens = [2, 4, 1, 3, 0, 0, 0]
        # self.currentGame.currentBoard.wTokens = [15, 15, 15, 15, 15, 15, 14]

        self.activate_posible_moves()

        self.currentGame.currentBoard.print_board()

        self.lblTotal.setText('Player rolled:')
        self.lblTotalDice.setText(f'{self.currentGame.diceRollResult}')

    # handles the click of a button in the board
    def board_button_handler(self):
        btnName = self.sender().objectName()
        print("clicked board button: ", btnName)
        if self.currentGame.currentState != States.PLAYER_MOVE:
            print("It's not your turn yet, be patient")
            return
        print("clicked board button: ", btnName)
        token_id = self.getTokenIdbyBtnName(btnName)
        if token_id == -1:
            return
        if token_id not in self.currentGame.possibleMoves:
            return

        # token_id should be on the possible moves list
        self.currentGame.commit_player_action(token_id)
        self.clear_dice_result()
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
        else:
            # make AI move
            self.currentGame.currentState = States.AI_MOVE

            self.computerTurn()

    def make_ai_move(self):
        self.lblTotal.setText('AI rolled')
        self.currentGame.ai_turn(lambda s: self.lblTotalDice.setText(f'{s}'))
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
            self.lblTurn.setText('Player\'s turn')
            self.refreshUI()

    # handles the click of a button in new tokens space
    def computerTurn(self):
        self.lblTurn.setText('AI\'s turn')
        QTimer.singleShot(675, self.make_ai_move)

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
        self.currentGame.commit_player_action(self.currentGame.ADD_TOKEN_BOARD)
        self.clear_dice_result()
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
            self.lblTurn.setText('Player\'s turn')
            self.refreshUI()
        else:
            # make AI move
            self.currentGame.currentState = States.AI_MOVE

            # probably thread this to avoid blocking the UI
            self.computerTurn()

    def player_won(self):
        self.lblTurn.setText('Player has won')
        return

    def ai_won(self):
        self.lblTurn.setText('AI has won')
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

    # returns the button instance for the given coordinate
    def getButtonByCoord(self, row, column):
        return self.board_buttons[row][column]

    # returns the id of the token corresponding to the pressed button name, returns -1
    # if no token was found in the position the button was pressed
    def getTokenIdbyBtnName(self, btnName):
        pos = self.button_pos[btnName]
        return self.currentGame.currentBoard.getTokenIDWhite(pos)

if __name__ == '__main__':
    app = QApplication()
    qt_app = GameBoard()
    qt_app.show()
    app.exec_()
