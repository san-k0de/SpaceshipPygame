import pygame

# General setup
pygame.init() # Initializes pygame

# Create the display surface
pygame.display.set_caption("Spaceship Game") # Add a title to the game window
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 # Set resolution
displaySurface = pygame.display.set_mode((1280, 720))
running = True

# Create plain surface
surf = pygame.Surface((100, 200)) # tuple of dimensions; needs to be attached to display surface
surf.fill("orange")
x = 100

# Import image

# Run the window
while running:
    # Create event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game
    displaySurface.fill("cadetblue3")
    x += 0.1
    displaySurface.blit(surf, (x, 150)) # blit is block image transfer
    pygame.display.update()

# Close the game   
pygame.quit() # Uninitializes everything to close the game properly