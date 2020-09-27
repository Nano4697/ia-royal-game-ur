from enum import Enum
from ai import *
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
        self.aiAgent = AiAgent()
        self.diceRollResult = None
        self.possibleMoves = []
        self.hasFinished = False
        self.repeatTurn = False

    def __init__(self):
        self.ROSETTES = [4, 8, 14]

        self.W_PATH = [[0, 4], [0, 3], [0, 2], [0, 1], [0, 0], [1, 0], [1, 1],
                       [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [0, 7], [0, 6], [0, 5]]
        self.B_PATH = [[0, 4], [2, 3], [2, 2], [2, 1], [2, 0], [1, 0], [1, 1],
                       [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [2, 7], [2, 6], [0, 5]]
        self.start_new_game()

    def redraw_ui(self):
        pass

    # returns array of token ids that can be moved on the board, and will
    # have 10 if there are tokens available to move into the board
    def calculate_possible_moves(self):
        moves = []
        playerTokens = self.currentBoard.wTokens
        addedToken = False

        # checks if position 0 + dice roll is ocuppied by another player token
        canAddBoardToken = !(self.currentBoard.isPosOccWhite(diceRollResult))

        # for each of the player tokens
        for token_id in range(0, 7):
            token_pos = playerTokens[token_id]

            if token_pos == 0 and !(addedToken) and canAddBoardToken:
                addedToken = True
                moves.append(10)  # add 10 to signify new move only once
            # if the token is in the board
            elif token_pos != 0 and token_pos != 15:
                new_pos = token_pos+diceRollResult
                if new_pos <= 15 and !(self.currentBoard.isPosOccWhite(new_pos)):
                    moves.append(token_id)
        self.possibleMoves = moves

    def ai_turn(self, board):
        pass

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
        # probability of getting it = 3/8 -> 37.5 -> [625,99[
        elif randomValue < 1000:
            return 2

    def move_token(self, id, moves):
        resultPos = self.currentBoard.move_token(id, moves)

        return resultPos

    def next_turn(self):
        if self.currentTurn == "Black":
            if not self.repeatTurn:
                self.currentTurn = "White"
        else:
            if not self.repeatTurn:
                self.currentTurn = "Black"

        self.repeatTurn = False

    def print_board(self):
        self.currentBoard.print_board()

    def next_state(self):
        nextValue = (self.currentState.value + 1) % (States.END_GAME.value + 1)

        self.currentState = States(nextValue)
        print("Current state:", self.currentState.name)

    def restart_state(self):
        self.currentState = States.DICE_ROLL
        print("Current state:", self.currentState.name)

    def game(self, firstPlayer="Black"):
        self.start_new_game(firstPlayer)

        turns = 0
        while not self.hasFinished:
            # ---------------- ROLL DICE -------------
            input("Press Enter to roll dice...")
            self.restart_state()
            dice = self.roll_dice()

            self.repeatTurn = True
            # ---------------- PLAYER MOVE --------------
            while self.repeatTurn:
                self.repeatTurn = False
                self.next_state()

                newPos = self.move_token(turns % 7, dice)

                if newPos in self.ROSETTES:
                    self.repeatTurn = True

                    self.restart_state()
                    input("Press Enter to roll dice...")
                    dice = self.roll_dice()

            self.next_turn()
            self.next_state()

            self.repeatTurn = True

            # ---------------- AI MOVE --------------
            while self.repeatTurn:
                self.repeatTurn = False
                newPos = self.move_token((turns % 7) + 7, dice)

                if newPos in self.ROSETTES:
                    self.repeatTurn = True
                    dice = self.roll_dice()

            if turns == 100:
                self.start_new_game(self.currentTurn)

            self.hasFinished, winner = self.currentBoard.check_win_condition()
            turns += 1

        # --------------- END GAME -------------------
        self.next_state()
        self.print_board()
        print("Winner is:", winner)


# def main():
#     game = Game()

#     game.game()


# if __name__ == "__main__":
#     main()
