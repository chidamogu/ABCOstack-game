#----------------------------------------------------
# Assignment 3: AbacoStack.py
# Assigment Focuses: Refresher of Python and hands-on experience with algorithm coding, input validation, exceptions, Stack, Queue, and data structures with encapsulation
# 
# Author: Chidinma Amogu
# Collaborators: Anjika Sabhani
#----------------------------------------------------

import random 

class Card:
    def __init__(self, width, depth):
        """
        An object of this class represents a configuration card for a game of AbacoStack
        Inputs: width(int) - the desired width of the card object
                depth(int) - the desired depth of the card object
        Returns: None
        """
        
        # validating input
        if type(width) != int or type(depth) != int:
            raise Exception('Error: Invalid Input')
        
        self.width = width
        self.depth = depth
        self.__beads = []
        
        # handling having a self.width input thats larger than the length of the alphabet by using lower case letters to wrap back around
        possible_beads = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        possible_beads_lower = []
        for item in possible_beads:
            possible_beads_lower.append(item.lower())
            
            
        if self.width > len(possible_beads):
            self.decided_width = possible_beads + possible_beads_lower[:self.width - len(possible_beads)]
        else:
            self.decided_width = possible_beads[:self.width]
        
        
        # using a for loop to add the beads to a list to ensure nothing gets hard coded
        for bead in self.decided_width:              
            for i in range(self.depth):                    
                self.__beads.append(bead)
    
    def reset(self):
        """
        reshuffles the instance of a card to generate a new configuration
        Inputs: None
        Outputs: None
        """
        random.shuffle(self.__beads)
    
    
    def show(self):
        """
        displays a card
        Inputs: None
        Outputs: None
        """
        
        # turning the list self.__beads into a list of BStacks to make it easier to show
        matrix = []
        h = 0
        for j in range(self.width):        
            stack = []
            for i in range(self.depth):                
                stack.append(self.__beads[h])
                h += 1
            matrix.append(stack) 
           
        i = 0
        for row in range(self.depth):
            print('|', end = '') 
            j = 0
            for m in matrix:
                if j != self.width-1:
                    print('%s ' % m[i], end = '')   
                else:
                    print('%s ' % m[i], end = '')   
                j += 1
            i += 1
            print('|')
                   
         
         
    def stack(self, number):
        """
        returns the ordered list of elements top to bottom in the number stack
        Inputs: number(int) - a number that represents the stack that should be returned
        Outputs: matrix[number] (list) - a list that represents the stack that is to be returned
        """
        
        # input valiation, making sure the number that gets inputted is an int and is within the bounds of whatever card layout being used
        if type(number) != int or number < 0:
            raise Exception('Invalid Input')
        
        if number - 1 > self.width:
            raise Exception('Stack index out of bounds')
        
        # making self.__beads into a matrix, and sending back whichever list index is inputted
        matrix = []
        number -= 1
        h = 0
        for i in range(self.width):
            stack = []
            for j in range(self.depth):
                stack.append(self.__beads[h])
                h += 1
            matrix.append(stack)
                
        return matrix[number]
    
    
    def __str__(self):
        """
        converts a Card instance into a string such that the string represents the stacks in the configuration card
        Inputs: None
        Returns: str_stack (str) - the string object that represents the stacks in the configuration card
        """
        
        str_stack = ''
        h = 0
        for column in range(self.depth):
            str_stack += '|'
            for row in range(self.width):
                str_stack += '%s' % self.__beads[h]
                h += 1
            str_stack += '|'
        
        return(str_stack)
      
        
    def replace(self, filename, n):
        """
        reads from the file filename  the nth config card and replaces the card state with the new configuration
        Inputs: filename (str) - the file that is to be read from
                n (int) - the line from the file that we need to read
        Returns: None
        """
        
        file = open(filename, 'r')
        lines = file.readlines()
        line = lines[n]
        line = line.strip()
        line = line.replace(' ', '')
        
        counts = {}
        for i in line:
            counts[i.upper()] = line.count(i)
        
        valid = True
        for i in range(1, len(counts.values())):
            # this means that the amount of each bead in the card wouldn't be the same, which wouldn't work
            if list(counts.values())[i] != list(counts.values())[i - 1]:
                valid = False
                raise Exception('Error: Invalid file')
            
        if valid:
            self.width = len(counts.keys())
            self.depth = list(counts.values())[0]
            
            # replacing the old card with the new configuration
            self.__beads = []
            for bead in list(counts.keys()):              
                for i in range(self.depth):                    
                    self.__beads.append(bead)            
            
        
        
class BStack:
    def __init__(self, size):
        """
        An object of this class represents a bounded stack
        Inputs: size(int) - represents the maximum size of the stack
        Returns: None
        """
        self.items = []
        self.capacity = size
        
        
    def push(self, item):
        """
        Adds the inputted item to the BStack if it isn't already at capacity
        Inputs: item(any type) - the item to be added to the stack
        Returns: None
        """
        
        # checking to make sure the BStack isn't full, raising an exceotion otherwise
        if len(self.items) == self.capacity:
            raise Exception('Error: Stack is full')
        
        else:
            self.items.insert(0, item)
    
    def pop(self): 
        """
        Removes the item at the head of the stack and returns it
        Inputs: None
        Returns: self.items.pop() (any type) - the item from the head of the stack
        """
        
        # checking to make sure the stack isn't empty, raising an exception otherwise
        if len(self.items) == 0:
            raise Exception('Index Error: stack is empty')
        
        else: 
            return self.items.pop(0)
    
    
    def peek(self):
        """
        returns the item at the head of the BStack, but does not remove it from the BStack
        Inputs: None
        Returns: self.items[0] (any type) - the item at the head of the stack
        """
        
        # checking to make sure the stack isn't empty, raising an exception otherwise
        if len(self.items) == 0:
            raise Exception('Index Error: stack is empty')        
        else:
            return self.items[0] 
    
    def isEmpty(self):
        """
        Returns a Boolen value that indicates whether or not the BStack is empty
        Input: None
        Returns: A boolean value
        """
        return self.items == []
    
    def size(self):
        """
        Returns the current size of the BStack
        Inputs: None
        Returns: and int value that represents the length of the stack
        """
        return len(self.items)
    
    def show(self):
        """
        displays the items in BStack
        Inputs: None
        Returns: None
        """
        print(self.items)
    
    def __str__(self):
        """
        Returns a string of all the items in BStack
        Inputs: None
        Returns: a string that contains all the items in BStack seperated by a single space
        """
        
        stackAsString = ''
        for item in self.items:
            stackAsString += str(item) + ' '
        return stackAsString
    
    def clear(self):
        """
        Resets the BStack to be completely empty
        Inputs: None
        Returns: None
        """
        if len(self.items) > 0:
            self.items = []
         
    def isFull(self):
        """
        Returns a boolean value that represents whether or not the BStack is at capacity
        Inputs: None
        Returns: A boolean Value
        """
        return len(self.items) == self.capacity


class AbacoStack:
    def __init__(self, stacks, depth):
        """
        An instance of this class represents a game of AbacoStack
        Inputs: stacks(int) - the desired amount of stacks
                depth(int) - the desired depth of each stack
        Returns: None
        """
        self.width = stacks
        self.depth = depth
        self.top_row = ['.']* int(self.width + 2)
        self.moves = 0
        self.stacks = []
        c = Card(self.width, self.depth)
        for i in range(1, self.width + 1):  # because the stack method of the card class starts from 1
            stack = BStack(self.depth)
            for element in c.stack(i):
                stack.push(element)
            self.stacks.append(stack)
       
               
    def moveBead(self, move):
        """
        Changes the state of the AbacoStack instance based on the valid moves indicated above
        Inputs: move(str) - a string of 2 characters
        Returns: None
        """
        # raising Exceptions is the move cannot be done or if the move inputted isn't valid
        if type(move) != str:
            raise Exception('Invalid Move')
        
        # getting a list of all the possible indexes so i can use it to find all the valid moves
        indexes = []
        for i in range(len(self.top_row)):
            indexes.append(i)        
        
        # if the move isn't in the list of all valid moves and exception is riased
        if int(move[0]) not in indexes or move[1].lower() not in ['u', 'd', 'l', 'r']:
            raise Exception('Invalid Move')
        
        # if the move is done from position 0 and its not going right or the move is from the last position and is not going left an exception is raised
        if int(move[0]) == 0 and move[1].lower() not in 'r' or int(move[0]) == len(self.top_row) - 1 and move[1] not in 'l':
            raise Exception('Invalid Move')
        
        # now that the input has been validated, we need to make sure the move can be done on the board, and then do them
        for i in indexes:
            # dealing with moving down from any of the valid positions
            if int(move[0]) == i and move[1].lower() == 'd':
                # if there isn't an empty space at the top of the stack for the bead to be pushed into, or there is no bead to push in at all an excpetion is raised
                if self.stacks[i-1].peek() != '.' or self.top_row[i] == '.':
                    raise Exception('Invalid Move')
                else:
                    # otherwise we pop out all the '.''s from the BStack, push in the bead, and then fill the BStack back up with '.''s
                    color = False
                    while not color:
                        if self.stacks[i-1].size() == 0:
                            color = True
                        elif self.stacks[i-1].peek() == '.':
                            self.stacks[i-1].pop()
                        else:
                            color = True
                            
                    if color:
                        self.stacks[i-1].push(self.top_row[i])
                        self.moves += 1
                        self.top_row[i] = '.'
                        while not self.stacks[i-1].isFull():
                            self.stacks[i-1].push('.')
                    
            
            if int(move[0]) == i and move[1].lower() == 'u':
                # dealing with moving up from any of the valid positions
                
                # if there is already something in the top row at that position or the BStack is empty and excpetion is raised
                if self.top_row[i] != '.' or self.stacks[i-1].isEmpty():
                    raise Exception('Invalid Move')
                      
                # otherwise we pop out all the '.''s from the BStack, pop out the bead, and then fill the BStack back up with '.''s 
                color = False
                while not color:
                    if self.stacks[i-1].size() == 0:
                        color = True
                    elif self.stacks[i-1].peek() == '.':
                        self.stacks[i-1].pop()
                    else:
                        color = True
                   
                if color:
                    if self.stacks[i-1].size() == 0:
                        raise Exception('Invalid Move')
                    
                    else:
                        element = self.stacks[i-1].pop()
                        self.top_row[i] = element
                        self.moves += 1
                        
                    while not self.stacks[i-1].isFull():
                        self.stacks[i-1].push('.')
                    
                
            if int(move[0]) == i and move[1].lower() == 'r':
                # dealing with moving right from any of the valid positions
                
                # making sure there's no bead in the position we're trying to move to, otherwise an exception is raised
                if self.top_row[i+1] != '.':
                    raise Exception('Invalid Move')
                else:
                    element = self.top_row[i]
                    self.top_row[i + 1] = element
                    self.top_row[i] = '.'
                    self.moves += 1
                    
                
            if int(move[0]) == i and move[1].lower() == 'l':
                # dealing with moving left from any of the valid positions
                
                # making sure there's no bead in the position we're trying to move to, otherwise an exception is raised                
                if self.top_row[i-1] != '.':
                    raise Exception('Invalid Move')
                
                else:
                    element = self.top_row[i]
                    self.top_row[i-1] = element
                    self.top_row[i] = '.'    
                    self.moves += 1
    
    
    
    def isSolved(self, card):
        """
        returns TRUE if the state of the instance corresponds to the configuration card, FALSE otherwise
        Inputs: card (Type Card) - an instance of the Card class
        Returns: a boolean value
        """
        
        solved = True
        # turning the inputted card into a list of BStacks to make it easier to compare the two
        c_stack = []
        for i in range(1, self.width+1):
            stack = BStack(self.depth)
            for element in card.stack(i):
                stack.push(element)
                
            c_stack.append(stack)
            
        # Since putting things into a stack reverses the order of them, popping everything from the previous BStacks and pushing them into a new one to get the correct order
        reversed_c_stack = []
        for stack in c_stack:
            new_stack = BStack(self.depth)
            for item in range(stack.size()):
                element = stack.pop()
                new_stack.push(element)
                
            reversed_c_stack.append(new_stack)
            
        # now comparing the two lists of stacks
        for stack in range(self.width):
            for i in range(self.depth):
                if str(self.stacks[stack])[i] != str(reversed_c_stack[stack])[i]:
                    solved = False
                
        return solved   
    
    def reset(self):
        """
        resets the property moves to zero and rearrange the stack to the initial position with each stack having its own beads.  
        Inputs: None
        Returns: None
        """
        self.top_row = ['.']* int(self.width + 2)
        self.moves = 0
        self.stacks = []
        c = Card(self.width, self.depth)
        for i in range(1, self.width + 1):  # because the stack method of the card class starts from 1
            stack = BStack(self.depth)
            
            for element in c.stack(i):
                stack.push(element)
            self.stacks.append(stack)
        
        
    def show(self, card = None):
        """
        takes an optional parameter card and displays the state of the AbacoStack instance. When the parameter card is present, the configuration card will also be displayed on the side of the AbacoStack instance in addition to the number of moves already taken since the start otherwise only the state of the abacoStack is shown
        Inputs: card (Type Card), optional - an instance of the class Card
        Returns: None
        """ 
        # getting all the indexes needed for the showing of the game as strings in a list
        indexes = []
        for i in range(len(self.top_row)):
            indexes.append(str(i))
            
        # printing the indexes and the top row
        print()
        print('%-2s' % ' '.join(indexes))
        
        if card != None:
            print('%-2s' % ' '.join(self.top_row), end = '')
            print(' ' * self.width, 'card')
        
        else:
            print('%-2s' % ' '.join(self.top_row))            
        
        # getting the inputted card as a list of BStacks
        if card != None:
            c_stack = []
            for i in range(1, self.width+1):
                stack = BStack(self.depth)
                for element in card.stack(i):
                    stack.push(element)
                    
                c_stack.append(stack)
            
        # displaying the game Card      
        for i in range(self.depth + (self.depth - 1)):
            print('|%s' % ' ', end = '')
            for stack in range(self.width):                
                print('%-2s' % str(self.stacks[stack])[i], end = '')

            
            # displaying the card if it's inputted
            if card != None: 
                print('|   ', end = '')                
                print('|%s' % '', end = '')            
                for stack in range(self.width):  
                    if stack != 0 and stack != self.width:
                        print('%2s' % str(c_stack[stack])[i], end = '')   
                    else:
                        print('%s' % str(c_stack[stack])[i], end = '')                       
                print('|%s' % '', end = '')            
                
                print('')
            else:
                print('|')
                
        # printing the bottom of the card and the number of moves 
        print('+' + '-'*((self.width * 2) + 1) + '+', end = '')
        print(' ' *((self.width * 2)* 2), 'Moves: ' + str(self.moves))
        print()
        
            
        
def tests():
    print('Testing the Card class:')
    c = Card(30, 30)
    print('Displaying a card that is 30 by 30')
    c.show()
    print()
    
    # testing the replace method
    print('Testing the replace method: ')
    test_file = 'test.txt'
    c.replace(test_file, 1)
    c.show()
    
    print()
    print('Testing the Card class:')
    a = Card(27, 2)
    print('Displaying a card that is 27 by 2')
    a.show()
    print()
    
    
    print('Testing the Card class:')
    d = Card(3,3)
    print('Displaying a card that is 3 by 3')    
    d.show()
    print()
    print('Displaying the stack in the 1st index of this card instance')
    stack = d.stack(1)
    print(stack)    
    
    
    print('reseting the 3 by 3 card')
    d.reset()
    print('displaying the 3 by 3 card as a string')
    d.__str__()
    print('Using the show function on the 3 by 3 card')
    d.show()
    
    stack = d.stack(1)
    print(stack)
    
    print()
    print('Testing the BStack class')
    s = BStack(5)
    print('printing:', str(s))
    print()
    
    print('is full:')
    print(s.isFull())
    print()
    
    
    print('is empty:')
    print(s.isEmpty())
    print()
    
    
    print('size:', s.size())
    print()
    
    
    print('pushing 3')
    s.push(3)
    print('pushing 4')    
    s.push(4)
    print('pushing 5')    
    s.push(5)
    print('pushing 6')    
    s.push(6)
    print('pushing 7')    
    s.push(7)
    print()
    
    print('printintg:', str(s))
    print('is full:', s.isFull())
    print()
    
    
    print('Clearing')
    s.clear()
    
    print('is full:', s.isFull())
    
    print('is empty:', s.isEmpty())
    print()
    
    print('Testing the AbacoStack Class')
    a = AbacoStack(3, 3)
    card = Card(3, 3)
    card.reset()
    
    print('is solved:', a.isSolved(card))
    
    print('showing the card to be matched:')
    a.show(card)
    
    print('Moving on the board and then displaying the game card and the template card:')
    a.moveBead('2u')
    a.show(card)
    
    a.moveBead('2r')
    a.show(card)
    
    a.moveBead('3r')
    a.show(card)
    
    a.moveBead('2u')
    a.show(card)
    
    a.moveBead('2r')
    a.show(card)    
    
    a.moveBead('2u')
    a.show(card)
    
    a.moveBead('2l')
    a.show(card) 
    
    a.moveBead('1l')
    a.show(card) 
    
    a.moveBead('1u')
    a.show(card)
    
    a.moveBead('1r')    
    a.show(card)
    
    a.moveBead('2d')    
    a.show(card)
    
    a.moveBead('1u')
    a.show(card)
    
    a.moveBead('1r')    
    a.show(card)
    
    a.moveBead('2d')    
    a.show(card)
    
    a.moveBead('1u')
    a.show(card)
    
    a.moveBead('1r')    
    a.show(card)
    
    a.moveBead('2d')    
    a.show(card)
    
    a.moveBead('0r')
    a.show(card)
    
    a.moveBead('1d')    
    a.show(card)
    
    a.moveBead('3l')    
    a.show(card)
    
    a.moveBead('2l')
    a.show(card)
    
    a.moveBead('1d')    
    a.show(card)
    
    a.moveBead('4l')    
    a.show(card) 
    
    a.moveBead('3l')    
    a.show(card)
    
    a.moveBead('2l')
    a.show(card)
    
    a.moveBead('1d')    
    a.show(card)    
    
    
    print('showing only the game card:')
    a.show()
    
if __name__ == '__main__':
    tests()