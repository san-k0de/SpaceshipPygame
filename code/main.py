import pygame
from os.path import join
from random import randint

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
# Player
player_surf = pygame.image.load(join("images", "player.png")).convert_alpha() # loading image from path; using convert() as image has no transparent pixels
player_rect = player_surf.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

# Stars
star_surf = pygame.image.load(join("images", "star.png")).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

# Run the window
while running:
    # Create event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game
    displaySurface.fill("cadetblue3")
    for pos in star_positions:
        displaySurface.blit(star_surf, pos)
    player_rect.left += 0.2
    displaySurface.blit(player_surf, player_rect) # blit is block image transfer
    pygame.display.update()

# Close the game   
pygame.quit() # Uninitializes everything to close the game properly


# EXTRA NOTES
# If image has no transparent pixels -> .convert()
# If image has transparent pixels -> .convert_alpha()