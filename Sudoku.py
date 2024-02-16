# modules

import time
import os


# this function will pause the script with a custom message
def pause(message = 'press any key to continue'):
    print(message)
    # this will pause untill any key is pressed.
    os.system('pause >NULL')
    return 0


# function which clears the console
def clear_console():
    os.system('cls')


# function that displays the contents of a board
def display_board(x):
    clear_console()
    print('     1  2  3  4  5  6  7  8  9')
    print('  -----------------------------')
    for i in range(9):
        print(i+1, '| ', end= ' ')
        for j in range(len(x[i])):
            print(x[i][j], end='  ')
        print()
    print()

# solution of a particular difficulty
def solution(difficulty):
    x = []
    if difficulty == 1:
        row1 = [5, 4, 9, 6, 1, 3, 7, 8, 2]
        row2 = [8, 3, 1, 2, 5, 7, 9, 6, 4]
        row3 = [6, 7, 2, 9, 8, 4, 1, 5, 3]
        row4 = [4, 1, 5, 3, 7, 8, 2, 9, 6]
        row5 = [9, 2, 8, 5, 6, 1, 4, 3, 7]
        row6 = [7, 6, 3, 4, 2, 9, 5, 1, 8]
        row7 = [2, 8, 4, 1, 9, 6, 3, 7, 5]
        row8 = [1, 5, 7, 8, 3, 2, 6, 4, 9]
        row9 = [3, 9, 6, 7, 4, 5, 8, 2, 1]
        x = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
    elif difficulty == 2:
        row1 = [3, 2, 8, 7, 6, 1, 5, 9, 4]
        row2 = [5, 1, 9, 8, 3, 4, 6, 7, 2]
        row3 = [6, 4, 7, 2, 5, 9, 8, 1, 3]
        row4 = [8, 6, 1, 4, 2, 3, 7, 5, 9]
        row5 = [7, 9, 2, 6, 8, 5, 4, 3, 1]
        row6 = [4, 5, 3, 9, 1, 7, 2, 8, 6]
        row7 = [1, 7, 5, 3, 4, 2, 9, 6, 8]
        row8 = [9, 8, 4, 1, 7, 6, 3, 2, 5]
        row9 = [2, 3, 6, 5, 9, 8, 1, 4, 7]
        x = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
    elif difficulty == 3:
        row1 = [7, 3, 5, 2, 4, 8, 9, 1, 6]
        row2 = [4, 6, 9, 1, 7, 5, 3, 8, 2]
        row3 = [2, 8, 1, 3, 6, 9, 4, 7, 5]
        row4 = [5, 1, 3, 6, 2, 7, 8, 9, 4]
        row5 = [8, 7, 2, 5, 9, 4, 1, 6, 3]
        row6 = [6, 9, 4, 8, 1, 3, 5, 2, 7]
        row7 = [9, 2, 6, 4, 5, 1, 7, 3, 8]
        row8 = [1, 5, 8, 7, 3, 6, 2, 4, 9]
        row9 = [3, 4, 7, 9, 8, 2, 6, 5, 1]
        x = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
    return x


# assigns a puzzle to the empty initialized board based on difficulty
def assign_puzzle(n):
    x = []
    if n == 1:
        row1 = [5, 0, 9, 0, 1, 0, 0, 8, 2]
        row2 = [8, 3, 1, 0, 5, 0, 0, 0, 0]
        row3 = [6, 0, 2, 9, 0, 0, 1, 0, 0]
        row4 = [4, 1, 0, 3, 0, 8, 2, 9, 0]
        row5 = [9, 2, 0, 5, 6, 1, 0, 0, 7]
        row6 = [0, 0, 0, 4, 2, 0, 0, 0, 8]
        row7 = [0, 8, 0, 0, 0, 6, 3, 0, 5]
        row8 = [0, 0, 7, 0, 3, 0, 6, 0, 0]
        row9 = [0, 9, 0, 0, 4, 5, 0, 0, 0]
        x = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
    if n == 2:
        row1 = [3, 2, 0, 0, 0, 1, 5, 0, 0]
        row2 = [0, 1, 9, 8, 3, 0, 0, 7, 0]
        row3 = [6, 0, 0, 0, 0, 0, 0, 1, 0]
        row4 = [8, 6, 0, 4, 0, 3, 0, 0, 0]
        row5 = [0, 0, 0, 0, 8, 5, 0, 3, 0]
        row6 = [4, 0, 3, 0, 0, 0, 2, 8, 0]
        row7 = [1, 7, 5, 3, 4, 2, 0, 0, 0]
        row8 = [0, 0, 0, 1, 0, 0, 0, 0, 0]
        row9 = [0, 0, 0, 5, 0, 0, 1, 0, 7]
        x = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
    if n == 3:
        row1 = [0, 0, 5, 0, 0, 8, 0, 0, 0]
        row2 = [0, 0, 0, 0, 7, 0, 0, 8, 0]
        row3 = [0, 0, 0, 3, 0, 0, 4, 7, 5]
        row4 = [0, 0, 0, 0, 0, 7, 0, 0, 0]
        row5 = [0, 0, 0, 0, 9, 4, 1, 0, 0]
        row6 = [0, 9, 0, 8, 0, 0, 0, 0, 0]
        row7 = [9, 2, 0, 0, 0, 0, 0, 3, 8]
        row8 = [1, 0, 0, 0, 0, 6, 0, 0, 9]
        row9 = [3, 4, 0, 0, 0, 2, 6, 0, 0]
        x = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
    return x

# inserts an element to the puzzle
def insert(x, row, col, a):
    if x[row-1][col-1] == 0:
        x[row-1][col-1] = a
        print('Element inserted successfully.')
    else:
        print('There is already an element in this position.')
    pause()
    return x

# deletes an element from the puzzle
def delete(difficulty, x, row, col):
    testlist = []
    testlist = assign_puzzle(difficulty)
    if testlist[row-1][col-1] != 0:
        print('The element is part of the original puzzle.')
    else:
        x[row-1][col-1] = 0
        print('Element deleted successfully.')
    pause()
    return x


#main
# initialization
rows, cols = (9, 9)
board = [[0] * rows] * cols

# input difficulty level
print('Input a number from 1 to 3 to choose your difficulty level:')
print('1 - Easy')
print('2 - Medium')
print('3 - Hard')
difficulty = input()
while not (difficulty == '1' or difficulty == '2' or difficulty == '3'):
    print("Input must be an integer between 1-3 inclusive.")
    difficulty = input()
difficulty = int(difficulty)

if difficulty == 1:
    print('You have chosen an easy puzzle.')
elif difficulty == 2:
    print('You have chosen a medium puzzle.')
elif difficulty == 1:
    print('You have chosen a hard puzzle.')
pause()

# set board to difficulty level
board = assign_puzzle(difficulty)

flag = False
highscore = 0

# start timer
start = time.time()

while not flag:
    display_board(board)
    # case statements
    print('What would you like to do?')
    print('1 - Insert an element')
    print('2 - Delete an element')
    print('3 - Submit the puzzle')

    answer = input()
    while not (answer == '1' or answer == '2' or answer == '3'):
        print("Input must be an integer between 1-3 inclusive.")
        answer = input()
    answer = int(answer)

    if answer == 1:
        print('Input the row you would like to insert the number in')
        row = int(input())

        print('Input the column you would like to insert the number in')
        column = int(input())

        print('Input the number you would like to insert')
        num1 = int(input())

        board = insert(board, row, column, num1)

    elif answer == 2:
        print('Input the row you would like to delete the number from')
        row = int(input())

        print('Input the column you would like to delete the number from')
        column = int(input())

        board = delete(difficulty, board, row, column)

    elif answer == 3:
        # stop timer
        end = time.time()
        time_taken = round(end - start)
        print("It took you", time_taken, "seconds to complete the puzzle.")
        if board == solution(difficulty):
            if highscore == 0:
                highscore = time_taken
            else:
                if time_taken >= highscore:
                    print('You have successfully completed the puzzle but not beaten your highscore.')
                    print('Your highscore is', highscore)
                else:
                    print('Congratulations, you beat your highscore.')
                    print('Your new highscore is:', time_taken, 'seconds.')
        else:
            print('Your solution is either incomplete or wrong. Better luck next time!')
        pause()

        flag = True
        
pause()
exit()
