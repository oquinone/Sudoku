import pygame
import Sudoku
import pygame.freetype
import math

def click_On_Screen(X, Y):
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            X = 0
            Y = 0
            board_X = 0
            board_Y = 0
            text = "9"
            mx, my = pygame.mouse.get_pos()
            found_X = True
            found_Y = True

            while found_X:
                if(X + 75 < mx):
                    X += 75
                    board_X += 1
                else:
                    found_X = False

            while found_Y:
                if(Y + 75 < my):
                    Y += 75
                    board_Y += 1
                else:
                    found_Y = False
            # pygame.key.start_text_input()
            #textinput = pygame.textinput.TextInput()

            #while getInput:
            if (partially_Filled_Board[board_Y][board_X] == 0):
                if event.type == pygame.KEYDOWN:
                    test = event.unicode
                    print(test)
                    if event.type == pygame.K_RETURN:
                        mes = font.render("8", True, red)
                        place = mes.get_rect(topleft = (X, Y))
                        screen.blit(mes, place)
                        #pygame.draw.rect(screen, green, [X, Y, width, height], 5)
                else:
                    return -150, -150
                # if pygame.type == pygame.K_RETURN:
                #     pygame.key.stop_text_input()


    # elif event.type == pygame.MOUSEMOTION:
    #         pygame.draw.rect(screen, red, [X, Y, width, height], 5)

    return X, Y

def get_Pressed_Number():
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_b:
            print("Hi")
            return "0"
        elif event.type == pygame.K_1:
            return '1'
        elif event.type == pygame.K_2:
            return '2'
        elif event.type == pygame.K_3:
            return '3'
        elif event.type == pygame.K_4:
            return '4'
        elif event.type == pygame.K_5:
            return '5'
        elif event.type == pygame.K_6:
            return '6'
        elif event.type == pygame.K_7:
            return '7'
        elif event.type == pygame.K_8:
            return '8'
        elif event.type == pygame.K_9:
            return '9'

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([676, 680])

pygame.display.set_caption("Soduku Game!")

# def text_objects(text, font):
#     Textsurface = font.render(text, True, green)
#     return Textsurface, Textsurface.get_rect()

# Run until the user asks to quit
pos_X = -100
pos_Y = -100
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    #Variables needed to create black Sudoku Grid
    width = 75   
    height = 75    
    margin = 7
    black = (0,0,0)
    orange = (255, 165, 0) 
    green = (0, 255, 0)
    red = (200, 0, 0)
    light_green = (0, 200, 0)
    x = 0
    y = 0
    font = pygame.font.SysFont('Arial', 35)

    sudoku_Class = Sudoku.Sodoku()
    partially_Filled_Board = sudoku_Class.get_Board()

    #Creating Sudoku Grid
    for i in range (0, 9):
        for j in range(0,9):
            pygame.draw.rect(screen, black, [x,y,width, height], 12)

            if(partially_Filled_Board[i][j] != 0):
                message = font.render(str(partially_Filled_Board[i][j]), True, black)
                place = message.get_rect(center=(math.floor(x + width / 2), math.floor(y + height / 2)))
                screen.blit(message, place)

            x += 75
        x = 0
        y += 75

    # Vertical Orange Lines in the Center
    pygame.draw.line(screen, orange, (225, 0), (225, 680), 11)
    pygame.draw.line(screen, orange, (450, 0), (450, 680), 11)

    # Horizontal Orange Lines in the Center
    pygame.draw.line(screen, orange, (0, 225), (680, 225), 11)
    pygame.draw.line(screen, orange, (0, 450), (680, 450), 11)
    #pygame.draw.rect(screen, red,[0, 225, 680, 226], 11)

    #Orange Outer Border
    pygame.draw.rect(screen, orange, [0, 0, 675,676], 11)

    pos_X, pos_Y = click_On_Screen(pos_X, pos_Y)    

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()