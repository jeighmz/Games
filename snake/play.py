import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20
FOOD_SIZE = 20
FPS = 10

# Colors
dark_green = (0, 100, 0)
light_green = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Load Snake Head Image
snake_head_image = pygame.image.load("pics/snake_head.png")
snake_head_image = pygame.transform.scale(snake_head_image, (SNAKE_SIZE, SNAKE_SIZE))


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

# Define the start and end colors for the gradient
start_color = dark_green
end_color = light_green

# Number of colors in the gradient
num_colors = 40

# Calculate the color step for each component (R, G, B)
color_step = [(end - start) // num_colors for start, end in zip(start_color, end_color)]

# Generate the color gradient
color_gradient = [(start_color[0] + i * color_step[0],
                   start_color[1] + i * color_step[1],
                   start_color[2] + i * color_step[2])
                  for i in range(num_colors)]


# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
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

    # Check for collisions with self
    if (snake_x, snake_y) in snake_body[1:] and len(snake_body) > 10:
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

    # Remove the last segment if the snake didn't eat food (to make it move)
    if len(snake_body) > 1 and (snake_x, snake_y) != snake_body[-1]:
        snake_body.pop()

    # Draw the snake with color fading effect
    for i, segment in enumerate(snake_body):
        # Calculate the index in the gradient based on position
        gradient_index = min(i, len(color_gradient) - 1)
        segment_color = color_gradient[gradient_index]
        pygame.draw.rect(screen, segment_color, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    # Draw the food
    pygame.draw.rect(screen, RED, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))

    # Draw the score on the screen
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    if snake_speed_x > 0:
        rotated_head = pygame.transform.rotate(snake_head_image, 90)
    elif snake_speed_x < 0:
        rotated_head = pygame.transform.rotate(snake_head_image, 270)
    elif snake_speed_y > 0:
        rotated_head = pygame.transform.rotate(snake_head_image, 0)
    else:
        rotated_head = pygame.transform.rotate(snake_head_image, 180)

    screen.blit(rotated_head, (snake_body[0][0], snake_body[0][1]))

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
