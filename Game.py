import pygame
from PlatformObject import PlatformObject  # Імпортуємо клас платформи

# Константи розміру вікна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Game:
    """
    Main game class responsible for initializing the window, handling events, and updating the game state.
    """

    def __init__(self):
        """
        Initializes the game window, platform, and game loop components.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Arkanoid")
        self.clock = pygame.time.Clock()

        # Створення платформи
        self.platform_object = PlatformObject(x=350, y=550, width=100, height=10, speed=7, color=(255, 0, 0))

    def process_input(self):
        """
        Handles user input, including key presses for platform movement.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.platform_object.move("left", SCREEN_WIDTH)
        if keys[pygame.K_RIGHT]:
            self.platform_object.move("right", SCREEN_WIDTH)

    def update_game_state(self):
        """
        Updates game logic, such as platform movement.
        """
        pass  # Тут будуть оновлення гри в майбутньому

    def render(self):
        """
        Draws all game objects on the screen.
        """
        self.screen.fill((0, 0, 0))  # Очищення екрану (чорний фон)
        self.platform_object.draw(self.screen)  # Малюємо платформу
        pygame.display.flip()  # Оновлення екрану

    def game_loop(self):
        """
        Runs the main game loop, handling events, updating logic, and rendering the game.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.process_input()  # Обробка введення
            self.update_game_state()  # Оновлення логіки
            self.render()  # Малювання

            self.clock.tick(60)  # Обмеження FPS до 60

        pygame.quit()


# Запуск гри
if __name__ == "__main__":
    game = Game()
    game.game_loop()
