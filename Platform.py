import pygame

class Platform:
    """
    Represents the platform in the Arkanoid game.
    """

    def __init__(self, x, y, speed):
        """
        Initializes the platform.
        Parameters:
        x (int): X-coordinate of the platform.
        y (int): Y-coordinate of the platform.
        speed (int): Movement speed of the platform.
        """
        self.image = pygame.image.load('Images/platform.png')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def draw(self, screen):
        """
        Draws the platform on the screen.
        Parameters:
        screen (pygame.Surface): The screen to draw on.
        """
        screen.blit(self.image, self.rect)

    def move(self, direction):
        """
        Moves the platform left or right.
        Parameters:
        direction (str): 'left' or 'right'.
        """
        if direction == "left":
            self.rect.x -= self.speed
        elif direction == "right":
            self.rect.x += self.speed


