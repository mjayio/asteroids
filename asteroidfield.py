import pygame
import random
from asteroid import Asteroid
from constants import *

"""
This module implements the `AsteroidField` class, which is responsible for
spawning and managing asteroids in the game.

The `AsteroidField` class spawns asteroids at random intervals and positions
along the edges of the screen. The asteroids have random sizes and velocities.

The class also handles the collision detection between asteroids and the player,
although this functionality is implemented in the `main.py` module.
"""

class AsteroidField(pygame.sprite.Sprite):
    """
    Manages the spawning and updating of asteroids in the game.

    Asteroids are spawned at random intervals and positions along the edges
    of the screen, with random sizes and velocities.

    Inherits from `pygame.sprite.Sprite`, which provides basic functionality
    for game objects that can be drawn and updated.
    """

    # Define the edges of the screen where asteroids can spawn.
    # Each edge is represented by a list containing two elements:
    # 1. A `pygame.Vector2` object representing a normalized vector pointing
    #    outwards from the edge. This vector is used to determine the initial
    #    direction of the asteroid's velocity.
    # 2. A lambda function that calculates the spawn position along the edge
    #    based on a random value between 0 and 1. This ensures that asteroids
    #    spawn at random positions along the edge.
    edges = [
        [
            pygame.Vector2(1, 0),  # Right edge: Vector pointing to the right.
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
            # Lambda function for the right edge:
            # - Takes a random value `y` between 0 and 1.
            # - Calculates the x-coordinate as `-ASTEROID_MAX_RADIUS`, which
            #   places the asteroid just off the right edge of the screen.
            # - Calculates the y-coordinate as `y * SCREEN_HEIGHT`, which
            #   places the asteroid at a random height along the right edge.
        ],
        [
            pygame.Vector2(-1, 0),  # Left edge: Vector pointing to the left.
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
            # Lambda function for the left edge:
            # - Takes a random value `y` between 0 and 1.
            # - Calculates the x-coordinate as `SCREEN_WIDTH + ASTEROID_MAX_RADIUS`,
            #   which places the asteroid just off the left edge of the screen.
            # - Calculates the y-coordinate as `y * SCREEN_HEIGHT`, which
            #   places the asteroid at a random height along the left edge.
        ],
        [
            pygame.Vector2(0, 1),  # Bottom edge: Vector pointing downwards.
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
            # Lambda function for the bottom edge:
            # - Takes a random value `x` between 0 and 1.
            # - Calculates the x-coordinate as `x * SCREEN_WIDTH`, which
            #   places the asteroid at a random width along the bottom edge.
            # - Calculates the y-coordinate as `-ASTEROID_MAX_RADIUS`, which
            #   places the asteroid just off the bottom edge of the screen.
        ],
        [
            pygame.Vector2(0, -1),  # Top edge: Vector pointing upwards.
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
            # Lambda function for the top edge:
            # - Takes a random value `x` between 0 and 1.
            # - Calculates the x-coordinate as `x * SCREEN_WIDTH`, which
            #   places the asteroid at a random width along the top edge.
            # - Calculates the y-coordinate as `SCREEN_HEIGHT + ASTEROID_MAX_RADIUS`,
            #   which places the asteroid just off the top edge of the screen.
        ],
    ]

    def __init__(self):
        """
        Initializes the `AsteroidField`.

        Calls the constructor of the parent class (`pygame.sprite.Sprite`)
        to initialize the sprite.

        Initializes the `spawn_timer` to 0.0. This timer is used to track
        the time elapsed since the last asteroid spawn.
        """
        # Call the constructor of the parent class, passing the `containers`
        # attribute. This adds the `AsteroidField` instance to the sprite groups
        # specified in `containers`.
        pygame.sprite.Sprite.__init__(self, self.containers)
        # Initialize the spawn timer to 0.0.
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        """
        Spawns a new asteroid with the given radius, position, and velocity.

        Args:
            radius (int): The radius of the asteroid.
            position (pygame.Vector2): The position of the asteroid.
            velocity (pygame.Vector2): The velocity of the asteroid.
        """
        # Create a new `Asteroid` instance with the given radius, position,
        # and velocity.
        asteroid = Asteroid(position.x, position.y, radius)
        # Set the velocity of the asteroid.
        asteroid.velocity = velocity

    def update(self, dt):
        """
        Updates the `AsteroidField`, spawning new asteroids at intervals.

        Args:
            dt (float): The time elapsed since the last update.
        """
        # Increment the spawn timer by the elapsed time.
        self.spawn_timer += dt
        # Check if it's time to spawn a new asteroid.
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            # Reset the spawn timer.
            self.spawn_timer = 0

            # Spawn a new asteroid at a random edge.
            # Choose a random edge from the `edges` list.
            edge = random.choice(self.edges)
            # Generate a random speed for the asteroid.
            speed = random.randint(40, 100)
            # Calculate the initial velocity of the asteroid along the chosen edge.
            velocity = edge[0] * speed
            # Add a random deviation to the velocity to make the asteroid's
            # movement less predictable.
            velocity = velocity.rotate(random.randint(-30, 30))
            # Calculate the spawn position of the asteroid along the chosen edge.
            position = edge[1](random.uniform(0, 1))
            # Determine the size of the asteroid (kind).
            kind = random.randint(1, ASTEROID_KINDS)
            # Spawn the asteroid with the calculated parameters.
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)