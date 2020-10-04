import copy


class AiAgent:
    def __init__(self, game):
        self.game = game
        self.open = game.currentBoard
        self.closed = []

    def expand_board(self, game, moves, player):
        gameCopy = copy.deepcopy(game)
        boards = []
        gameCopy.diceRollResult = moves
        gameCopy.set_next_turn()
        posibleMoves = gameCopy.calculate_possible_moves()

        hasAddedNewToken = False

        # if player == "black":
        #     tokens = board.getBlackTokens()
        # else:
        #     tokens = board.getWhiteTokens()
        for tokenToMove in posibleMoves:
            childCopy = copy.deepcopy(gameCopy)

            childCopy.commit_player_action(tokenToMove)
            boards.append(childCopy)
            # currentPosOfToken = tokens[tokenToMove]

            # if (currentPosOfToken == 0 and not hasAddedNewToken) or currentPosOfToken != 0:
            #     # print("moving token:")
            #     gameCopy.move_token(tokenToMove, moves, player)
            #     boards.append(boardCopy)

            #     if currentPosOfToken == 0:
            #         hasAddedNewToken = True

            #     # boardCopy.print_board()

        return boards

    def minimax(self, game, depth, alpha, beta, maximizingPlayer):
        winnerExist, winner = game.currentBoard.check_win_condition()

        # if I reach the end return the evaluation of that state
        if depth == 0 or winnerExist:
            evaluation = self.evaluate_board(game)
            # print("\t"*(4-depth), "- child evaluation:", evaluation)
            return evaluation

        # maximize
        if maximizingPlayer:
            maxEval = -99999

            # iterate over the possible dice's outcomes
            for dice in range(1, 5):
                # expand the possible moves for that dice outcome
                for child in self.expand_board(game, dice, "black"):
                    maximize = child.repeatTurn
                    # child.set_next_turn()

                    if maximize:
                        eval = self.minimax(child, depth, alpha, beta, True)
                        # print("repeat turn", eval)
                    else:
                        eval = self.minimax(child, depth-1, alpha, beta, False)

                    if child.diceRollResult <= 2:
                        eval *= 0.75
                    else:
                        eval *= 0.25

                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            # print("\t"*(3-depth), "max chosen:", maxEval)
            return maxEval

        # minimize
        else:
            minEval = 99999

            for dice in range(1, 5):
                for child in self.expand_board(game, dice, "white"):
                    minimize = child.repeatTurn
                    # child.set_next_turn()

                    if minimize:
                        eval = self.minimax(child, depth, alpha, beta, False)
                        # print("repeat turn", eval)
                    else:
                        eval = self.minimax(child, depth-1, alpha, beta,  True)

                    if child.diceRollResult <= 2:
                        eval *= 0.75
                    else:
                        eval *= 0.25

                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            # print("\t"*(3-depth), "min chosen:", minEval)
            return minEval

    def expand_possible_states(self, board_state, moves):
        succesors = []

    def calculate_next_move(self, game, diceRoll):
        game_copy = copy.deepcopy(game)

        possible_moves = self.expand_board(game_copy, diceRoll, "black")

        best_move = 0
        value = 9999
        alpha = -9999
        beta = 9999
        current_move = 0
        # print("------------- Calculating move - BEGIN ----------------")
        for move in possible_moves:
            if move.repeatTurn:
                evaluation = self.minimax(move, 2, alpha, beta, True)
            else:
                evaluation = self.minimax(move, 2, alpha, beta, False)

            # print("parent evaluation:", evaluation)

            # print("\t\t\t\t\tBoard value:", evaluation)

            if evaluation > value:
                best_move = current_move
                value = evaluation

            alpha = max(alpha, value)

            current_move += 1
        # print("-------------- Calculating move - END -----------------")

        # print("chose value:", value)
        token = None
        if len(possible_moves) == 0:
            return -1
        return possible_moves[best_move-1].currentBoard.getLastMove()

    def evaluate_board(self, game):
        blackTokens = game.currentBoard.getBlackTokens()
        whiteTokens = game.currentBoard.getWhiteTokens()

        sum = 0

        for token in blackTokens:
            if token in game.ROSETTES and 5 <= token <= 12:
                sum += 3
            if token == 15:
                sum += 5
            sum += token

        if game.currentTurn == game.BLACK_TURN and game.currentBoard.ateToken:
            sum += 5
        # # if game.currentTurn == game.BLACK_TURN and game.currentBoard.landedOnRosette:
        # #     sum += 3
        if game.currentTurn == game.BLACK_TURN and game.currentBoard.tokenExited:
            sum += 10

        for token in whiteTokens:
            if token in game.ROSETTES and 5 <= token <= 12:
                sum -= 3
            if token == 15:
                sum -= 5
            sum -= token

        if game.currentTurn == game.WHITE_TURN and game.currentBoard.ateToken:
            sum -= 5
        # if game.currentTurn == game.WHITE_TURN and game.currentBoard.landedOnRosette:
        #     sum -= 3
        if game.currentTurn == game.WHITE_TURN and game.currentBoard.tokenExited:
            sum -= 10

        # if game.diceRollResult <= 2:
        #     sum *= 0.75
        # else:
        #     sum *= 0.25

        return sum

    # def evaluate_board(self, game):
    #     blackTokens = game.currentBoard.getBlackTokens()
    #     whiteTokens = game.currentBoard.getWhiteTokens()

    #     sum = 0

    #     for token in blackTokens:
    #         # if token in game.ROSETTES:
    #         #     sum += 3
    #         if token == 15:
    #             sum += 1
    #         sum += token

    #     # if game.currentTurn == game.BLACK_TURN and game.currentBoard.ateToken:
    #     #     sum += 1
    #     # # if game.currentTurn == game.BLACK_TURN and game.currentBoard.landedOnRosette:
    #     # #     sum += 3
    #     # if game.currentTurn == game.BLACK_TURN and game.currentBoard.tokenExited:
    #     #     sum += 10

    #     for token in whiteTokens:
    #         #     # if token in game.ROSETTES:
    #         #     #     sum -= 3
    #         if token == 15:
    #             sum -= 5
    #         sum -= token

    #     if game.currentTurn == game.WHITE_TURN and game.currentBoard.ateToken:
    #         sum -= 5
    #     # if game.currentTurn == game.WHITE_TURN and game.currentBoard.landedOnRosette:
    #     #     sum -= 3
    #     if game.currentTurn == game.WHITE_TURN and game.currentBoard.tokenExited:
    #         sum -= 10

    #     if game.diceRollResult <= 2:
    #         sum *= 0.75
    #     else:
    #         sum *= 0.25

    #     return -sum