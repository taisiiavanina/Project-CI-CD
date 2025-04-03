import pygame


class PlatformObject:
    """
    Represents the platform in the game.
    """

    def __init__(self, x=400, y=550, width=100,
                 height=10, speed=5, color=(255, 0, 0)):
        """
        Initializes the platform.
        Parameters:
        x (int): X-coordinate of the platform (default: 400).
        y (int): Y-coordinate of the platform (default: 550).
        width (int): Width of the platform (default: 100).
        height (int): Height of the platform (default: 10).
        speed (int): Movement speed of the platform (default: 5).
        color (tuple): Color of the platform (default: red).
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.color = color  # Колір платформи

    def draw(self, screen):
        """
        Draws the platform on the screen.
        Parameters:
        screen (pygame.Surface): The screen to draw on.
        """
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, direction, screen_width):
        """
        Moves the platform left or right within screen boundaries.
        Parameters:
        direction (str): left, right.
        screen_width (int): Width of the game screen.
        """
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= self.speed
        elif direction == "right" and self.rect.right < screen_width:
            self.rect.x += self.speed
