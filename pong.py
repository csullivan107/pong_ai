import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pygame Test")

# Set up colors
BLUE = (0, 0, 255)

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with white
    window.fill((255, 255, 255))

    # Draw a blue rectangle
    pygame.draw.rect(window, BLUE, (300, 200, 200, 100))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
