import allfunctions_2048
import random
import time
def main():
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] #board
    randomlist = [2, 2, 2, 2, 2, 2, 2, 2, 2,  4] #list for generating random numbers in the board
    gamenotoverlist = [2, 4, 8, 16, 32, 64, 128] 
    validlist = ['a', 'w', 's', 'd', 'e'] #list to check whether the player's input is valid
    count = 0 #to count how many chances are used
    checkgamenotoverlist = [512, 1024, 2048] #list to check whether game-not-over conditions met
    point = 0
    allfunctions_2048.Welcome()
    time.sleep(1)
    allfunctions_2048.createRandom(board, randomlist, point) #creates the random starting board
    while True: #allows the code to execute forever until break
        direction = allfunctions_2048.chooseDirection() #for the player to choose the slide-direction
        #check whether the input is valid
        if direction not in validlist: #validlist = ['a', 'w', 's', 'd', 'e']
            print('Invalid input, please choose direction again.')
            allfunctions_2048.printboard(board, point)
            continue #jumps to the next round and asks for direction again
        if direction == 'e': #exit
            allfunctions_2048.print_lose()
            print('Your final score is', point)
            print('Good luck next time!')
            break
        if direction == 'a': #slide left
            board, validity, point = allfunctions_2048.slide_left(board, point)
        if direction == 'd': #slide right
            board, validity, point = allfunctions_2048.slide_right(board, point)
        if direction == 'w': #slide up
            board, validity, point = allfunctions_2048.slide_up(board, point)
        if direction == 's': #slide down
            board, validity, point = allfunctions_2048.slide_down(board, point)
        if validity == False: 
        #validity == False when nothing in the board is changed, neither compressed nor combined, then this slide-direction is invalid
            allfunctions_2048.printboard(board, point)
            continue
        if validity == True: #slide-direction valid
            allfunctions_2048.randomNumberCell(board, randomlist, point) #adds randomly 2 or 4 to an empty cell
            condition = allfunctions_2048.check_game_over(board) #check whether win or lose or continue
            if point >= 25000: #another way of winning, total score >= 25000
                print('Total score:', point, '>= 25000')
                print('')
                print('CONGRATULATIONS!!!')
                time.sleep(1)
                allfunctions_2048.print_win()
                time.sleep(1)
                print('Your final score is', point)
                break
            if condition == 'Continue': #continue
                print(condition)
                continue #jumps into the next loop
            if condition == "CONGRATULATIONS!!!": #won
                print('')
                print(condition)
                time.sleep(1)
                allfunctions_2048.print_win()
                time.sleep(1)
                print('Your final score is', point)
                break
            if condition == "GAME OVER!!!":
                if count == 1: #if the second chance is already used, then the player has lost
                    print('Second chance already used.')
                    print('')
                    allfunctions_2048.print_lose()
                    time.sleep(1)
                    print('Your final score is', point)
                    print('Good luck next time!')
                    break
                else: #if the player has not used the first chance
                    print('')
                    count += 1 #first chance is used
                    temp = []
                    for x in checkgamenotoverlist: #[512, 1024, 2048]
                        for y in board:
                            if x in y: #to check whether there are numbers greater than or equal to 512 in board
                                temp.append(True) #if so, add True
                            else:
                                temp.append(False)#if not, add False
                    if any(temp) == True: #game-not-over conditions met
                        allfunctions_2048.game_not_over(board, gamenotoverlist) 
                        #randomly chooses 6 cells with numbers smaller than or equal to 128 and clears the cell
                        time.sleep(2)
                        print('Game-not-over conditions met.')
                        time.sleep(1)
                        x = input('Press enter to continue playing, input e to give up: ') 
                        #Player can choose to continue playing, or give up
                        if x == 'e':
                            print('Oh no! You were so close!')
                            time.sleep(1)
                            allfunctions_2048.print_lose()
                            print('Your final score is', point)
                            print('Good luck next time!')
                            break
                        else:
                            print('Score -2048')
                            print('Come on! You are about to win.')
                            point -= 2048 #score -2048 as a punishment of using the second chance
                            time.sleep(1)
                            allfunctions_2048.printboard(board, point)
                            print('Continue')
                    if any(temp) == False: #game-not-over conditions not met, then the player has lost
                        time.sleep(2)
                        print('Game-not-over conditions not met.')
                        time.sleep(1)
                        allfunctions_2048.print_lose()
                        time.sleep(1)
                        print('You final score is', point)
                        print('Good luck next time!')
                        break
                    
main()
