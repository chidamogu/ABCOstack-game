# ABCOstack-game

This is a project I made using python3 in my CMPUT 175 class taken at the University of Alberta. It runs in the terminal or in a compiler.

The user is first prompted to select how wide and how long they would like their stack to be, then they are presented with a fully sorted stack, and a randomized "card" stack. The goal of the game is to transform the sorted stack into the "card" stack using as few moves as possible. The user is able to move the letters in the stack one at a time using: up "U", down "D", to the left "L", or to the right "R". To specify which letter they want to move the user must add the column number. For example, if the user wants to move an A up by one and to the left by one, they would input 1U1L. The user can input multiple movement commands in the same line - such as "1U2U2R3R", and if one of the commands is invalid all the moves before the invalid move will be executed and all the moves after the invalid move will not be executed.
