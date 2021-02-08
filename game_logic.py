import game_board, game_ai

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
    for i in range(len(board)):
        if board[i][0]==player and board[i][1]==player and board[i][2]==player:
            return True
        if board[0][i]==player and board[1][i]==player and board[2][i]==player:
            return True 
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        return True
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
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
            ai_move(board, game_round, player, game_ai.minimax(board, player)[1])
        else:   
            move(board, game_round, player)
        if check_win(board, player):
            print(f"Hra sa skoncila. Vyhral hrac {player}!")
            break
        player = 2 if player == 1 else 1
        game_round += 1
        if game_round == 10:
            print(f"Hra sa skoncila remizou!")
            break
                