def board_game():
    global board
    board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")
def game():
    board_game()
    player1=input("enter Your name=")
    player2=input("enter your name=")
    mark1="X"#mark of player1
    mark2="O"#mark of player2
    current_player=player1
    current_mark=mark1
    while True:
        pos_1=int(input("Enter nunmber between 0 to 2="))
        pos_2=int(input("Enter number between 0 to 2="))
        if(board[pos_1][pos_2]==mark1 or board[pos_1][pos_2]==mark2):
            print("This is invalid position,Choose another position")
        else:
            board[pos_1][pos_2]=current_mark
        flat_board=[cell for row in board for cell in row]
        print(flat_board)
        win_cond=[[0,1,2],[3,4,5],[6,7,8],
             [0,3,6],[1,4,7],[2,5,8],
             [0,4,8],[2,4,6]]
        for i in win_cond:
            if(flat_board[i[0]]==flat_board[i[1]]==flat_board[i[2]]==mark1):
                print("player",player1,"won")
                return
            elif(flat_board[i[0]]==flat_board[i[1]]==flat_board[i[2]]==mark2):
                print("player",player2,"won")
                return
        if all( cell in [mark1,mark2] for cell in flat_board):
            print("match is draw")
            return
        if(current_player==player1):
            current_player=player2
            current_mark=mark2
        else:
            current_player=player1
            current_mark=mark1        
        
game()