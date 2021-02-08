def print_board(board):
    print(" ",end="")
    for i in range(len(board)):
        print(f" {i}",end="")
    print()
    
    for i in range(len(board)):
        print(i, end="")
        for j in board[i]:
            if j == 0:
                print(f" _",end="")
            elif j == 1:
                print(f" X",end="")
            elif j == 2:
                print(f" 0",end="")            
        print()

def init_board(board, n):
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(0)