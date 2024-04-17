import pygame
import sys

# General setup
pygame.init()
clock = pygame.time.Clock()

score_a = 0
score_b = 0

font = pygame.font.Font(None, 36)

# Setting up main window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
paddle_a = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
paddle_b = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Game Variables
ball_speed = [2, 2]
paddle_speed = 2
paddle_a_speed = 0
paddle_b_speed = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Ball movement
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collision with wall
    if ball.left < 0 or ball.right > screen_width:
        ball_speed[0] *= -1
    if ball.top < 0 or ball.bottom > screen_height:
        ball_speed[1] *= -1

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle_a_speed = -paddle_speed
    elif keys[pygame.K_DOWN]:
        paddle_a_speed = paddle_speed
    else:
        paddle_a_speed = 0

    paddle_a.move_ip(0, paddle_a_speed)

     # AI
    if ball.centery > paddle_b.centery:
        paddle_b_speed = paddle_speed
    elif ball.centery < paddle_b.centery:
        paddle_b_speed = -paddle_speed
    else:
        paddle_b_speed = 0

    # Update paddle position
    paddle_b.y += paddle_b_speed


    # Check if ball hit the wall
    if ball.left < 0:
        score_b += 1
        ball.center = (screen_width/2, screen_height/2)
    elif ball.right > screen_width:
        score_a += 1
        ball.center = (screen_width/2, screen_height/2)

    # Render scores
    score_a_surface = font.render(str(score_a), True, (0,0,0) )
    score_b_surface = font.render(str(score_b), True, (0,0,0))

    # Calculate positions for scores
    score_a_position = (10, 10)
    score_b_position = (screen_width - score_b_surface.get_width() - 10, 10)

    # Draw scores
    screen.blit(score_a_surface, score_a_position)
    screen.blit(score_b_surface, score_b_position)



    # Ensuring paddles don't go off screen
    if paddle_a.top < 0:
        paddle_a.top = 0
    if paddle_a.bottom > screen_height:
        paddle_a.bottom = screen_height
    
    # Ball collision with paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed[0] *= -1

    # Visuals
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (200, 200, 200), paddle_a)
    pygame.draw.rect(screen, (200, 200, 200), paddle_b)
    pygame.draw.ellipse(screen, (200, 200, 200), ball)
    pygame.draw.aaline(screen, (200, 200, 200), (screen_width / 2, 0), (screen_width / 2, screen_height))

    pygame.display.flip()
    clock.tick(60)