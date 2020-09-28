# from token import Token


class Board:

    def __init__(self):
        self.wTokens = [0, 0, 0, 0, 0, 0, 0]
        self.bTokens = [0, 0, 0, 0, 0, 0, 0]

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

    def move_token_white(self, id, moves):
        self.wTokens[id] += moves

        return self.wTokens[id]

    def move_token_black(self, id, moves):
        self.bTokens[id] += moves

        return self.bTokens[id]

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
