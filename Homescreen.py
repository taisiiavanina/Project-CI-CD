import pygame
import sys
from Game import Game
from Settings import Settings
from Settings import SettingsScreen
from Complexity import Complexity
from Wall import Wall

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Arkanoid')

BG_COLOR = (255, 240, 245)

BUTTON_COLOR = (211, 211, 211)
HOVER_COLOR = (192, 192, 192)

font = pygame.font.SysFont('Arial', 40)


def draw_button(text, x, y, width, height, color):
    """
    Draws a button on the screen with the specified text, position, size, and color.

    :param text: The text to display on the button.
    :param x: The x-coordinate of the button.
    :param y: The y-coordinate of the button.
    :param width: The width of the button.
    :param height: The height of the button.
    :param color: The color of the button.
    """
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface,
                (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) // 2))


def main_menu(selected_difficulty):
    """
    Displays the main menu with options to start the game, access settings, or quit.
    """
    clock = pygame.time.Clock()
    running = True
    settings = Settings()
    settings_screen = SettingsScreen(screen, settings)

    while running:
        screen.fill(settings.background_color)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        start_button = pygame.Rect(300, 200, 200, 50)
        settings_button = pygame.Rect(300, 300, 200, 50)
        quit_button = pygame.Rect(300, 400, 200, 50)

        draw_button("Start", 300, 200, 200, 50, HOVER_COLOR if start_button.collidepoint(mouse_x, mouse_y) else BUTTON_COLOR)
        draw_button("Settings", 300, 300, 200, 50, HOVER_COLOR if settings_button.collidepoint(mouse_x, mouse_y) else BUTTON_COLOR)
        draw_button("Exit", 300, 400, 200, 50, HOVER_COLOR if quit_button.collidepoint(mouse_x, mouse_y) else BUTTON_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    game = Game(selected_difficulty, settings)
                    game.game_loop()
                if settings_button.collidepoint(event.pos):
                    settings_running = True
                    while settings_running:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            result = settings_screen.handle_events(event)
                            if result == "main_menu":
                                settings_running = False

                        settings_screen.draw()
                        pygame.display.update()

                    screen.fill(settings.background_color)
                    pygame.display.update()
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)


# The user first selects the difficulty level
complexity = Complexity()
complexity.select_difficulty()  # Method to select difficulty level
selected_difficulty = complexity.get_difficulty()  # Get selected difficulty level

main_menu(selected_difficulty)
