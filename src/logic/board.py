# from token import Token


class Board:

    def __init__(self):
        self.wTokens = [0, 0, 0, 0, 0, 0, 0]
        self.bTokens = [0, 0, 0, 0, 0, 0, 0]

        self.ROSETTES = [4, 8, 14]
        self.landedOnRosette = False

        self.lastMovedToken = 0

    def check_win_condition(self):
        hasWin = True

        for token in self.bTokens:
            # as long as I dont find a token's pos <15 it is winning
            hasWin = hasWin and token >= 15

            # if it is no longer winning stop the verification for this player
            if not hasWin:
                break

        # if it won return it and dont verify the next player
        if hasWin:
            return hasWin, "Black"

        hasWin = True

        for token in self.wTokens:
            hasWin = hasWin and token >= 15
            if not hasWin:
                break

        if hasWin:
            return hasWin, "White"
        else:
            return hasWin, "None"

    def getTokenID(self, pos):
        for i in range(0, 7):
            if self.wTokens[i] == pos:
                return i
        # if no token was found in that position
        return -1

    # returns true if it finds a white token in the given position, false otherwise
    def isPosOccWhite(self, pos):
        for i in range(0, 7):
            if self.wTokens[i] == pos:
                return True
        return False

    # returns true if it finds a black token in the given position, false otherwise
    def isPosOccBlack(self, pos):
        for i in range(0, 7):
            if self.bTokens[i] == pos:
                return True
        return False

    def move_token(self, id, moves, player):
        if player == "black":
            new_pos = self.move_token_black(id, moves)
        else:
            new_pos = self.move_token_white(id, moves)

        return new_pos

    def move_token_white(self, id, moves):
        self.landedOnRosette = False
        self.wTokens[id] += moves

        if self.wTokens[id] in self.ROSETTES:
            self.landedOnRosette = True
        else:
            if self.wTokens[id] >= 5 and self.wTokens[id] <= 12:
                for token in range(0, len(self.wTokens)):
                    if self.wTokens[id] == self.bTokens[token]:
                        # print("Black token replaced", id, token,
                        #       self.wTokens[id], self.bTokens[token])
                        self.bTokens[token] = 0

        self.lastMovedToken = id
        return self.wTokens[id]

    def move_token_black(self, id, moves):
        self.landedOnRosette = False
        self.bTokens[id] += moves

        if self.bTokens[id] in self.ROSETTES:
            self.landedOnRosette = True
        else:
            if self.bTokens[id] >= 5 and self.bTokens[id] <= 12:
                for token in range(0, len(self.bTokens)):
                    if self.bTokens[id] == self.wTokens[token]:
                        # print("White token replaced", id, token,
                        #       self.bTokens[id], self.wTokens[token])
                        self.wTokens[token] = 0

        self.lastMovedToken = id
        return self.bTokens[id]

    def has_landed_on_rossette(self):
        return self.landedOnRosette

    # returns array of token ids that can be moved on the board, and will
    # have 10 if there are tokens available to move into the board
    def calculate_possible_moves(self, diceRoll):
        moves = []
        addedToken = False

        # checks if position 0 + dice roll is ocuppied by another player token
        canAddBoardToken = not (
            self.isPosOccWhite(diceRoll))

        # for each of the player tokens
        for token_id in range(0, len(self.wTokens)):
            token_pos = self.wTokens[token_id]

            if token_pos != 15:
                new_pos = token_pos+diceRoll
                if new_pos <= 15 and not self.isPosOccWhite(new_pos) and self.check_black_conflict(new_pos):
                    moves.append(token_id)
        return moves

    def check_black_conflict(self, pos):
        if self.isPosOccBlack(pos) and pos in self.ROSETTES:
            return False
        return True

    def remove_black_token(self, pos):
        for token in range(0, len(self.bTokens)):
            if self.bTokens[token] == pos:
                self.bTokens[token] = 0

    def print_tokens(self, tokens):
        for token in tokens:
            print(token)

    def print_board(self):
        print("White tokens:")
        for token in self.wTokens:
            print(token)

        print("Black tokens:")
        for token in self.bTokens:
            print(token)

    def getWhiteTokens(self):
        return self.wTokens

    def getBlackTokens(self):
        return self.bTokens

    def getCurrentBoard(self):
        return self.wTokens, self.bTokens

    def getLastMove(self):
        return self.lastMovedToken
