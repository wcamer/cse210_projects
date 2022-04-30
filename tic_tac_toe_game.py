#William Cameron Tic Tac Toe Game 


intro = 'Welcome to Tic Tac Toe.  Two players will go head to head and try to line up 3 of their symbols in a row vertically, horizonatlly or diagnally.  The first player to get 3 in a row wins!'
intro_2 = "Player one will be X and will start.  Player 2 will go second and will be using the O's."
intro_3 = 'You will see a grid and will be asked what number you would like to select and the selected spot will have the players symbol replacing the number.'
intro_4 = 'Be careful.  You are racing against the clock.  If there is no winner in 9 turns then the match ends in a draw.  Any incorrect inputs or spot stealing will result in a turn lose.'
intro_5 = 'HAVE FUN!!!'

markers = [1,2,3,4,5,6,7,8,9] #This is the creation of my place holders for my spaces in my grid.
position = markers
bomb = 9 #Bomb is a what I will use as a type of countdown that someone has to win in 9 turns or the game is over in a draw.
count_down = bomb #This variable will be what determines player 1 & 2 in addition to forcing a draw if there is no winner.
turn_counter = 0 #This is show as part of the results for the winner to show how many turns it took them to win.



def main():
    print()
    print(intro,'\n')
    print(intro_2,'\n')
    print(intro_3,'\n')
    print(intro_4,'\n')
    print(intro_5,'\n')
    print()
    print('LET THE GAME BEGIN!!!')
    while check_for_winner(position) != True and count_down >= 0: #round_counter <= 6 :# and game != 'draw':
        print()
        print()
        grid()
        player_select(count_down)
        results()
        
        

def grid(): #this will display my grid
    print(f'| {position[0]} | {position[1]} | {position[2]} |')
    print(f'| {position[3]} | {position[4]} | {position[5]} |')
    print(f'| {position[6]} | {position[7]} | {position[8]} |')
    
    
    
    
    
    
def check_for_winner(x): #this will check for the winning solution and will return true if there is, otherwise it will be false
    return (position[0] == position[1] == position[2] or
        position[3] == position[4] == position[5] or
        position[6] == position[7] == position[8] or
        position[0] == position[3] == position[6] or
        position[1] == position[4] == position[7] or
        position[2] == position[5] == position[8] or
        position[0] == position[4] == position[8] or
        position[2] == position[4] == position[6])

     
     
     
     
     
        

    
def results(): #this will check increase my turn counter, decrease my remaining turns and display results for how many turns remain, if there is a winner or, a draw.
    global count_down
    global turn_counter
    turn_counter += 1
    if check_for_winner(grid) != True:
        count_down -= 1
        if count_down > 0:
            print(count_down, 'remaining move left before draw')
            return count_down
        
        elif count_down == 0:
            print(count_down,'THIS IS THE LAST TURN')
        
        else:
            print()
            print('THIS IS MATCH ENDS IN A DRAW...')
            print()
    
    else:
        print('WINNER WINNER WINNER CHICKEN DINNER!!!!!!!!!')
        print()
        grid()
        if count_down % 2 == 1:
            print()
            print(f'Congratulations Player 1, You managed to defeat Player 2 in...{turn_counter} turns!')
            print()
            print("Can you claim victory again, in less turns?")
            print()
            
        else:
            print()
            print(f'Congratulations Player 2, You managed to defeat Player 1 in...{turn_counter} turns!')
            print()
            print("Can you  claim victory again, in less turns?")
            print()
    








def player_select(turn_count):
    if count_down % 2 == 1:  #All odd number turns will be Player 1
        print()
        choice = int(input('PLAYER 1, what position are you choosing? '))
        player_symbol_1 = 'X'    
        if acceptable_move(position[choice -1]) == True:
            print()
            print('PLAYER 1, THIS MOVE HAS BEEN PERMITTED.')
            print()
            position[choice -1] = player_symbol_1
            
        else:
            print('PLAYER 1, THIS MOVE IS UNACCEPTABLE AND YOU LOSE YOUR TURN!!!')
            
        
    
    else: #All even number turns will be player 2
        print()
        choice = int(input('PLAYER 2, what position are you choosing? '))
        player_symbol_2 = 'O'
        #position[choice -1] = player_symbol_2
        if acceptable_move(position[choice -1]) == True:
            print()
            print('PLAYER 2, THIS MOVE HAS BEEN PERMITTED.')
            print()
            position[choice -1] = player_symbol_2
            
        else:
            print()
            print('PLAYER 2, THIS MOVE IS UNACCEPTABLE AND YOU LOSE YOUR TURN!!!')
            print()
        

def acceptable_move (move): #this function will check to see if the input from player 1 or 2 is valid when the decision is made.  
    if move != 'X' and move != 'O':
        return True 
        
        
        
if __name__ == "__main__":
    main()       
        
print('Game Over')