"""
This file contains the main entry point for the Asteroids game. 
It initializes the game, handles user input, updates game state, 
and renders the game to the screen.
"""

# Import necessary modules
import pygame  # Pygame library for game development
from asteroid import Asteroid  # Class representing an asteroid
from asteroidfield import AsteroidField  # Class managing the asteroid field
from player import Player  # Class representing the player's spaceship
from constants import *  # Import all constants defined in constants.py
from shot import Shot  # Class representing a shot fired by the player


def main():
    """
    This is the main function of the Asteroids game. 
    It initializes Pygame, creates the game window, 
    sets up the game objects, and runs the main game loop.
    """

    # Initialize Pygame
    pygame.init()  # Initializes all imported Pygame modules

    # Print some debug information to the console
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")  # Print the screen width
    print(f"Screen height: {SCREEN_HEIGHT}")  # Print the screen height

    # Create the game window
    # The screen variable represents the game window's surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the initial position of the player to the center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Create sprite groups for updatable and drawable objects
    # Sprite groups are used to efficiently manage and update multiple sprites
    # updatable group contains sprites that need to be updated every frame
    updatable = pygame.sprite.Group()  
    # drawable group contains sprites that need to be drawn every frame
    drawable = pygame.sprite.Group()  
    # asteroids group contains all asteroid sprites
    asteroids = pygame.sprite.Group()  
    # shots group contains all shot sprites
    shots = pygame.sprite.Group()  

    # Set the sprite groups for the Player, Asteroid, and AsteroidField classes
    # This allows us to add instances of these classes to the appropriate groups
    # when they are created
    Player.containers = (updatable, drawable)  # Player sprites are updatable and drawable
    Asteroid.containers = (updatable, drawable, asteroids)  # Asteroid sprites are updatable, drawable, and belong to the asteroids group
    AsteroidField.containers = (updatable)  # AsteroidField is updatable (it spawns asteroids)
    Shot.containers = (updatable, drawable, shots)  # Shot sprites are updatable, drawable, and belong to the shots group

    # Create the player object
    pl = Player(x, y)  # Create a Player instance at the center of the screen

    # Create the asteroid field object
    af = AsteroidField()  # Create an AsteroidField instance

    # Add the player to the updatable and drawable groups
    updatable.add(pl)  # Add the player to the updatable group
    drawable.add(pl)  # Add the player to the drawable group

    # Draw the player on the screen initially
    pl.draw(screen)  # Draw the player on the screen

    # Create a clock object to track time
    time = pygame.time.Clock()  # Create a Clock object to control the frame rate

    # Initialize the delta time (time since last frame)
    dt = 0  # Delta time (time elapsed since the last frame)

    # Main game loop
    while True:
        # Handle events
        for event in pygame.event.get():  # Get all events from the event queue
            # If the user closes the window, exit the game
            if event.type == pygame.QUIT:  # If the event type is QUIT (window close)
                return  # Exit the main function, ending the game

        # Clear the screen
        screen.fill("black")  # Fill the screen with black color

        # Update all updatable objects
        for sprite in updatable:  # Iterate through all sprites in the updatable group
            sprite.update(dt)  # Call the update method of each sprite, passing the delta time

        # Check for collisions between asteroids and the player
        for sprite in asteroids:  # Iterate through all sprites in the asteroids group
            if sprite.does_collide(pl):  # Check if the asteroid collides with the player
                print("Game Over!")  # Print "Game Over!" to the console
                exit()  # Exit the game
            for shot in shots:  # Iterate through all sprites in the shots group
                if sprite.does_collide(shot):  # Check if the asteroid collides with a shot
                    sprite.split()  # Split the asteroid into smaller asteroids
                    shot.kill()  # Remove the shot from the game

        # Draw all drawable objects
        for sprite in drawable:  # Iterate through all sprites in the drawable group
            sprite.draw(screen)  # Call the draw method of each sprite, passing the screen surface

        # Update the display
        pygame.display.flip()  # Update the entire screen content

        # Calculate the delta time
        dt = (time.tick(60)) / 1000  # Limit the frame rate to 60 FPS and calculate the delta time

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly
