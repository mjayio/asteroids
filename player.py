"""
This module defines the `Player` class, which represents the player's spaceship in the Asteroids game.
The player can move, rotate, and shoot projectiles to destroy asteroids.
"""

# Import the `CircleShape` class from the `circleshape` module.
# The `CircleShape` class provides basic functionality for circular game objects,
# such as position, velocity, radius, drawing, updating, and collision detection.
# We will inherit from this class to create our `Player` class.
import circleshape as cshape

# Import the Pygame library for game development.
# Pygame provides functionality for graphics, sound, input, and more.
import pygame

# Import all constants from the `constants` module.
# This module contains various constants used throughout the game,
# such as player properties (e.g., speed, radius, shot cooldown),
# screen dimensions, and more.
from constants import *

# Import the `Shot` class from the `shot` module.
# The `Shot` class represents a projectile fired by the player.
from shot import Shot


class Player(cshape.CircleShape):
    """
    Represents the player's spaceship in the game.

    The `Player` class inherits from the `CircleShape` class, which provides basic functionality
    for circular game objects such as position, velocity, radius, drawing, updating, and collision detection.

    Attributes:
        rotation (float): The rotation angle of the spaceship in degrees.
        shot_timer (float): The time remaining until the player can shoot again.
            This is used to implement a cooldown period between shots, preventing the player
            from shooting continuously.
    """

    def __init__(self, x, y):
        """
        Initializes a new Player object.

        Args:
            x (int): The initial x-coordinate of the spaceship's center.
            y (int): The initial y-coordinate of the spaceship's center.
        """
        # Call the constructor of the parent class (CircleShape) to initialize the position, velocity, and radius.
        # The player's radius is defined by the `PLAYER_RADIUS` constant in the `constants` module.
        super().__init__(x, y, PLAYER_RADIUS)

        # Initialize the rotation angle of the spaceship to 0 degrees.
        # This means the spaceship will initially be facing upwards.
        self.rotation = 0

        # Initialize the shot timer to 0.
        # This allows the player to shoot immediately when the game starts.
        self.shot_timer = 0

    def triangle(self):
        """
        Calculates the vertices of the triangle representing the spaceship's shape.

        The triangle's shape is determined by the spaceship's rotation angle and radius.
        The spaceship is represented as a triangle pointing in the direction of its rotation.

        Returns:
            list[pygame.Vector2]: A list of three `pygame.Vector2` objects representing the vertices of the triangle.
                Each `pygame.Vector2` object represents a point in 2D space with x and y coordinates.
        """
        # Calculate a unit vector pointing forward relative to the spaceship's rotation.
        # A unit vector has a length of 1.
        # We start with a vector pointing upwards (0, 1) and rotate it by the spaceship's rotation angle.
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        # Calculate a vector pointing to the right relative to the spaceship's rotation and scaled by the radius.
        # We start with a vector pointing upwards (0, 1), rotate it by 90 degrees clockwise (the spaceship's rotation angle + 90),
        # and then scale it by the spaceship's radius divided by 1.5.
        # This gives us a vector pointing to the right of the spaceship's forward direction,
        # with a length proportional to the spaceship's radius.
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        # Calculate the coordinates of the three vertices of the triangle.
        #
        # Vertex a: The tip of the triangle.
        # It is calculated by adding the forward vector (scaled by the radius) to the spaceship's position.
        a = self.position + forward * self.radius

        # Vertex b: The bottom left vertex of the triangle.
        # It is calculated by subtracting the forward vector (scaled by the radius) and the right vector from the spaceship's position.
        b = self.position - forward * self.radius - right

        # Vertex c: The bottom right vertex of the triangle.
        # It is calculated by subtracting the forward vector (scaled by the radius) and adding the right vector to the spaceship's position.
        c = self.position - forward * self.radius + right

        # Return the list of vertices.
        return [a, b, c]

    def draw(self, screen):
        """
        Draws the spaceship on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the spaceship on.
                This is the Pygame surface representing the game window.
        """
        # Draw the spaceship as a white triangle with a width of 2 pixels using the calculated vertices.
        # The `pygame.draw.polygon()` function is used to draw a polygon on a surface.
        # The first argument is the surface to draw on, the second argument is the color of the polygon ("white" in this case),
        # the third argument is a list of vertices representing the polygon's shape (obtained from the `triangle()` method),
        # and the fourth argument is the width of the polygon's outline in pixels (2 in this case).
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        """
        Rotates the spaceship by a certain angle based on the elapsed time.

        Args:
            dt (float): The time elapsed since the last frame in seconds.
                This is used to ensure that the spaceship rotates at a consistent speed regardless of the frame rate.
        """
        # Update the rotation angle based on the player's turn speed and the elapsed time.
        # The rotation speed is defined by the `PLAYER_TURN_SPEED` constant in the `constants` module.
        # Multiplying the turn speed by `dt` ensures that the rotation angle is proportional to the elapsed time.
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """
        Moves the spaceship forward or backward based on the elapsed time.

        Args:
            dt (float): The time elapsed since the last frame in seconds.
                This is used to ensure that the spaceship moves at a consistent speed regardless of the frame rate.
        """
        # Calculate a unit vector pointing forward relative to the spaceship's rotation.
        # A unit vector has a length of 1.
        # We start with a vector pointing upwards (0, 1) and rotate it by the spaceship's rotation angle.
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        # Update the spaceship's position based on its speed, the forward vector, and the elapsed time.
        # The spaceship's speed is defined by the `PLAYER_SPEED` constant in the `constants` module.
        # Multiplying the speed by `dt` ensures that the distance moved is proportional to the elapsed time.
        # Multiplying the forward vector by the speed and `dt` gives us the displacement vector,
        # which is then added to the spaceship's current position to update its position.
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        """
        Updates the spaceship's state based on user input and the elapsed time.

        Args:
            dt (float): The time elapsed since the last frame in seconds.
                This is used to ensure that the spaceship's movement and rotation are smooth and consistent
                regardless of the frame rate.
        """
        # Get the state of all keyboard keys.
        # This returns a dictionary-like object where each key is represented by a constant from the `pygame.locals` module
        # (e.g., `pygame.K_LEFT` for the left arrow key), and the value is True if the key is currently pressed, False otherwise.
        keys = pygame.key.get_pressed()

        # Rotate the spaceship left or right based on the left and right arrow keys.
        # If the left arrow key is pressed, rotate the spaceship counterclockwise by calling the `rotate()` method with a negative `dt` value.
        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        # If the right arrow key is pressed, rotate the spaceship clockwise by calling the `rotate()` method with a positive `dt` value.
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)

        # Move the spaceship forward or backward based on the up and down arrow keys.
        # If the up arrow key is pressed, move the spaceship forward by calling the `move()` method with a positive `dt` value.
        if keys[pygame.K_UP]:
            self.move(dt)
        # If the down arrow key is pressed, move the spaceship backward by calling the `move()` method with a negative `dt` value.
        if keys[pygame.K_DOWN]:
            self.move(-dt)

        # Shoot a projectile if the spacebar is pressed.
        # If the spacebar is pressed, call the `shoot()` method to fire a projectile.
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def shoot(self, dt):
        """
        Shoots a projectile from the spaceship.

        Args:
            dt (float): The time elapsed since the last frame in seconds.
                This is used to update the shot timer, which prevents the player from shooting continuously.
        """
        # Check if the shot timer has expired.
        # The shot timer is used to implement a cooldown period between shots.
        if self.shot_timer > 0:
            # If the timer is still active, decrement it by the elapsed time `dt` and return without shooting.
            self.shot_timer -= dt
            return

        # Create a new `Shot` object at the spaceship's current position.
        # The shot's radius is defined by the `SHOT_RADIUS` constant in the `constants` module.
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)

        # Set the shot's velocity based on the spaceship's rotation and the shot speed.
        # The shot speed is defined by the `PLAYER_SHOT_SPEED` constant in the `constants` module.
        # We start with a vector pointing upwards (0, 1), rotate it by the spaceship's rotation angle,
        # and then scale it by the shot speed.
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED

        # Reset the shot timer to the cooldown period, preventing the player from shooting again immediately.
        # The cooldown period is defined by the `PLAYER_SHOT_COOLDOWN` constant in the `constants` module.
        self.shot_timer = PLAYER_SHOT_COOLDOWN

