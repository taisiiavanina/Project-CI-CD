import pygame
from PlatformObject import PlatformObject
from Wall import Wall
from Ball import Ball
from Settings import Settings

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Game:
    """
    Main game class responsible for initializing the window, handling events, and updating the game state.
    """

    def __init__(self, difficulty="easy", settings=None):
        self.difficulty = difficulty
        self.settings = settings if settings else Settings()
        self.wall = Wall(difficulty)
        self.ball = Ball(x=400, y=300)
        self.platform_object = PlatformObject(x=350, y=550, width=100, height=10, speed=7, color=(255, 0, 0))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Arkanoid")
        self.paused = False

        self.font = pygame.font.Font(None, 36)

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
        Updates game logic, such as platform movement and ball movement.
        """
        status = self.ball.move(SCREEN_WIDTH, SCREEN_HEIGHT, self.platform_object, self.wall)

        if status == "win":
            self.show_end_screen(f"Ви виграли! Бали: {self.ball.bonus_points}")

        elif not status:
            self.show_end_screen(f"Гра закінчена! Бали: {self.ball.bonus_points}")

    def show_end_screen(self, message):
        """
        Displays the end game screen and returns to the menu after a delay.
        """
        self.screen.fill((0, 0, 0))
        text = self.font.render(message, True, (255, 255, 255))
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
        pygame.display.flip()

        pygame.time.delay(3000)

        from Homescreen import main_menu
        main_menu(self.difficulty)


    def render(self):
        """
        Draws all game objects on the screen.
        """
        self.screen.fill(self.settings.background_color)
        self.platform_object.draw(self.screen)
        self.wall.draw(self.screen)
        self.ball.draw(self.screen)

        score_text = self.font.render(f"Бали: {self.ball.bonus_points}", True, (255, 255, 255))
        self.screen.blit(score_text, (20, 20))

        if self.paused:
            pause_font = pygame.font.Font(None, 74)
            pause_text = pause_font.render("PAUSE", True, (255, 255, 255))
            self.screen.blit(pause_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))

        pygame.display.flip()

    def game_loop(self):
        """
        Runs the main game loop, handling events, updating logic, and rendering the game.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.paused = not self.paused

            if not self.paused:
                self.process_input()
                self.update_game_state()

            self.render()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    settings = Settings()
    game = Game(settings=settings)
    game.game_loop()
