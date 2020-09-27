# from token import Token


class Board:

    def __init__(self):
        self.wTokens = [0, 0, 0, 0, 0, 0, 0]
        self.bTokens = [0, 0, 0, 0, 0, 0, 0]

    def check_win_condition(self):
        hasWin = True

        for token in self.bTokens:
            # as long as I dont find a token's pos <15 it is winning
            hasWin = hasWin and token.get_pos() == 15

            # if it is no longer winning stop the verification for this player
            if not hasWin:
                break

        # if it won return it and dont verify the next player
        if hasWin:
            return hasWin, "Black"

        hasWin = True

        for token in self.wTokens:
            hasWin = hasWin and token.get_pos() == 15
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

    def exists_token_pos(self):
        return True

    def move_token(self, id, moves):
        if id > 6:
            token = self.bTokens[id-7]
        else:
            token = self.wTokens[id]

        return token.move_pos(moves)

    def print_tokens(self, tokens):
        for token in tokens:
            token.print()

    def print_board(self):
        print("White tokens:")
        self.print_tokens(self.wTokens)

        print("Black tokens:")
        self.print_tokens(self.bTokens)
