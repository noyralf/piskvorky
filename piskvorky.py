import game_logic
import game_board

def main():
    print("Vitajte v hre piskvorky!")
    n = int(input("Zadaj velkost plochy:"))
    
    board = []
    game_board.init_board(board, n)
    game_board.print_board(board)
    
    game_logic.play(board)
    print("Stlac Enter pre koniec...")
    input()

if __name__ == "__main__":
    main()