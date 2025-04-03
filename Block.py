import pygame
import random


class Block:
    """
    Represents a single block in the game with a random color.
    """

    def __init__(self, x, y, width=50, height=20, points=10):
        """
        Initializes a block with a random color.
        Parameters:
        x (int): X-coordinate of the block.
        y (int): Y-coordinate of the block.
        width (int): Width of the block (default: 50).
        height (int): Height of the block (default: 20).
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.color = self.random_color()
        self.points = random.randint(5, 20)

    def random_color(self):
        """
        Generates a random bright color for the block.
        Returns:
        tuple: RGB color.
        """
        return (random.randint(50, 255), random.randint(50, 255),
                random.randint(50, 255))

    def draw(self, screen):
        """
        Draws the block on the screen.
        Parameters:
        screen (pygame.Surface): The screen to draw on.
        """
        pygame.draw.rect(screen, self.color, self.rect)
