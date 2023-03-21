import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong')

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the paddles and ball
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
BALL_RADIUS = 10

player1_paddle = pygame.Rect(50, WINDOW_HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2_paddle = pygame.Rect(WINDOW_WIDTH - 50 - PADDLE_WIDTH, WINDOW_HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WINDOW_WIDTH/2 - BALL_RADIUS, WINDOW_HEIGHT/2 - BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)

# Set up the ball's initial movement
ball_speed_x = 1
ball_speed_y = 1

# Set up the scoring system
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the paddles based on keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.move_ip(0, -3)
    if keys[pygame.K_s] and player1_paddle.bottom < WINDOW_HEIGHT:
        player1_paddle.move_ip(0, 3)
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.move_ip(0, -3)
    if keys[pygame.K_DOWN] and player2_paddle.bottom < WINDOW_HEIGHT:
        player2_paddle.move_ip(0, 3)

    # Move the ball
    ball.move_ip(ball_speed_x, ball_speed_y)

    # Check for collisions with the paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed_x *= -1

    # Check for collisions with the top and bottom walls
    if ball.top < 0 or ball.bottom > WINDOW_HEIGHT:
        ball_speed_y *= -1

    # Check for scoring
    if ball.left < 0:
        player2_score += 1
        ball_speed_x = 1
        ball_speed_y = 1
        ball.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    if ball.right > WINDOW_WIDTH:
        player1_score += 1
        ball_speed_x = -1
        ball_speed_y = -1
        ball.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

    # Draw the paddles, ball, and scores
    game_window.fill(BLACK)
    pygame.draw.rect(game_window, WHITE, player1_paddle)
    pygame.draw.rect(game_window, WHITE, player2_paddle)
    pygame.draw.circle(game_window, WHITE, ball.center, BALL_RADIUS)
    player1_text = font.render('Player 1: ' + str(player1_score), True, WHITE)
    player2_text = font.render('Player 2: ' + str(player2_score), True, WHITE)
    game_window.blit(player1_text, (20, 20))
    game_window.blit(player2_text, (WINDOW_WIDTH - player2_text.get_width() - 20, 20))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
