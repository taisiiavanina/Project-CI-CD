import pytest
import pygame
from unittest.mock import MagicMock, patch
from Game import Game
from PlatformObject import PlatformObject
from Ball import Ball
from Wall import Wall
from Settings import Settings

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

@pytest.fixture
def game_instance():
    """Fixture to create a Game instance."""
    pygame.init()
    return Game()

@pytest.mark.parametrize("difficulty", ["easy", "medium", "hard"])
def test_game_initialization(difficulty):
    """Tests if the game initializes correctly with different difficulty levels."""
    pygame.init()
    game = Game(difficulty=difficulty)
    assert game.difficulty == difficulty

@patch("pygame.display.set_mode", return_value=MagicMock())
def test_render(mock_display, game_instance):
    """Tests if rendering methods are called correctly."""
    game_instance.screen = MagicMock()
    game_instance.screen.fill((0, 0, 0))
    game_instance.screen.fill.assert_called_once_with((0, 0, 0))

@patch("pygame.key.get_pressed", return_value={pygame.K_LEFT: True, pygame.K_RIGHT: False})
def test_process_input(mock_keys, game_instance):
    """Tests if the platform moves when the left arrow key is pressed."""
    game_instance.platform_object.move = MagicMock()
    game_instance.process_input()
    game_instance.platform_object.move.assert_called_once_with("left", SCREEN_WIDTH)

@patch("pygame.key.get_pressed", return_value={pygame.K_LEFT: False, pygame.K_RIGHT: True})
def test_platform_moves_right(mock_keys, game_instance):
    """Tests if the platform moves right when the right arrow key is pressed."""
    game_instance.platform_object.move = MagicMock()
    game_instance.process_input()
    game_instance.platform_object.move.assert_called_once_with("right", SCREEN_WIDTH)
