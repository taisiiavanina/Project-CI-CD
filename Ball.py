import pygame
import math


class Ball:
    """
    Class representing the ball in the game.
    """

    def __init__(self, x, y, radius=8, speed=3, color=(255, 255, 0)):
        """
        Initializes the ball.
        :param x: Initial X position
        :param y: Initial Y position
        :param radius: Ball size
        :param speed: Initial speed
        :param color: Ball color
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.dx = (math.cos
                   (math.radians(45)) * self.speed)
        self.dy = (-math.sin(math.radians(45))
                   * self.speed)
        self.color = color
        self.bonus_points = 0

    def move(self, screen_width, screen_height, platform, wall):
        """
        Moves the ball, checks for collisions, and updates speed.
        """
        self.x += self.dx
        self.y += self.dy

        # Відбивання від стін
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.dx = -self.dx

        # Відбивання від стелі
        if self.y - self.radius <= 0:
            self.dy = -self.dy

        # Перевірка зіткнення з платформою
        if (platform.rect.y <= self.y + self.radius
                <= platform.rect.y + platform.rect.height and
                platform.rect.x <= self.x <= platform.rect.x
                + platform.rect.width):
            self.dy = -self.dy
            self.y = platform.rect.y - self.radius

        for block in wall.blocks[:]:
            if (block.rect.x <= self.x
                    <= block.rect.x + block.rect.width
                    and block.rect.y <= self.y
                    <= block.rect.y + block.rect.height):
                self.dy = -self.dy
                wall.blocks.remove(block)
                self.bonus_points += block.points
                self.speed += 0.03
                self.dx = math.copysign(self.speed, self.dx)
                self.dy = math.copysign(self.speed, self.dy)

        if self.y > screen_height:
            return False

        if not wall.blocks:
            return "win"

        return True

    def draw(self, screen):
        """
        Draws the ball.
        """
        pygame.draw.circle(screen, self.color,
                           (int(self.x), int(self.y)), self.radius)

        glow_color = (255, 255, 100)
        pygame.draw.circle(
            screen, glow_color, (int(self.x), int(self.y)), self.radius + 3, 1
        )
