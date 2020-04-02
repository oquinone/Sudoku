import pygame
import Sudoku
#import pygame.freetype
import math

def click_On_Screen():
    for key in pygame.event.get():
        if key.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            pygame.draw.rect(screen, red, [mx, my, width, height], 7)

# def hover_Over_Button(x, y):
#     mouse = pygame.mouse.get_pos()


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([676, 680])

pygame.display.set_caption("Soduku Game!")

# def text_objects(text, font):
#     Textsurface = font.render(text, True, green)
#     return Textsurface, Textsurface.get_rect()

# Run until the user asks to quit
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
            grid = pygame.draw.rect(screen, black, [x,y,width, height], 12)

            if(partially_Filled_Board[i][j] != 0):
                message = font.render(str(partially_Filled_Board[i][j]), True, black)
                place = message.get_rect(center=(math.floor(x + width / 2), math.floor(y + height / 2)))
                screen.blit(message, place)
                # hover_Over_Button(x,y)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                #hold = screen.get_rect()
                text = ""
                mx, my = pygame.mouse.get_pos()
                pos_X = 0 
                pos_Y = 0
                found_X = True
                found_Y = False
                while found_X:
                    if(pos_X + 75 < mx):
                        pos_X += 75
                    else:
                        found_X = False

                while not found_Y:
                    if(pos_Y + 75 < my):
                        pos_Y += 75
                    else:
                        found_Y = True

                img = font.render(text, True, red)
                rectt = img.get_rect()
                rectt.center = (pos_Y, pos_X)
                #cursor = pygame.draw.rect(rectt.center, (3, height))
                pygame.draw.rect(screen, green, [pos_X, pos_Y, width, height], 5)


            x += 75
        x = 0
        y += 75

    # hover_Over_Button(grid)
    
    
    # Vertical Orange Lines in the Center
    pygame.draw.line(screen, orange, (225, 0), (225, 680), 11)
    pygame.draw.line(screen, orange, (450, 0), (450, 680), 11)

    # Horizontal Orange Lines in the Center
    pygame.draw.line(screen, orange, (0, 225), (680, 225), 11)
    pygame.draw.line(screen, orange, (0, 450), (680, 450), 11)

    #Border Orange Lines
    pygame.draw.line(screen, orange, (0, 0), (680, 0), 8)
    pygame.draw.line(screen, orange, (0, 675), (680, 675), 11)
    pygame.draw.line(screen, orange, (0, 0), (0, 680), 8)
    pygame.draw.line(screen, orange, (675, 0), (675, 673), 11)
    

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()