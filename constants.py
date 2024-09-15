"""
This file defines various constants used throughout the Asteroids game. 
Constants are values that do not change during the game's execution. 
Using constants makes the code more readable, maintainable, and easier to modify.
For example, if we want to change the screen size, we only need to modify it here.
"""

# Screen dimensions
SCREEN_WIDTH = 1280  # Width of the game window in pixels
SCREEN_HEIGHT = 720  # Height of the game window in pixels

# Asteroid properties
ASTEROID_MIN_RADIUS = 20  # Minimum radius of an asteroid in pixels
ASTEROID_KINDS = 3       # Number of different asteroid sizes (e.g., small, medium, large)
ASTEROID_SPAWN_RATE = 0.8  # Average time between asteroid spawns in seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS  # Maximum radius of an asteroid, calculated based on the minimum radius and the number of asteroid kinds

# Player properties
PLAYER_RADIUS = 20        # Radius of the player's ship in pixels
PLAYER_TURN_SPEED = 300  # Player's turning speed in degrees per second
PLAYER_SPEED = 200      # Player's movement speed in pixels per second

# Shot (projectile) properties
SHOT_RADIUS = 5            # Radius of a shot fired by the player in pixels
PLAYER_SHOT_SPEED = 500   # Speed of a shot fired by the player in pixels per second
PLAYER_SHOT_COOLDOWN = 0.3  # Minimum time between shots fired by the player in seconds