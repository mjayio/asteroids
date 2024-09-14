import pygame
import random
from asteroid import Asteroid
from constants import *

"""
This module implements the AsteroidField class, which is responsible for
spawning and managing asteroids in the game.

The AsteroidField class spawns asteroids at random intervals and positions
along the edges of the screen. The asteroids have random sizes and velocities.

The class also handles the collision detection between asteroids and the player.
"""

class AsteroidField(pygame.sprite.Sprite):
    """
    Manages the spawning and updating of asteroids in the game.

    Asteroids are spawned at random intervals and positions along the edges
    of the screen, with random sizes and velocities.
    """

    # Define the edges of the screen where asteroids can spawn.
    # Each edge is represented by a list containing:
    # - A normalized vector pointing outwards from the edge.
    # - A lambda function that calculates the spawn position along the edge
    #   based on a random value between 0 and 1.
    edges = [
        [
            pygame.Vector2(1, 0),  # Right edge
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),  # Left edge
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),  # Bottom edge
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),  # Top edge
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        """
        Initializes the AsteroidField.
        """
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        """
        Spawns a new asteroid with the given radius, position, and velocity.

        Args:
            radius (int): The radius of the asteroid.
            position (pygame.Vector2): The position of the asteroid.
            velocity (pygame.Vector2): The velocity of the asteroid.
        """
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        """
        Updates the AsteroidField, spawning new asteroids at intervals.

        Args:
            dt (float): The time elapsed since the last update.
        """
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # Spawn a new asteroid at a random edge.
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)  # Random speed
            velocity = edge[0] * speed  # Initial velocity along the edge
            velocity = velocity.rotate(random.randint(-30, 30))  # Add random deviation
            position = edge[1](random.uniform(0, 1))  # Random position along the edge
            kind = random.randint(1, ASTEROID_KINDS)  # Random asteroid size
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)