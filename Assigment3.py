#----------------------------------------------------
# Assignment 3: main.py 
# Assigment Focuses: Refresher of Python and hands-on experience with algorithm coding, input validation, exceptions, Stack, Queue, and data structures with encapsulation
# 
# Author: Chidinma Amogu
#----------------------------------------------------

# importing the needed classes
from AbacoStack import Card
from AbacoStack import AbacoStack


def main():
    
    play_again = True
    win = False
    
    while play_again:
        # creating an empty list to gather all the possible moves for every different game in order to do input validation        
        possible_moves = []        
        s_valid = False
        while not s_valid:
            stacks = input('Please enter the number of stacks between 2 and 5: ')
            if len(stacks.strip()) == 0:
                print('Error: Invalid Input')
            
            else:
                try:
                    stacks = int(stacks)
                except ValueError:
                    print('Error: Invalid Input')
                    
                if stacks <= 5 and stacks >= 2:
                    s_valid = True
                else:
                    print('Error: Invalid Number.')
            
            
            d_valid = False
            while not d_valid:
                depth = input('Please enter the depth of stacks between 2 and 4: ')
                if len(depth.strip()) == 0:
                    print('Error: Invalid Input')
                
                else:
                    try:
                        depth = int(depth)
                        
                    except ValueError:
                        print('Error: Invalid Input')
                        
                    if depth <= 4 and depth >= 2:
                        d_valid = True
                    else:
                        print('Error: Invalid Number.') 
            
            for i in range(stacks + 2):
                if i > 0 and i < (stacks +2) - 1:
                    for movement in 'udlr':
                        possible_moves.append(str(i) + movement)
                else:
                    for movement in 'lr':
                        possible_moves.append(str(i) + movement)
                        
        game = AbacoStack(stacks, depth)
        card = Card(stacks, depth)
        card.reset()    
        playing = True
        
        while playing:
            game.show(card)        
            move = input('Enter your move(s) [Q for quit and R to reset]: ')
            move = move.strip()
            move = move.replace(' ', '')
            if len(move) == 0:
                print('Invalid Input')
            elif move[0].upper() == 'Q':
                playing = False
                
            elif move[0].upper() == 'R':
                game.reset()
                
            else:
                try:
                    if len(move) == 2:
                        if move.lower() in possible_moves:
                            game.moveBead(move.lower())
                        else:
                            print('Invalid Move')
                    else:
                            
                        move = move.replace(' ', '')
                        move_list = list(move)
                        options = True
                        
                        while options:
                            
                            if ''.join(move_list[:2]).lower() in possible_moves and len(move_list) >= 2:
                                game.moveBead(''.join(move_list[:2]).lower())
                                
                            else:
                                if len(move_list) != 0:
                                    raise Exception('Invalid input')
                                
                            if len(move_list) >= 2:
                                move_list.pop(0)
                                move_list.pop(0)
                  
                            else:
                                options = False

                            
                except Exception as e:
                    print(e)
                    
            
            if game.isSolved(card):
                win = True
                playing = False 
             
             
        if win:   
            game.show(card)
            print('Congratulations! Well done.')
            valid = False
            while not valid:
                replay = input('Would you like another game? [Y/N]: ')                    
                if replay[0].upper() in 'YN':
                    valid = True
                else:
                    print('Invalid Input: ')
                    
            if replay[0].upper() == 'N':
                play_again = False
                    
        else:
            print('Quit game, goodbye...')
            play_again = False

        
    
main()
    