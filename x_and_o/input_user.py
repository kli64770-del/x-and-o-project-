from all_function import board,WINNING_LINES
# from all_function import 


def is_empty_index(index1):
    is_empty = False
    while not is_empty:
        if index1>9 or index1<1:
            index1=int(input("this is must to be between 1-9 press (1-9): "))

        if board[index1 - 1] == None:
            return index1
        else :
            print("this is not empty. try agian.!!")
            index1=int(input("press (1-9): "))
    



def valid_num_for_game(index1):
    is_valid = False
    while not is_valid:
        if int(index1) >= 1 and int(index1) <10:
            is_valid = True

        else:
            print("try agian...")
            index1=int(input("press agian between( 1 - 9)"))
    return index1


def check_winner(board_1,player):
    for a,b,c in WINNING_LINES:
        if board_1[a]==player and board_1[b]==player and board_1[c]==player:
            print(f"player: {player} wins!!!")
            return True




    
