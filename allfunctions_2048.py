import random

def Welcome(): #This is the welcome function to start the game.
    print('''*****************************************************************  
***************     Welcome to the 2048-Game     ****************
**                                                             **
** 1. The aim of the game is to slide cells containing numbers **
**    on a 4*4 board to combine them to create the number 2048 **
** 2. Once you create the number 2048 or reach 25000 points,   **
**    you will win                                             **
** 3. If you fail to create 2048 or reach 25000 points with    **
**    all cells already occupied and no chance of combining    **
**    cells, you will fail                                     **
** 4. When you fail for the first time, but you have created   **
**    numbers greater than 512, a second chance will be given  **
**                                                             **
***************           GOOD LUCK!!!           ****************
*****************************************************************''')
    _ = input('Press enter to proceed to the commands ') 
    #input() is used so that the player need not to read too much at the same time. 
    #When the player has read the rules, he or she can press enter to proceed to the commands
    print('''Command are as follows: 
\tSlide Left:  a
\tSlide Right: d
\tSlide Up:    w
\tSlide Down:  s
\tExit:        e''')
    _ = input('Press enter to start the game ') 
    #same as above
    print('TIME TO START!!!!')
    print('')

#print the 4*4 board and the score of the game
def printboard(board, point): 
    #we use nested for-loops to print the board because board=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range (4): 
        for j in range (3): 
            print(str(board[i][j]).rjust(4), end = ' ') 
        print(str(board[i][3]).rjust(4))
    print('Score:', point)

#This function chooses two random cells to change them to 2 or 4 randomly to create the starting board of 2048.
def createRandom(board, randomlist, point): 
    for i in range (2):
        x = random.choice(board) #x is a random sub-list chosen out of the list board.
                                 #It can be guaranteed that x contains 0. No need to check x.
        y = random.randint(0, 3) #y can be any number between 0 and 3 containing 0 and 3.
                                 #x[y] refers to the randomly chosen cell
        #It can happen that the program chooses the same x and y twice. And this while loop will avoid that.
        while x[y] != 0: 
            y = random.randint(0, 3)
        x[y] = random.choice(randomlist) #randomlist = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
    printboard(board, point) #print the board

def chooseDirection(): 
    x = input('Choose the direction to slide (a/w/s/d/e):')
    return x

#This function is used to randomly put 2 or 4 to a randomly chosen cell each round.
def randomNumberCell(board, randomlist, point): 
    x = random.choice(board) #need to check the sub-list x too
    # It can happen that sub-list x = [2, 16, 64, 4] (does not contain 0) and this while loop is used to prevent that.
    while 0 not in x: 
        x = random.choice(board)
    y = random.randint(0, 3)
    while x[y] != 0:
        y = random.randint(0, 3)
    x[y] = random.choice(randomlist)
    printboard(board, point)

#to check whether the player has won, lost, or neither and the game continues
def check_game_over(board): 
    #Once there is 2048 in the board, the player wins immediately.
    for i in range(4):
        for j in range(4): 
            if (board[i][j] == 2048): 
                return "CONGRATULATIONS!!!"
    #If the player has not won, and there are still 0 (empty cells) in the board, the game continues
    for i in range(4):
        for j in range(4):
            if (board[i][j] == 0):
                return 'Continue'
    #If there are no 0s (empty cells), but two same numbers are next to each other (can be combined), the game continues
    for i in range(3):
        for j in range(3): 
            if (board[i][j] == board[i+1][j] or board[i][j] == board[i][j+1]):
                return 'Continue'
    #The next two blocks are used to check the last line and the last column for numbers that can be combined
    #It is separated from the block above two avoid out of index error
    for i in range(3): 
        if (board[3][i] == board[3][i+1]):
            return "Continue"
    for i in range(3):
        if (board[i][3] == board[i+1][3]):
            return 'Continue'
    #If all the conditions above are not met, then the player has lost
    return "GAME OVER!!!"  

#This function is something new we want to add to the game 2048.
#Our idea is that when the player has already created numbers greater than or equal to 512 and then loses,
#six random cells with numbers smaller than or equal to 128 will be changed to 0 (clear the space).
#2048 is subtracted from the total score as a punishment and the game continues.

#This function is used to clear the six cells with numbers smaller than or equal to 128
def game_not_over(board, gamenotoverlist):#gamenotoverlist = list of numbers smaller than or equal to 128
    for i in range (6): #clear six cells
        x = random.choice(board)
        temp = [] #we have to check whether there exist a number smaller than or equal to 128 in this sub-list x
        for z in x:
            if z not in gamenotoverlist: #if z is not number smaller than or equal 128, False is added to the list temp
                temp.append(False)
            else:
                temp.append(True) #if z is a number smaller than or equal to 128, True is added to the list
        while any(temp) == False: #So if there is no numbers smaller than or equal to 128 in the sub-list,
            x = random.choice(board) #the program randomly chooses the another sub-list x again
            temp = []
            for z in x:
                if z not in gamenotoverlist:
                    temp.append(False)
                else:
                    temp.append(True)
        y = random.randint(0, 3)
        while x[y] not in gamenotoverlist: #To check whether x[y] is a number smaller than or equal to 128
            y = random.randint(0, 3)
        x[y] = 0

#The following functions are used to slide to left, right, up or down.

#to compress all cells to the left side without combining them
def compress_left(board): 
    validity = False #to check whether something has changed
    new_board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range (4):
        position = 0
        #If there is an occupied cell (!=0）in this line, then this cell should be compressed to the first cell (board[i][0]) of this line.
        #Therefore, position is at first 0.
        for j in range (4):
            if (board[i][j] != 0):
                new_board[i][position] = board[i][j]
                if j != position:
                    validity = True #when something has change, validity becomes True
                position += 1 #when board[i][0] is occupied, position becomes 1 (the second cell of this line)
    return new_board, validity

#to combine two same numbers
def combine_left(board, point):
    validity = False
    for i in range (4):
        for j in range (3):
            if (board[i][j] == board[i][j+1] and board[i][j] != 0):
                point += board [i][j]*2 
                board[i][j] = board[i][j]*2 #the number of the left cell becomes twice the original number
                board[i][j+1] = 0 #the right cell becomes 0
                validity = True
    return board, validity, point

#realizing sliding to the left
def slide_left(board, point):
    new_board, validity1 = compress_left(board) #First compress, then combine, then compress again
    new_board, validity2, point = combine_left(new_board, point)
    validity = validity1 or validity2 #True or False = True, True or True = True, False or False = False
    new_board, _ = compress_left(new_board)
    return new_board, validity, point

#The following functions have the same logic as sliding to the left.
#Only small changes need to be made, since sliding left combines from the left to the right, and vice versa.
#Sliding up combines from up to down, and vice versa
def compress_right(board):
    validity = False
    new_board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range (4):
        position = 3
        for j in range (3, -1, -1):
            if (board[i][j] != 0):
                new_board[i][position] = board[i][j]
                if j != position:
                    validity = True
                position -= 1
    return new_board, validity

def combine_right(board, point):
    validity = False
    for i in range (4):
        for j in range (3, 0, -1):
            if (board[i][j] == board[i][j-1] and board[i][j] != 0):
                point += board[i][j]*2
                board[i][j] = board[i][j]*2
                board[i][j-1] = 0
                validity = True
    return board, validity, point

def slide_right(board, point):
    new_board, validity1 = compress_right(board)
    new_board, validity2, point = combine_right(new_board, point)
    validity = validity1 or validity2
    new_board, _ = compress_right(new_board)
    return new_board, validity, point

def compress_up(board):
    validity = False
    new_board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range (4):
        position = 0
        for j in range (4):
            if (board[j][i] != 0):
                new_board[position][i] = board[j][i]
                if j != position:
                    validity = True
                position += 1
    return new_board, validity

def combine_up(board, point):
    validity = False
    for i in range (4):
        for j in range (3):
            if (board[j][i] == board[j+1][i] and board[j][i] != 0):
                point += board[j][i]*2
                board[j][i] = board[j][i]*2
                board[j+1][i] = 0
                validity = True
    return board, validity, point

def slide_up(board, point):
    new_board, validity1 = compress_up(board)
    new_board, validity2, point = combine_up(new_board, point)
    validity = validity1 or validity2
    new_board, _ = compress_up(new_board)
    return new_board, validity, point

def compress_down(board):
    validity = False
    new_board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range (4):
        position = 3
        for j in range(3,-1,-1):
            if board[j][i] != 0:
                new_board[position][i] = board[j][i]
                if j != position:
                    validity = True
                position -= 1
    return new_board, validity

def combine_down(board, point):
    validity = False
    for i in range(4):
        for j in range(3, 0, -1):
            if board[j][i] == board[j-1][i] and board[j][i] != 0:
                point += board[j][i]*2
                board[j][i] = board[j][i]*2
                board[j-1][i] = 0
                validity = True
    return board, validity, point

def slide_down(board, point):
    new_board, validity1 = compress_down(board)
    new_board, validity2, point = combine_down(new_board, point)
    validity = validity1 or validity2
    new_board, _ = compress_down(new_board)
    return new_board, validity, point

def print_win():
    print('██████████████████████████████████████████████████████████████████████████████████████████')
    print('███  ██████  ████      ████  ██████  ██████  ████████████████  ████      ████    ████  ███')
    print('████  ████  ████  ████  ███  ██████  ██████  ██████    ██████  ███  ████  ███  █  ███  ███')
    print('█████  ██  ████  ██████  ██  ██████  ███████  ████  ██  ████  ███  ██████  ██  ██  ██  ███')
    print('██████    █████  ██████  ██  ██████  ███████  ████  ██  ████  ███  ██████  ██  ██  ██  ███')
    print('███████  ██████  ██████  ██  ██████  ████████  ██  ████  ██  ████  ██████  ██  ███  █  ███')
    print('███████  ███████  ████  ████  ████  █████████  ██  ████  ██  █████  ████  ███  ███  █  ███')
    print('███████  ████████      ██████      ███████████    ██████    ███████      ████  ████    ███')
    print('██████████████████████████████████████████████████████████████████████████████████████████')

def print_lose():
    print('███████████████████████████████████████████████████████████████████████████████████████')
    print('███  ██████  ████      ████  ██████  ██████  ███████████      █████       ██        ███')
    print('████  ████  ████  ████  ███  ██████  ██████  ██████████  ████  ███   ██████████  ██████')
    print('█████  ██  ████  ██████  ██  ██████  ██████  █████████  ██████  ██   ██████████  ██████')
    print('██████    █████  ██████  ██  ██████  ██████  █████████  ██████  ███      ██████  ██████')
    print('███████  ██████  ██████  ██  ██████  ██████  █████████  ██████  ███████   █████  ██████')
    print('███████  ███████  ████  ████  ████  ███████  ██████████  ████  ████████   █████  ██████')
    print('███████  ████████      ██████      ████████         ████      ████       ██████  ██████')
    print('███████████████████████████████████████████████████████████████████████████████████████')
