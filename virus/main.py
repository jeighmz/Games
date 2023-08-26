import pygame
import math

## create the skeleton for a pygame program with a circle that moves with the arrow keys and has a clock

pygame.init()

# Screen
screen = pygame.display.set_mode((400, 300))

## give the circle a position
x = 200
y = 150

# draw a circle in the window
pygame.draw.circle(screen, (0, 0, 255), (x, y), 15)


done = False

# create a clock
clock = pygame.time.Clock()

# wait for the user to close the window
while not done:
 

    ## let the circle move with the arrow keys smoothly (hint: use the clock)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    if pressed[pygame.K_ESCAPE]: done = True

    ## events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #fill the screen with black
    screen.fill((0, 0, 0))
        
    # draw a circle in the window
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 20)

    # update the display
    pygame.display.update()

    # tick the clock
    clock.tick(60)


pygame.quit()
