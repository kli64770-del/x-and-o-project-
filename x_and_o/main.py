from all_function import board
from input_user import is_empty_index,valid_num_for_game,check_winner

def show_board():
    print(f"""
                [1]{board[0]} | [2]{board[1]} | [3]{board[2]}
                ----+------+------
                [4]{board[3]} | [5]{board[4]} | [6]{board[5]}
                ----+------+------
                [7]{board[6]} | [8]{board[7]} | [9]{board[8]} """)
    
   

def main():
    global board
    is_finish=False
    count_o=0
    count_x_o=0 
    
    while not is_finish:      
        show_board()
        print("x's turn.")

        choise_user=valid_num_for_game(int(input("please enter num between (1-9): ")))
        choise_user
        choose2=is_empty_index(choise_user)
        board[choose2 -1] ="x"
        winner1=check_winner(board,"x")
        if winner1 == True:
            
            show_board()
            break
   
        if all(board):
            show_board()
            print("it is draw!!!!")
            
            break

        show_board()
        print("o's turn.")
        choise_user = valid_num_for_game(int(input("please enter num between (1-9): ")))
        
        coose2=is_empty_index(choise_user)
    
        board[ int(coose2) -1 ] = "o"
        wineer=check_winner(board,"o")

        if wineer == True:
            show_board()
            break

        continue

    print("\ndone!!!!!")

main()


