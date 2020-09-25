from enum import Enum
from ai import *
from board import Board


class States(Enum):
    DICE_ROLL = 0
    PLAYER_MOVE = 1
    COMP_MOVE = 2
    END_GAME = 3


class Game:
    def start_new_game(self, firstPlayer="Black"):
        self.currentBoard = Board()
        self.currentTurn = firstPlayer
        self.hasFinished = False
        self.repeatTurn = False

        self.W_PATH = [[0, 4], [0, 3], [0, 2], [0, 1], [0, 0], [1, 0], [1, 1],
                       [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [0, 7], [0, 6], [0, 5]]
        self.B_PATH = [[0, 4], [2, 3], [2, 2], [2, 1], [2, 0], [1, 0], [1, 1],
                       [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [2, 7], [2, 6], [0, 5]]

        self.currentState = States.DICE_ROLL
        self.aiAgent = AiAgent()
        self.diceRollResult = None
        self.possibleMoves = []
        self.hasFinished = False
        self.repeatTurn = False

    def __init__(self):
        self.ROSETTES = [4, 8, 14]

    def redraw_ui(self):
        pass

    def calculate_possible_moves(self):
        tokens = []
        return tokens

    def ai_turn(self, board):
        pass

    def roll_dice(self):
        pass

    def move_token(self, id, moves):
        pass

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

    def game(self, firstPlayer="Black"):
        self.start_new_game(firstPlayer)

        turns = 0
        while not self.hasFinished and turns < 10:
            print("turn:", turns, self.currentTurn)
            if turns == 5:
                self.repeatTurn = True
            self.next_turn()
            turns += 1


def main():
    game = Game()

    game.game()


if __name__ == "__main__":
    main()
