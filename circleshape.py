import pygame

# Base class for circular game objects.
# This class inherits from pygame.sprite.Sprite, which is a built-in class
# in Pygame for handling sprites (graphical objects in a game).
class CircleShape(pygame.sprite.Sprite):
    """
    Represents a circular shape in the game.

    This class serves as the base class for other circular game objects
    like asteroids, the player, and shots. It provides common functionality
    such as position, velocity, radius, drawing, updating, and collision
    detection.

    Attributes:
        position (pygame.Vector2): The position of the circle's center.
        velocity (pygame.Vector2): The velocity of the circle.
        radius (int): The radius of the circle.
    """

    def __init__(self, x, y, radius):
        """
        Initializes a new CircleShape object.

        Args:
            x (int): The x-coordinate of the circle's center.
            y (int): The y-coordinate of the circle's center.
            radius (int): The radius of the circle.
        """

        # Call the constructor of the parent class (pygame.sprite.Sprite).
        # If the 'containers' attribute is defined (which will be the case
        # for objects that are part of sprite groups), we pass it to the
        # parent constructor so that the object is automatically added to
        # those groups. Otherwise, we just call the parent constructor
        # without any arguments.
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Initialize the position, velocity, and radius of the circle.
        # pygame.Vector2 is a class from Pygame that represents a 2D vector.
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """
        Draws the circle on the screen.

        This method is intended to be overridden by subclasses to provide
        specific drawing logic for each type of circular object.

        Args:
            screen (pygame.Surface): The surface to draw the circle on.
        """
        # Subclasses must override this method to draw the circle.
        pass

    def update(self, dt):
        """
        Updates the circle's position based on its velocity and time elapsed.

        This method is intended to be overridden by subclasses to provide
        specific update logic for each type of circular object.

        Args:
            dt (float): The time elapsed since the last update (in seconds).
        """
        # Subclasses must override this method to update the circle.
        pass

    def does_collide(self, other):
        """
        Checks if this circle collides with another circle.

        Args:
            other (CircleShape): The other circle to check for collision with.

        Returns:
            bool: True if the circles collide, False otherwise.
        """
        # Calculate the distance between the centers of the two circles.
        distance = self.position.distance_to(other.position)
        # Check if the distance is less than the sum of the radii.
        return distance < self.radius + other.radius
