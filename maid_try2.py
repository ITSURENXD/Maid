import pygame
from pygame.locals import *
import os

# Initialize Pygame
pygame.init()

# Set the window dimensions
window_width = 800
window_height = 600

# Create the window with transparency support
window = pygame.display.set_mode((window_width, window_height), pygame.SRCALPHA)
pygame.display.set_caption("Animated PNG Sequence")

# Set the path to the folder containing the PNG images
image_folder = "maid"

# Get the list of PNG image files in the folder
image_files = sorted([file for file in os.listdir(image_folder) if file.endswith(".gif")])

# Load the images into a list
images = []
for file in image_files:
    image_path = os.path.join(image_folder, file)
    image = pygame.image.load(image_path).convert_alpha()
    images.append(image)

# Set the frame rate (adjust as needed)
frame_rate = 20

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Main animation loop
running = True
frame_index = 0
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear the window (with transparency)
    window.fill((0, 0, 0, 0))

    # Draw the current frame
    window.blit(images[frame_index], (0, 0))

    # Update the frame index for the next iteration
    frame_index = (frame_index + 1) % len(images)

    # Update the window display
    pygame.display.update()

    # Delay to achieve the desired frame rate
    clock.tick(frame_rate)

# Quit the program
pygame.quit()
