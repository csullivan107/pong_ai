import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 1600  # Increased width by 100%
window_height = int(window_width * 9 / 16)  # Calculate height for 16:9 ratio
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Move Rectangle with Arrow Keys")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the rectangle
rect_width = 25  # Half as thick
rect_height = 175  # 75% taller
rect_x = 50
rect_y = window_height // 2 - rect_height // 2

# Set up movement speed
move_speed = 5

# Set up the ball
ball_radius = 25  # Half as big
ball_x = window_width // 2
ball_y = window_height // 2

# Set up the score
score = 0

# Set up the font
font = pygame.font.SysFont(None, 48)

# Define difficulty increase rates
speed_increase_rate = 1.0  # How much to increase the ball speed per point

def reset_ball():
    global ball_x, ball_y, ball_velocity_x, ball_velocity_y, score
    ball_x = window_width // 2
    ball_y = window_height // 2
    ball_velocity_x = random.uniform(2, 5)
    ball_velocity_y = random.uniform(-1, 1)
    while abs(ball_velocity_y / ball_velocity_x) > math.tan(math.radians(45)):
        ball_velocity_y = random.uniform(-1, 1)
        ball_velocity_x = random.uniform(2, 5)
    score = 0

# Reset the ball at the beginning
reset_ball()

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rect_y -= move_speed
    if keys[pygame.K_DOWN]:
        rect_y += move_speed

    # Ensure the paddle stays within the window boundaries
    rect_y = max(min(rect_y, window_height - rect_height), 0)

    # Update ball position
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Check for collisions with the paddle
    if (ball_x + ball_radius >= rect_x and ball_x - ball_radius <= rect_x + rect_width and
            ball_y + ball_radius >= rect_y and ball_y - ball_radius <= rect_y + rect_height):
        # Calculate normalized distance from the center of the paddle to the point of collision
        paddle_center_y = rect_y + rect_height / 2
        distance_from_center = (ball_y - paddle_center_y) / (rect_height / 2)

        # Adjust vertical velocity based on the position of collision
        ball_velocity_y = 5 * distance_from_center

        # Reverse horizontal velocity and increase speed
        ball_velocity_x = -ball_velocity_x * (1 + speed_increase_rate / 10)

        # Increase the score
        score += 1

    # Check for collision with the top or bottom edge of the window
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= window_height:
        ball_velocity_y = -ball_velocity_y

    # Check for collision with the right edge of the window
    if ball_x + ball_radius >= window_width:
        ball_velocity_x = -ball_velocity_x

    # Check for collision with the left edge of the window (reset game)
    if ball_x - ball_radius <= 0:
        reset_ball()

    # Fill the window with white
    window.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(window, BLACK, (rect_x, rect_y, rect_width, rect_height))

    # Draw the ball
    pygame.draw.circle(window, BLACK, (int(ball_x), int(ball_y)), ball_radius)

    # Draw the score at the top of the window
    score_text = font.render("Score: " + str(score), True, BLACK)
    window.blit(score_text, (20, 20))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
