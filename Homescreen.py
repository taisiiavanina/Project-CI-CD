import pygame
import sys
from Game import Game
from Settings import Settings
from Settings import SettingsScreen

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Arkanoid')

BG_COLOR = (255, 240, 245)

BUTTON_COLOR = (211, 211, 211)
HOVER_COLOR = (192, 192, 192)

font = pygame.font.SysFont('Arial', 40)

def draw_button(text, x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) // 2))

def main_menu():
    clock = pygame.time.Clock()
    running = True

    settings = Settings()

    while running:
        screen.fill(settings.background_color)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        start_button = pygame.Rect(300, 200, 200, 50)
        settings_button = pygame.Rect(300, 300, 200, 50)
        quit_button = pygame.Rect(300, 400, 200, 50)

        if start_button.collidepoint(mouse_x, mouse_y):
            draw_button("Start", 300, 200, 200, 50, HOVER_COLOR)
        else:
            draw_button("Start", 300, 200, 200, 50, BUTTON_COLOR)

        if settings_button.collidepoint(mouse_x, mouse_y):
            draw_button("Settings", 300, 300, 200, 50, HOVER_COLOR)
        else:
            draw_button("Settings", 300, 300, 200, 50, BUTTON_COLOR)

        if quit_button.collidepoint(mouse_x, mouse_y):
            draw_button("Exit", 300, 400, 200, 50, HOVER_COLOR)
        else:
            draw_button("Exit", 300, 400, 200, 50, BUTTON_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    print("Гра починається!")
                    game = Game()
                    game.game_loop()
                    #running = False
                if settings_button.collidepoint(event.pos):
                    print("Перехід до налаштувань!")
                    settings = Settings()
                    settings_screen = SettingsScreen(screen, settings)

                    # Запускаємо цикл екрану налаштувань
                    settings_running = True
                    while settings_running:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            # Обробка подій у налаштуваннях
                            result = settings_screen.handle_events(event)
                            if result == "main_menu":
                                settings_running = False  # Вихід з екрану налаштувань

                        settings_screen.draw()
                        pygame.display.update()

                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)

main_menu()