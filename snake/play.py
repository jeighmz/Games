import random
import os
import sys
from leaderboard import connect, initate_leaderboard, add_score, view_leaderboard, check_rank, update_leaderboard 

# Import pygame
import pygame



# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 800
SNAKE_SIZE = 20
FOOD_SIZE = 20
FPS = 18 ## human reaction time is 0.25s

# Colors
dark_green = (0, 100, 0)
light_green = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initial snake position
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_speed_x = 0
snake_speed_y = 0

# Initial food position
food_x = random.randint(0, (WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE
food_y = random.randint(0, (HEIGHT - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE

# Snake body (list of segments)
snake_body = [(snake_x, snake_y)]

# Score
score = 0

# Color gradient for the snake's body
# You can customize the gradient colors as desired
first_move = False

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            first_move = True
            if event.key == pygame.K_UP and snake_speed_y == 0:
                snake_speed_x = 0
                snake_speed_y = -SNAKE_SIZE
            if event.key == pygame.K_DOWN and snake_speed_y == 0:
                snake_speed_x = 0
                snake_speed_y = SNAKE_SIZE
            if event.key == pygame.K_LEFT and snake_speed_x == 0:
                snake_speed_x = -SNAKE_SIZE
                snake_speed_y = 0
            if event.key == pygame.K_RIGHT and snake_speed_x == 0:
                snake_speed_x = SNAKE_SIZE
                snake_speed_y = 0

    snake_x += snake_speed_x
    snake_y += snake_speed_y

    # Check for collisions with self after first move
    if first_move and (snake_x, snake_y) in snake_body[1:]:
        running = False

    # Check for collisions with game borders
    if (
        snake_x < 0
        or snake_x >= WIDTH
        or snake_y < 0
        or snake_y >= HEIGHT
    ):
        running = False

    # Check if the snake eats the food
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, (WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE
        food_y = random.randint(0, (HEIGHT - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE
        # Increase the snake's size by adding a new segment
        snake_body.append((snake_x, snake_y))
        # Increase the score
        score += 1

    # Clear the screen
    screen.fill(BLACK)

    # Update the snake's body segments
    snake_body.insert(0, (snake_x, snake_y))

    # Remove the last segm
    # ent if the snake didn't eat food (to make it move)
    if len(snake_body) > 3:
        snake_body.pop()

    # Draw the food
    pygame.draw.rect(screen, RED, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))

    # Draw the score on the screen
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))


    # Draw the snake's body
    for segment in snake_body:
        pygame.draw.rect(screen, light_green, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))


    if running == False:
        initate_leaderboard()
        if check_rank(score) == True:
            print('you got a high score!')
            # get user id
            id = input('enter your id: ')
            # add score to leaderboard
            update_leaderboard(id, score)
            
            # display leaderboard on display
            font = pygame.font.Font(None, 36)
            text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(text, (10, 10))
            

            ## delay for 1 second
            pygame.time.delay(1000)
    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(FPS)

print('score: ', score)
# Quit Pygame
pygame.quit()
sys.exit()
