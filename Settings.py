import pygame
import sys

BG_COLOR = (255, 240, 245)
BUTTON_COLOR = (211, 211, 211)
HOVER_COLOR = (192, 192, 192)


class Settings:
    """
    Class to store and manage game settings.
    """
    def __init__(self):
        """
        Initializes the settings with a default background color.
        """
        self.background_color = BG_COLOR

    def change_background_color(self, color):
        """
        Changes the background color.
        :param color: Tuple representing RGB values.
        """
        self.background_color = color
        print(f"Background color changed to {self.background_color}")


class SettingsScreen:
    """
    Class to manage the settings screen.
    """
    def __init__(self, screen, settings):
        """
        Initializes the settings screen with buttons and color palette.
        :param screen: The main game screen.
        :param settings: Settings instance to apply changes.
        """
        self.screen = screen
        self.settings = settings
        self.font = pygame.font.SysFont("Arial", 30)

        self.buttons = {
            "Color Palette": pygame.Rect(100, 200, 200, 50),
            "Back": pygame.Rect(100, 400, 200, 50),
        }

        self.color_palette = [
            (255, 182, 193),
            (176, 224, 230),
            (255, 228, 225),
            (255, 239, 184),
            (255, 182, 193),
            (216, 191, 216),
            (144, 238, 144),
            (255, 240, 245),
            (211, 211, 211)
        ]

        self.palette_rects = [pygame.Rect(350 + i * 40, 200, 30, 30)
                              for i in range(len(self.color_palette))]

        self.using_eyedropper = False

    def draw(self):
        """
        Draws the settings screen.
        """
        self.screen.fill(self.settings.background_color)
        title = self.font.render("Settings", True, (0, 0, 0))
        self.screen.blit(title, (self.screen.get_width() // 2
                                 - title.get_width() // 2, 50))

        for text, rect in self.buttons.items():
            pygame.draw.rect(self.screen, BUTTON_COLOR, rect)
            label = self.font.render(text, True, (0, 0, 0))
            self.screen.blit(label, (rect.x + 10, rect.y + 10))

        for i, rect in enumerate(self.palette_rects):
            pygame.draw.rect(self.screen, self.color_palette[i], rect)

        if self.using_eyedropper:
            hint = self.font.render("Click anywhere to pick a color!",
                                    True, (255, 0, 0))
            self.screen.blit(hint, (200, 500))

        pygame.display.flip()

    def handle_events(self, event):
        """
        Handles user interactions with the settings screen.
        :param event: Pygame event instance.
        :return: Returns "main_menu".
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if self.using_eyedropper:
                color = self.screen.get_at(mouse_pos)[:3]
                self.settings.change_background_color(color)
                self.using_eyedropper = False
                return None

            elif self.buttons["Color Palette"].collidepoint(mouse_pos):
                self.using_eyedropper = True
            elif self.buttons["Back"].collidepoint(mouse_pos):
                return "main_menu"

            for i, rect in enumerate(self.palette_rects):
                if rect.collidepoint(mouse_pos):
                    self.settings.change_background_color(
                        self.color_palette[i]
                    )
                    self.screen.fill(self.settings.background_color)
                    pygame.display.flip()

        return None


def main():
    """
    Main function to initialize and run the game loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game with Settings")

    settings = Settings()
    settings_screen = SettingsScreen(screen, settings)

    main_menu = True
    settings_menu = False
    clock = pygame.time.Clock()

    while True:
        if main_menu:
            screen.fill(settings.background_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if pygame.Rect(300, 250, 200, 50).collidepoint(mouse_pos):
                        main_menu = False
                        settings_menu = True

            pygame.draw.rect(screen,
                             BUTTON_COLOR, pygame.Rect(300, 250, 200, 50)
                             )
            label = pygame.font.SysFont("Arial", 30).render(
                "Settings", True, (0, 0, 0)
            )
            screen.blit(label, (350, 265))

            pygame.display.flip()
            clock.tick(60)

        elif settings_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                result = settings_screen.handle_events(event)
                if result == "main_menu":
                    main_menu = True
                    settings_menu = False

            settings_screen.draw()
            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    main()
