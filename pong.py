import pygame
import sys

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

    # Fill the window with white
    window.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(window, BLACK, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
