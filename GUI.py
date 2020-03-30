import pygame
import Sudoku
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([780, 700])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    width = 75
    height = 75
    margin = 7
    black = (0,0,0)
    orange = (255, 165, 0)
    x = 50
    y = 10
    for i in range (0, 9):
        for j in range(0,9):
            pygame.draw.rect(screen, black, [x,y,width, height], 5)
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