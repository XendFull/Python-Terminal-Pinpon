import time
import sys
import keyboard
# Initial positions and directions
while True:
    xpos = 15
    ypos = 10
    xdir = 'right'
    ydir = 'down'
    p1 = 10
    p2 = 10
    ROWS = 20
    score = 0
    time.sleep(0.1)
    user_input = input("What would you like to do? (singleplayer/multiplayer/exit): ").lower()
    if user_input == 'singleplayer':
        while True:
            diff = input("Select difficulty (easy/medium/hard): ").lower()
            if diff == 'easy':
                speed = 0.1
                break
            elif diff == 'medium':
                speed = 0.075
                break
            elif diff == 'hard':
                speed = 0.05
                break
            else:
                print("Invalid input, please select again.")
        while True:
            
            
            #Clear the screen 
            sys.stdout.write("\033c") 
            print("Pinpon Game")
            print("Use W and S to move the hand up and down.")
            print("——————————————————————————————————————————————" )
            
            for i in range(ROWS):  # Loop through all rows (0 to 20)
                if i == p1:  # Render hand at its position
                    if i == ypos:  # If the ball is on the same row as the hand
                        sys.stdout.write('☒☒☒'+ ' '+'🧤' + ' ' * (xpos) + '⚽' + ' ' * (38 - xpos) + '|' + '\n')
                    else:
                        sys.stdout.write('☒☒☒'+ ' '+'🧤' + ' ' * 40 + '|' + '\n')
                elif i == ypos:  # Render ball at its position
                    sys.stdout.write('☒☒☒'+ ' '+' ' * xpos + '⚽' + ' ' * (40 - xpos) + '|' +  '\n')
                else:  # Render empty rows
                    sys.stdout.write('☒☒☒'+ ' '+' ' * 42 +  '|' + '\n')
            sys.stdout.flush()  
            
            print("——————————————————————————————————————————————" )
            
            if keyboard.is_pressed('w'):
                if p1 < 20:
                    p1 -= 1
                else:
                    p1 = 19
            elif keyboard.is_pressed('s'):
                if p1 > 0:
                    p1 += 1
                else:
                    p1 = 1
            
            
            if ydir == 'down':
                if ypos == 20:
                    ydir = 'up'
                    ypos -= 1
                else:
                    ypos += 1
            elif ydir == 'up':
                if ypos == 0:
                    ydir = 'down'
                    ypos += 1   
                else:
                    ypos -= 1


            if xdir == 'right':
                if xpos == 40:
                    xdir = 'left'
                    xpos -= 1
                else:
                    xpos += 1
            elif xdir == 'left':
                if xpos == 0:
                    if (abs(ypos-p1) <= 2):
                        xdir = 'right'
                        xpos += 1
                        score += 1
                    else:
                        sys.stdout.write("\033c") # If the ball hits the left wall and not the hand, game over
                        print("Game Over!")
                        print("Your score is: ", score)
                        break
                else:
                    xpos -= 1
                    
            time.sleep(speed)  # Adjust the speed of the game based on difficulty

    elif user_input == 'multiplayer':
        while True:
            diff = input("Select difficulty (easy/medium/hard): ").lower()
            if diff == 'easy':
                speed = 0.1
                break
            elif diff == 'medium':
                speed = 0.075
                break
            elif diff == 'hard':
                speed = 0.05
                break
            else:
                print("Invalid input, please select again.")
        while True:
            
            #Clear the screen 
            sys.stdout.write("\033c")
            
            print("Pinpon Multiplayer Game")
            print("Use W and S to move the left hand up and down.")
            
            print("Use UP and DOWN arrow keys to move the right hand up and down.")
            print("———————————————————————————————————————————————————")
            
            
            
            for i in range(ROWS):  # Loop through all rows (0 to 20)
                if i == p1 and i == p2:  # Render both hands at their positions
                    if i == ypos:
                        sys.stdout.write('☒☒☒'+ ' '+'🧤' + ' ' * (xpos) + '⚽' + ' ' * (36 - xpos) + '🧤' +' '+'☒☒☒'+'\n') #47
                    else:
                        sys.stdout.write('☒☒☒'+ ' '+'🧤' + ' ' * 38 + '🧤'+ ' '+'☒☒☒'+'\n') #48
                elif i == p1:
                    if i == ypos:
                        sys.stdout.write('☒☒☒'+ ' '+'🧤' + ' ' * (xpos) + '⚽' + ' ' * (38 - xpos) + ' '+'☒☒☒'+ '\n') #48
                    else:
                        sys.stdout.write('☒☒☒'+ ' '+'🧤' + ' ' * 40 + ' ' + '☒☒☒'+'\n') #49
                elif i == p2:
                    if i == ypos:
                        sys.stdout.write('☒☒☒' + ' ' * (xpos) + '⚽' + ' ' * (39 - xpos) +'🧤'+ ' ' + '☒☒☒'+ '\n') #48
                    else:
                        sys.stdout.write('☒☒☒'+ ' '+' ' * 40 + '🧤'+ ' ' +'☒☒☒'+'\n') #49
                elif i == ypos:
                    sys.stdout.write('☒☒☒'+' '+' ' * xpos + '⚽' + ' ' * (40 - xpos) +' '+ '☒☒☒'+'\n') #49
                else:
                    sys.stdout.write('☒☒☒'+' '+' ' * 42 +' '+ '☒☒☒'+'\n')
            sys.stdout.flush()
            print("———————————————————————————————————————————————————" )
            if keyboard.is_pressed('w'):
                if p1 < 20:
                    p1 -= 1
                else:
                    p1 = 19
            elif keyboard.is_pressed('s'):
                if p1 > 0:
                    p1 += 1
                else:
                    p1 = 1
            
            if keyboard.is_pressed('up'):
                if p2 < 20:
                    p2 -= 1
                else:
                    p2 = 19
            elif keyboard.is_pressed('down'):
                if p2 > 0:
                    p2 += 1
                else:
                    p2 = 1
            
            if ydir == 'down':
                if ypos == 20:
                    ydir = 'up'
                    ypos -= 1
                else:
                    ypos += 1
            elif ydir == 'up':
                if ypos == 0:
                    ydir = 'down'
                    ypos += 1   
                else:
                    ypos -= 1


            if xdir == 'right':
                if xpos == 40:
                    if (abs(ypos-p2) <= 2):
                        xdir = 'left'
                        xpos -= 1
                    else:
                        sys.stdout.write("\033c")
                        print("Game Over!")
                        print("Player 1 wins!")
                        break
                else:
                    xpos += 1
            elif xdir == 'left':
                if xpos == 0:
                    if (abs(ypos-p1) <= 2):
                        xdir = 'right'
                        xpos += 1
                    else:
                        sys.stdout.write("\033c") # If the ball hits the left wall and not the hand, game over
                        print("Game Over!")
                        print("Player 2 wins!")
                        break
                else:
                    xpos -= 1
            
            time.sleep(speed)
            
    elif user_input == 'exit':
        sys.stdout.write("\033c")
        print("Exiting the game...")
        break
    else:
        sys.stdout.write("\033c")
        print("Invalid input, please select again.")
        
