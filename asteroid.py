"""
This module defines the `Asteroid` class, which represents an asteroid in the Asteroids game.
Asteroids are space rocks that move around the screen and can collide with the player's ship.
When an asteroid is hit by a shot, it splits into two smaller asteroids.
"""

import pygame  # Import the Pygame library for game development
from circleshape import CircleShape  # Import the CircleShape class, which is the base class for Asteroid
import random  # Import the random module for generating random numbers
from constants import ASTEROID_MIN_RADIUS  # Import the ASTEROID_MIN_RADIUS constant, which defines the minimum radius of an asteroid


class Asteroid(CircleShape):
    """
    Represents an asteroid in the game.

    Inherits from `CircleShape`, which provides basic functionality for circular game objects
    such as position, velocity, radius, drawing, updating, and collision detection.

    Attributes:
        position (pygame.Vector2): The position of the asteroid's center.
        velocity (pygame.Vector2): The velocity of the asteroid.
        radius (int): The radius of the asteroid.
    """

    def __init__(self, x, y, radius):
        """
        Initializes a new Asteroid object.

        Args:
            x (int): The x-coordinate of the asteroid's center.
            y (int): The y-coordinate of the asteroid's center.
            radius (int): The radius of the asteroid.
        """
        # Call the constructor of the parent class (CircleShape) to initialize the position, velocity, and radius.
        super().__init__(x, y, radius)

    def draw(self, screen):
        """
        Draws the asteroid on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the asteroid on.
        """
        # Draw a white circle with a width of 2 pixels on the screen at the asteroid's position and with the asteroid's radius.
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        """
        Updates the asteroid's position based on its velocity and the elapsed time.

        Args:
            dt (float): The time elapsed since the last frame in seconds.
        """
        # Update the asteroid's position by adding its velocity multiplied by the elapsed time.
        self.position += self.velocity * dt

    def split(self):
        """
        Splits the asteroid into two smaller asteroids if its radius is greater than the minimum radius.

        If the asteroid's radius is less than or equal to the minimum radius, it is destroyed.
        Otherwise, it is destroyed and two new smaller asteroids are created at the same position with
        slightly different velocities and smaller radii.
        """
        if self.radius < ASTEROID_MIN_RADIUS:
            # If the asteroid is too small to split, destroy it.
            self.kill()
        else:
            # Destroy the current asteroid.
            self.kill()
            # Generate a random angle between 20 and 50 degrees.
            random_angle = random.uniform(20, 50)
            # Calculate the new velocities for the two smaller asteroids by rotating the current velocity by the random angle.
            new_velocity_1 = self.velocity.rotate(random_angle)
            new_velocity_2 = self.velocity.rotate(-random_angle)
            # Calculate the new radius for the smaller asteroids.
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            # Create two new Asteroid objects at the same position as the current asteroid with the new radius and velocities.
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            # Set the velocities of the new asteroids.
            asteroid_1.velocity = new_velocity_1
            asteroid_2.velocity = new_velocity_2
