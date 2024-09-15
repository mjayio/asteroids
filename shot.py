"""
This module defines the `Shot` class, which represents a projectile fired by the player's spaceship in the Asteroids game.
The shots are used to destroy asteroids.

The `Shot` class inherits from the `CircleShape` class, which provides basic functionality for circular game objects
such as position, velocity, radius, drawing, updating, and collision detection.
"""

# Import the Pygame library for game development.
# Pygame provides functionality for graphics, sound, input, and more.
import pygame

# Import the `CircleShape` class from the `circleshape` module.
# The `CircleShape` class provides basic functionality for circular game objects,
# such as position, velocity, radius, drawing, updating, and collision detection.
# We will inherit from this class to create our `Shot` class.
from circleshape import CircleShape

# Import the `SHOT_RADIUS` constant from the `constants` module.
# This module contains various constants used throughout the game,
# such as player properties (e.g., speed, radius, shot cooldown),
# screen dimensions, asteroid properties, and more.
from constants import SHOT_RADIUS


class Shot(CircleShape):
    """
    Represents a shot fired by the player's spaceship in the game.

    The `Shot` class inherits from the `CircleShape` class, which provides basic functionality
    for circular game objects such as position, velocity, radius, drawing, updating, and collision detection.

    Attributes:
        position (pygame.Vector2): The position of the shot's center.
        velocity (pygame.Vector2): The velocity of the shot.
        radius (int): The radius of the shot.
    """

    def __init__(self, x, y, radius=SHOT_RADIUS):
        """
        Initializes a new Shot object.

        Args:
            x (int): The initial x-coordinate of the shot's center.
            y (int): The initial y-coordinate of the shot's center.
            radius (int, optional): The radius of the shot. Defaults to SHOT_RADIUS.
        """
        # Call the constructor of the parent class (CircleShape) to initialize the position, velocity, and radius.
        # The shot's radius is defined by the `SHOT_RADIUS` constant in the `constants` module.
        super().__init__(x, y, radius)

    def draw(self, screen):
        """
        Draws the shot on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the shot on.
                This is the Pygame surface representing the game window.
        """
        # Draw the shot as a white circle with a width of 2 pixels.
        # The `pygame.draw.circle()` function is used to draw a circle on a surface.
        # The first argument is the surface to draw on, the second argument is the color of the circle ("white" in this case),
        # the third argument is the position of the circle's center (self.position),
        # the fourth argument is the radius of the circle (self.radius),
        # and the fifth argument is the width of the circle's outline in pixels (2 in this case).
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        """
        Updates the shot's position based on its velocity and the elapsed time.

        Args:
            dt (float): The time elapsed since the last frame in seconds.
                This is used to ensure that the shot moves at a consistent speed regardless of the frame rate.
        """
        # Update the shot's position based on its velocity and the elapsed time.
        # The shot's velocity is a `pygame.Vector2` object representing the shot's speed and direction.
        # Multiplying the velocity by `dt` gives us the displacement vector,
        # which is then added to the shot's current position to update its position.
        self.position += self.velocity * dt
