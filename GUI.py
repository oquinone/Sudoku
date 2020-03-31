import pygame
import Sudoku
import pygame.freetype
import math

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([780, 700])

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
    x = 50
    y = 10
    font = pygame.font.SysFont('Arial', 35)

    sudoku_Class = Sudoku.Sodoku()
    partially_Filled_Board = sudoku_Class.get_Board()

    #Creating Sudoku Grid
    for i in range (0, 9):
        for j in range(0,9):
            pygame.draw.rect(screen, black, [x,y,width, height], 13)

            if(partially_Filled_Board[i][j] != 0):
                message = font.render(str(partially_Filled_Board[i][j]), True, black)
                place = message.get_rect(center=(math.floor(x + width / 2), math.floor(y + height / 2)))
                screen.blit(message, place)


            x += 75
        x = 50
        y += 75
    
    # Vertical Orange Lines in the Center
    pygame.draw.line(screen, orange, (274, 10), (274, 680), 8)
    pygame.draw.line(screen, orange, (499, 10), (499, 680), 8)

    # Horizontal Orange Lines in the Center
    pygame.draw.line(screen, orange, (48, 233), (727, 233), 8)
    pygame.draw.line(screen, orange, (48, 458), (727, 458), 8)

    #Border Orange Lines
    pygame.draw.line(screen, orange, (48, 10), (727, 10), 8)
    pygame.draw.line(screen, orange, (48, 682), (727, 682), 8)
    pygame.draw.line(screen, orange, (48, 10), (48, 682), 8)
    pygame.draw.line(screen, orange, (725, 10), (725, 682), 8)
    

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()