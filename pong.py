import pygame
import sys
import random

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
move_speed = int(2 * 1.5)  # Increased by 50%
move_speed += int(move_speed * 0.5)  # Increase by 50% more

# Set up the ball
ball_radius = 25  # Half as big
ball_x = window_width // 2
ball_y = window_height // 2

# Set up the ball velocity
ball_velocity_x = random.uniform(2, 5)  # Random initial velocity towards the right side
ball_velocity_y = random.uniform(-2, 2)  # Random initial vertical velocity

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

    # Update ball position
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Check for collisions with the paddle
    if (ball_x + ball_radius >= rect_x and ball_x - ball_radius <= rect_x + rect_width and
            ball_y + ball_radius >= rect_y and ball_y - ball_radius <= rect_y + rect_height):
        ball_velocity_x = -ball_velocity_x

    # Check for collision with the top or bottom edge of the window
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= window_height:
        ball_velocity_y = -ball_velocity_y

    # Check for collision with the right or left edge of the window
    if ball_x + ball_radius >= window_width or ball_x - ball_radius <= 0:
        ball_velocity_x = -ball_velocity_x

    # Fill the window with white
    window.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(window, BLACK, (rect_x, rect_y, rect_width, rect_height))

    # Draw the ball
    pygame.draw.circle(window, BLACK, (int(ball_x), int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
