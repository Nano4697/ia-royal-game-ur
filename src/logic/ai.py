import copy


class AiAgent:
    def __init__(self, board):
        self.open = board.getCurrentBoard()
        self.closed = []

    def expand_board(self, board, moves, player):
        posibleMoves = board.calculate_possible_moves(moves)
        boards = []

        hasAddedNewToken = False

        if player == "black":
            tokens = board.getBlackTokens()
        else:
            tokens = board.getWhiteTokens()

        for tokenToMove in posibleMoves:
            boardCopy = copy.deepcopy(board)
            currentPosOfToken = tokens[tokenToMove]

            if (currentPosOfToken == 0 and not hasAddedNewToken) or currentPosOfToken != 0:
                # print("moving token:")
                boardCopy.move_token(tokenToMove, moves, player)
                boards.append(boardCopy)

                if currentPosOfToken == 0:
                    hasAddedNewToken = True

                # boardCopy.print_board()

        return boards

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        winnerExist, winner = board.check_win_condition()
        if depth == 0 or winnerExist:
            # print("depth:", depth)
            return self.evaluate_board(board)

        if maximizingPlayer:
            maxEval = -99999

            for dice in range(1, 5):
                for child in self.expand_board(board, dice, "black"):
                    if child.has_landed_on_rossette():
                        eval = self.minimax(child, depth-1, alpha, beta, True)
                    else:
                        eval = self.minimax(child, depth-1, alpha, beta, False)

                    # Testing the influence of probability
                    if dice <= 2:
                        eval *= 0.375
                    else:
                        eval *= 0.125

                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return maxEval
        else:
            minEval = 99999

            for dice in range(1, 5):
                for child in self.expand_board(board, dice, "white"):
                    if child.has_landed_on_rossette():
                        eval = self.minimax(child, depth-1, alpha, beta, False)
                    else:
                        eval = self.minimax(child, depth-1, alpha, beta, True)

                    # Testing the influence of probability
                    if dice <= 2:
                        eval *= 0.375
                    else:
                        eval *= 0.125

                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return minEval

    def expand_possible_states(self, board_state, moves):
        succesors = []

    def calculate_next_move(self, board, diceRoll):
        board_copy = copy.deepcopy(board)

        possible_moves = self.expand_board(board_copy, diceRoll, "black")

        best_move = 0
        value = 0
        current_move = 0

        for move in possible_moves:
            evaluation = self.minimax(move, 3, -9999, 9999, True)

            # print("\t\t\t\t\tBoard value:", evaluation)

            if evaluation > value:
                best_move = current_move
                value = evaluation

            current_move += 1

        token = None
        return possible_moves[best_move-1].getLastMove()

    def evaluate_board(self, board):
        blackTokens = board.getBlackTokens()
        whiteTokens = board.getWhiteTokens()

        sum = 0

        for token in blackTokens:
            if board.has_landed_on_rossette():
                sum += 1
            sum += token
        for token in whiteTokens:
            if board.has_landed_on_rossette():
                sum += 1
            sum -= token

        return sum
