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

    # Returns the id of the first token with the given position
    def getTokenIDWhite(self, pos):
        for i in range(0, 7):
            if self.wTokens[i] == pos:
                return i
        # if no token was found in that position
        return -1

    # Returns the id of the first token with the given position
    def getTokenIDBlack(self, pos):
        for i in range(0, 7):
            if self.bTokens[i] == pos:
                return i
        # if no token was found in that position
        return -1

    # returns true if it finds a white token in the given position, false otherwise
    def isPosOccWhite(self, pos):
        for i in range(0, 7):
            curr_pos = self.wTokens[i]
            if curr_pos != 0 and curr_pos != 15:
                if curr_pos == pos:
                    return True
        return False

    # returns true if it finds a black token in the given position, false otherwise
    def isPosOccBlack(self, pos):
        for i in range(0, 7):
            curr_pos = self.bTokens[i]
            if curr_pos != 0 and curr_pos != 15:
                if curr_pos == pos:
                    return True
        return False

    # moves token to new position and updates opposing player's tokens in case of moving to the sane tile

    def move_token_white(self, id, moves):
        if 0 >= id >= 6:
            print("error en move token white, id incorrecto")
            return
        new_pos = self.wTokens[id] + moves
        if new_pos > 15:
            print("error en move token white, movimiento invalido")
            return
        self.wTokens[id] = new_pos
        return new_pos

    # moves token to new position and updates opposing player's tokens in case of moving to the sane tile
    def move_token_black(self, id, moves):
        if 0 > id > 6:
            print("error en move token white, id incorrecto")
            return
        new_pos = self.bTokens[id] + moves
        if new_pos > 15:
            print("error en move token white, movimiento invalido")
            return
        self.bTokens[id] = new_pos
        return new_pos

    def print_tokens(self, tokens):
        for token in tokens:
            token.print()

    def print_board(self):
        print("White tokens:")
        print(self.wTokens)

        print("Black tokens:")
        print(self.bTokens)
