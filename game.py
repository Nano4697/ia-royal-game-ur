from enum import Enum
from ai import *


class States(Enum):
    DICE_ROLL = 0
    PLAYER_MOVE = 1
    COMP_MOVE = 2
    END_GAME = 3


class Game:

    def __init__(self):
        self.currentTurn = None
        self.currentBoard = None
        self.currentState = States.DICE_ROLL
        self.aiAgent = AiAgent()
        self.W_PATH = [[0, 4], [0, 3], [0, 2], [0, 1], [0, 0], [1, 0], [1, 1],
                       [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [0, 7], [0, 6], [0, 5]]
        self.B_PATH = [[0, 4], [2, 3], [2, 2], [2, 1], [2, 0], [1, 0], [1, 1],
                       [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [2, 7], [2, 6], [0, 5]]
        self.ROSETTES = [4, 8, 14]
        self.diceRollResult = None
        self.possibleMoves = []

    def redraw_ui(self):
        pass

    def start_new_game(self):
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
