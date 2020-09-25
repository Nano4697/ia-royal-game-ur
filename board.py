from token import Token


class Board:

    def __init__(self):
        self.wTokens = []
        self.bTokens = []

        for id in range(7):
            self.wTokens.append(Token(id))

        for id in range(7, 14):
            self.bTokens.append(Token(id))

    def check_win_condition(self):
        return True

    def exists_token_pos(self):
        return True

    def print_tokens(self, tokens):
        for token in tokens:
            token.print()

    def print_board(self):
        print("White tokens:")
        self.print_tokens(self.wTokens)

        print("Black tokens:")
        self.print_tokens(self.bTokens)
