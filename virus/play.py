import pygame
import math
import random


## create the skeleton for a pygame program with a circle that moves with the arrow keys and has a clock

pygame.init()

# Screen
screen = pygame.display.set_mode((400, 300))

## title 
pygame.display.set_caption("virus")


## give the circle a position
x = 200
y = 150


enemy_count = 4
health_count = 0

enemy_killed = 0

enemy_x = [random.randint(0, 400) for i in range(enemy_count)]
enemy_y = [random.randint(0, 300) for i in range(enemy_count)]

health_x = [random.randint(0, 400) for i in range(health_count)]
health_y = [random.randint(0, 300) for i in range(health_count)]

# draw a circle in the window
pygame.draw.circle(screen, (0, 0, 255), (x, y), 15)

for i in range(enemy_count):
    pygame.draw.circle(screen, (255, 0, 0), (enemy_x[i], enemy_y[i]), 10)

score = 0

done = False

## add a function that draws a fading circle as a blast radius around the circle when the health potion is collected


def draw_blast_radius(x, y):
   for i in range(10):
       pygame.draw.circle(screen, (255, 255, 255), (x, y), 10 + i**2)
       pygame.display.update()
       pygame.time.wait(100)
       screen.fill((0, 0, 0))
       pygame.draw.circle(screen, (0, 0, 255), (x, y), 15)


# create a clock
clock = pygame.time.Clock()

# wait for the user to close the window
while not done:
    ## increase the score the longer the player survives
    score += 1

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

    # draw the score top right corner
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))


    ## when the temp_score reaches 100, add another enemy
    if score % 100 == 0:
        enemy_count += 1

        ## spawn kill check for new enemy
        new_enemy_x = random.randint(0, 400)
        new_enemy_y = random.randint(0, 300)
        if x-25 <= new_enemy_x <= x+25 and y-25 <= new_enemy_y <= y+25:
            new_enemy_x = random.randint(0, 400)
            new_enemy_y = random.randint(0, 300)
        enemy_x.append(new_enemy_x)
        enemy_y.append(new_enemy_y)

    if score % 200 == 0:
        health_count += 1
        health_x.append(random.randint(0, 400))
        health_y.append(random.randint(0, 300))
        
    # draw a circle in the window
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 15)

    # draw a circle as a health potion
    for i in range(health_count):
        pygame.draw.circle(screen, 'yellow', (health_x[i], health_y[i]), 7)

    # draw circles for the enemies
    for i in range(enemy_count):
        pygame.draw.circle(screen, (255, 0, 0), (enemy_x[i], enemy_y[i]), 10)

    # move the enemies
    for i in range(enemy_count):
        enemy_x[i] += random.randint(-2, 2)
        enemy_y[i] += random.randint(-2, 2)
        if enemy_x[i] < 0:
            enemy_x[i] = 0
        if enemy_x[i] > 400:
            enemy_x[i] = 400
        if enemy_y[i] < 0:
            enemy_y[i] = 0
        if enemy_y[i] > 300:
            enemy_y[i] = 300

    # check for collisions
    for i in range(enemy_count):
        if math.sqrt((x - enemy_x[i])**2 + (y - enemy_y[i])**2) < 25:
            ## display "Game Over" in center of screen and enemies_killed

            #screen.fill((0, 0, 0))
            font = pygame.font.Font("freesansbold.ttf", 50)
            text = font.render("Game Over", True, (255, 255, 255))
            screen.blit(text, (60, 100))

            pygame.display.update()
            pygame.time.wait(2000)

            font = pygame.font.Font("freesansbold.ttf", 15)
            text = font.render("virus's killed: " + str(enemy_killed), True, (255, 255, 255))
            screen.blit(text, (140, 150))
            pygame.display.update()
            pygame.time.wait(1000)
            
            text = font.render(str(enemy_killed)+" x +10", True, (255, 255, 255))
            screen.blit(text, (160, 170))
            pygame.display.update()
            pygame.time.wait(500)

            font = pygame.font.Font("freesansbold.ttf", 17)
            final_score = score + int(enemy_killed*10)
            score = final_score
            text = font.render("final score: " + str(final_score), True, (255, 255, 255))
            screen.blit(text, (130, 200))
            pygame.display.update()

            pygame.time.wait(6500)

            
           
            done = True

    # check for collision with health potion
    for i in range(health_count):
        if math.sqrt((x - health_x[i])**2 + (y - health_y[i])**2) < 20:
            ## kill enemies in a blast radius of 100
            for j in range(enemy_count):
                if math.sqrt((health_x[i] - enemy_x[j])**2 + (health_y[i] - enemy_y[j])**2) < 100:
                    enemy_x[j] = 1000
                    enemy_y[j] = 1000
                    enemy_killed += 1
            draw_blast_radius(health_x[i], health_y[i])
            health_count -= 1
            health_x.pop(i)
            health_y.pop(i)
            break
    
    # check for collision with border
    if x < 0:
        x = 0 + 20
    if x > 400:
        x = 400 - 10
    if y < 0:
        y = 0 + 10
    if y > 300:
        y = 300 - 10
    

    # update the display
    pygame.display.update()

    # tick the clock
    clock.tick(60)

print("score: " + str(final_score))
pygame.quit()
