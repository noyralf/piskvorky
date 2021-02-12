import game_logic
import math

memoized_values = {}
flatten = lambda t: [item for sublist in t for item in sublist]

def ab_cached(board, player, alfa, beta):
    global memoized_values
    fboard = tuple(flatten(board))
    if fboard in memoized_values:
        val, a, b = memoized_values[fboard]
        if a<=alfa and beta<=b:
            return val
        else:
            alfa = min(alfa, a)
            beta = max(beta, b)
            val = minimax_ab(board, player, alfa, beta)
            memoized_values[fboard] = val, alfa , beta
            return val
    else:
        val = minimax_ab(board, player, alfa, beta)
        memoized_values[fboard] = val, alfa , beta
        return val     

def minimax_ab(board, player, alfa, beta):   
    chosen_move = -1    
    if end_state(board):
        return (state_score(board), chosen_move)
    if player == 1:
        value = -math.inf
        for move in available_moves(board):
            board[move[1]][move[0]] = 1
            new_value = ab_cached(board, 2, alfa, beta)[0]
            board[move[1]][move[0]] = 0
            if (new_value > value):
                value = new_value
                chosen_move = move
            alfa = max(alfa, value)
            if alfa >= beta:
                break
        return (value, chosen_move)
    if player == 2:
        value = math.inf
        for move in available_moves(board):
            board[move[1]][move[0]] = 2
            new_value = ab_cached(board, 1, alfa, beta)[0]
            board[move[1]][move[0]] = 0
            if (new_value < value):
                value = new_value
                chosen_move = move
            beta = min(beta, value)
            if beta <= alfa:
                break 
        return (value, chosen_move) 

def minimax(board, player):    
    try:
        return memoized_values[tuple(flatten(board))]
    except:
        pass
    chosen_move = -1
    if end_state(board):
        return (state_score(board), chosen_move)
    if player == 1:
        value = -math.inf
        for move in available_moves(board):
            board[move[1]][move[0]] = 1
            new_value = minimax(board, 2)[0]
            board[move[1]][move[0]] = 0
            if (new_value > value):
                value = new_value
                chosen_move = move
        memoized_values[tuple(flatten(board))] = (value, chosen_move)
        return (value, chosen_move)
    if player == 2:
        value = math.inf
        for move in available_moves(board):
            board[move[1]][move[0]] = 2
            new_value = minimax(board, 1)[0]
            board[move[1]][move[0]] = 0
            if (new_value < value):
                value = new_value
                chosen_move = move
        memoized_values[tuple(flatten(board))] = (value, chosen_move)
        return (value, chosen_move)    

def available_moves(board):
    moves = []
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 0:
                moves.append((x, y))
    return moves

def state_score(board):
    if game_logic.check_win(board, 1):
        return 10
    elif game_logic.check_win(board, 2):
        return -10
    else:
        return 0

def end_state(board):
    if state_score(board) != 0 or all(board[y][x]!=0 for x in range(len(board)) for y in range(len(board))):
    #if state_score(board) != 0 or len(available_moves(board)) == 0:
        return True
    else:
        return False
    