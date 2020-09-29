from enum import Enum
from ai import AiAgent
from board import Board
import random


class States(Enum):
    DICE_ROLL = 0
    PLAYER_MOVE = 1
    AI_MOVE = 2
    END_GAME = 3


class Game:
    def start_new_game(self, firstPlayer="Black"):
        self.currentBoard = Board()
        self.currentTurn = firstPlayer
        self.hasFinished = False
        self.repeatTurn = False

        self.currentState = States.DICE_ROLL
        self.aiAgent = AiAgent(self.currentBoard)
        self.diceRollResult = None
        self.possibleMoves = []
        self.hasFinished = False
        self.repeatTurn = False
        self.dice = 0

    def __init__(self):
        self.ROSETTES = [4, 8, 14]

        self.W_PATH = [[0, 4], [0, 3], [0, 2], [0, 1], [0, 0], [1, 0], [1, 1],
                       [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [0, 7], [0, 6], [0, 5]]
        self.B_PATH = [[0, 4], [2, 3], [2, 2], [2, 1], [2, 0], [1, 0], [1, 1],
                       [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [2, 7], [2, 6], [0, 5]]
        self.start_new_game()

    def redraw_ui(self):
        pass

    def calculate_possible_moves(self):
        self.possibleMoves = self.currentBoard.calculate_possible_moves(
            self.diceRollResult)

    def check_black_conflict(self, pos):
        if self.currentBoard.isPosOccBlack(pos) and pos in self.ROSETTES:
            return False
        return True

    def ai_turn(self):
        return self.aiAgent.calculate_next_move(
            self.currentBoard, self.diceRollResult)

    def roll_dice(self):
        randomValue = random.randint(0, 999)

        # check if result == 1
        # probability of getting it = 3/8 -> 37.5 -> [0,375[
        if 0 <= randomValue < 375:
            return 1

        # check if result == 3
        # probability of getting it = 1/8 -> 12.5 -> [375,500[
        elif 375 <= randomValue < 500:
            return 3

        # check if result == 4
        # probability of getting it = 1/8 -> 12.5 -> [500,625[
        elif 500 <= randomValue < 625:
            return 4

        # check if result == 2
        # probability of getting it = 3/8 -> 37.5 -> [625,999[
        elif randomValue < 1000:
            return 2

    def move_token_white(self, id, moves):
        resultPos = self.currentBoard.move_token_white(id, moves)

        self.currentBoard.remove_black_token(resultPos)

        return resultPos

    def move_token_black(self, id, moves):
        resultPos = self.currentBoard.move_token_black(id, moves)

        return resultPos

    def next_turn(self):
        if self.currentTurn == "Black":
            if not self.repeatTurn:
                self.currentTurn = "White"
        else:
            if not self.repeatTurn:
                self.currentTurn = "Black"

        self.repeatTurn = False

    def next_state(self):
        nextValue = (self.currentState.value + 1) % (States.END_GAME.value + 1)

        self.currentState = States(nextValue)
        print("Current state:", self.currentState.name)

    def restart_state(self):
        self.currentState = States.DICE_ROLL
        print("Current state:", self.currentState.name)

    def should_skip_turn(self):
        return len(self.possibleMoves) == 0

    def game(self, firstPlayer="Black"):
        self.start_new_game(firstPlayer)

        turns = 0
        while not self.hasFinished:
            # ---------------- ROLL DICE -------------
            input("Press Enter to roll dice...")
            self.restart_state()
            self.diceRollResult = self.roll_dice()
            print("\tDice result: ", self.diceRollResult)

            self.repeatTurn = True
            # ---------------- PLAYER MOVE --------------
            while self.repeatTurn:
                self.repeatTurn = False
                self.next_state()

                self.calculate_possible_moves()

                self.ask_token_to_move()

                userInput = input("Move token:")
                while not userInput.isdigit():
                    userInput = input("Move token:")

                tokenToMove = int(userInput)

                newPos = self.currentBoard.move_token_white(
                    tokenToMove, self.diceRollResult)

                if newPos in self.ROSETTES:
                    self.repeatTurn = True

                    self.restart_state()
                    input("Press Enter to roll dice...")
                    self.diceRollResult = self.roll_dice()
                    print("\tDice result: ", self.diceRollResult)

            self.next_turn()
            self.next_state()

            self.repeatTurn = True

            # ---------------- AI MOVE --------------
            while self.repeatTurn:
                self.diceRollResult = self.roll_dice()
                print("\tDice result: ", self.diceRollResult)

                self.repeatTurn = False

                tokenToMove = self.ai_turn()
                print("\t\t\tToken moved:", tokenToMove)
                newPos = self.currentBoard.move_token_black(
                    tokenToMove, self.diceRollResult)

                if newPos in self.ROSETTES:
                    self.repeatTurn = True

            if turns == 100:
                self.start_new_game(self.currentTurn)

            self.hasFinished, winner = self.currentBoard.check_win_condition()
            turns += 1

            self.print_board()

        # --------------- END GAME -------------------
        self.next_state()
        self.print_board()
        print("Winner is:", winner)

    # temporal functions - just testing ------------------------------------------------------------------
    def ask_token_to_move(self):
        for token in self.possibleMoves:
            if token == 10:
                print("Press enter to add new token")
            else:
                print(token, ") To move token", token)

    def print_board(self):
        board = [["   "]*8, ["   "]*8, ["   "]*8]

        whiteTokens = self.currentBoard.getWhiteTokens()
        for token in range(0, len(whiteTokens)):
            token_id = whiteTokens[token]
            if token_id < 15:
                token_pos = self.W_PATH[token_id]

                row = token_pos[0]
                column = token_pos[1]

                board[row][column] = " " + str(token) + " "

        blackTokens = self.currentBoard.getBlackTokens()
        for token in range(0, len(blackTokens)):
            token_id = blackTokens[token]
            if token_id < 15:
                token_pos = self.B_PATH[token_id]

                row = token_pos[0]
                column = token_pos[1]

                board[row][column] = "*" + str(token) + "*"

        for i in range(0, len(board)):
            row_cell = ""
            for j in range(0, len(board[i])):
                if j < 4 or j > 5 or i == 1:
                    row_cell += "[" + str(board[i][j]) + "]"
                else:
                    row_cell += "     "
            print(row_cell)


def main():
    game = Game()

    # game.print_board()
    game.game()


if __name__ == "__main__":
    main()
