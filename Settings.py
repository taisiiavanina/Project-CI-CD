import pygame
import sys

BG_COLOR = (255, 240, 245)
BUTTON_COLOR = (211, 211, 211)
HOVER_COLOR = (192, 192, 192)

class Settings:
    def __init__(self):
        self.difficulty = "easy"
        self.background_color = BG_COLOR

    def change_difficulty(self, difficulty):
        self.difficulty = difficulty
        print(f"Difficulty changed to {self.difficulty}")

    def change_background_color(self, color):
        self.background_color = color
        print(f"Background color changed to {self.background_color}")


class SettingsScreen:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.font = pygame.font.SysFont("Arial", 30)

        self.buttons = {
            "Change Difficulty": pygame.Rect(100, 200, 200, 50),
            "Color Palette": pygame.Rect(100, 300, 200, 50),
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

        self.palette_rects = [pygame.Rect(350 + i * 40, 300, 30, 30) for i in range(len(self.color_palette))]

        self.using_eyedropper = False


    def draw(self):
        self.screen.fill(self.settings.background_color)

        title = self.font.render("Settings", True, (0, 0, 0))
        self.screen.blit(title, (self.screen.get_width() // 2 - title.get_width() // 2, 50))

        for text, rect in self.buttons.items():
            pygame.draw.rect(self.screen, BUTTON_COLOR, rect)
            label = self.font.render(text, True, (0, 0, 0))
            self.screen.blit(label, (rect.x + 10, rect.y + 10))

        for i, rect in enumerate(self.palette_rects):
            pygame.draw.rect(self.screen, self.color_palette[i], rect)

        if self.using_eyedropper:
            hint = self.font.render("Click anywhere to pick a color!", True, (255, 0, 0))
            self.screen.blit(hint, (200, 500))

        pygame.display.flip()

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if self.using_eyedropper:
                color = self.screen.get_at(mouse_pos)[:3]
                self.settings.change_background_color(color)
                self.using_eyedropper = False
                return None

            if self.buttons["Change Difficulty"].collidepoint(mouse_pos):
                new_difficulty = "Easy" if self.settings.difficulty == "Medium" else "Hard"
                self.settings.change_difficulty(new_difficulty)
                wall.update_wall()
            elif self.buttons["Color Palette"].collidepoint(mouse_pos):
                self.using_eyedropper = True
            elif self.buttons["Back"].collidepoint(mouse_pos):
                return "main_menu"

            for i, rect in enumerate(self.palette_rects):
                if rect.collidepoint(mouse_pos):
                    self.settings.change_background_color(self.color_palette[i])

        return None

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game with Settings")

    settings = Settings()
    wall = Wall(settings)
    settings_screen = SettingsScreen(screen, settings)

    main_menu = True
    settings_menu = False
    clock = pygame.time.Clock()

    while True:
        if main_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if pygame.Rect(300, 250, 200, 50).collidepoint(mouse_pos):
                        main_menu = False
                        settings_menu = True

            screen.fill(settings.background_color)
            pygame.draw.rect(screen, BUTTON_COLOR, pygame.Rect(300, 250, 200, 50))
            label = pygame.font.SysFont("Arial", 30).render("Settings", True, (0, 0, 0))
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
