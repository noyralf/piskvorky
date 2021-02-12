import game_board, game_ai
import math
import timeit

class NotEmptyError(Exception):
    pass

def move(board, game_round, player):
    print(f"Vitajte v kole {game_round}. Teraz je na rade hrac {player}.")    
    while True:
        try:
            x, y = map(int, input("Zadaj suradnice svojho tahu, X medzera Y:").split())
            if x < 0 or y < 0:
                raise IndexError
            if board[y][x] != 0:
                raise NotEmptyError
            board[y][x] = player
            break
        except ValueError:
            print("Zadal si nespravne suradnice, skus to znova!")
        except IndexError:
            print("Zadal si suradnice mimo pola, skus to znova!") 
        except NotEmptyError:
            print("Zadal si obsadene suradnice, skus to znova!")            
    game_board.print_board(board)

def check_win(board, player):
    lb = len(board)
    for i in (range(lb)):
        if all([x==player for x in board[i]]):
            return True
        if all([board[y][i]==player for y in range(lb)]):
            return True
    if all([board[i][i]==player for i in range(lb)]):
        return True
    if all([board[lb - 1 - i][i]==player for i in range(lb)]):
        return True
    return False

def ai_move(board, game_round, player, move):
    print(f"Vitajte v kole {game_round}. Teraz je na rade hrac {player}. Hrac isiel na poziciu {move}")
    board[move[1]][move[0]] = player
    game_board.print_board(board)
            
def play(board):
    player = 1
    game_round = 1
    while True:
        if player == 2:
            start_time = timeit.default_timer()
            ai_move(board, game_round, player, game_ai.ab_cached(board, player, -math.inf, math.inf)[1])
            #ai_move(board, game_round, player, game_ai.minimax_ab(board, player, -math.inf, math.inf)[1])
            #ai_move(board, game_round, player, game_ai.minimax(board, player)[1])
            print("Cas AI:", timeit.default_timer() - start_time)
        else:   
            move(board, game_round, player)
        if check_win(board, player):
            print(f"Hra sa skoncila. Vyhral hrac {player}!")
            break
        player = 2 if player == 1 else 1
        game_round += 1
        if game_round == len(board)**2 + 1:
            print(f"Hra sa skoncila remizou!")
            break
                