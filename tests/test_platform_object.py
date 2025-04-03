import pytest
import pygame
from PlatformObject import PlatformObject


@pytest.fixture(autouse=True)
def init_pygame():
    """Initializes pygame for testing and
    ensures pygame.quit() is called after the test."""
    pygame.init()
    yield
    pygame.quit()


@pytest.fixture
def platform():
    """Creates a PlatformObject instance."""
    return PlatformObject(x=400, y=550, width=100,
                          height=10, speed=5, color=(255, 0, 0)
                          )


def test_platform_initialization(platform):
    """Verifies that the platform object initializes
    with the correct attributes."""
    assert platform.rect.x == 400
    assert platform.rect.y == 550
    assert platform.rect.width == 100
    assert platform.rect.height == 10
    assert platform.speed == 5
    assert platform.color == (255, 0, 0)


def test_platform_draw(platform):
    """Tests if the platform is correctly drawn
    on the screen with the specified color."""
    screen = pygame.Surface((800, 600))
    platform.draw(screen)
    new_color = screen.get_at((400, 555))
    assert new_color == (255, 0, 0), \
        f"Expected color (255, 0, 0), but got {new_color}"


@pytest.mark.parametrize("direction, expected_x", [
    ("left", 395),
    ("right", 405)
])
def test_platform_move(platform, direction, expected_x):
    """Ensures that the platform moves correctly in the specified direction."""
    platform.rect.x = 400
    platform.move(direction, 800)
    assert platform.rect.x == expected_x


def test_platform_move_left_boundary(platform):
    """Ensures that the platform doesn't move
    beyond the left screen boundary."""
    platform.rect.x = 0
    platform.move("left", 800)
    assert platform.rect.x == 0


def test_platform_move_right_boundary(platform):
    """Ensures that the platform doesn't move
    beyond the right screen boundary."""
    platform.rect.x = 700
    platform.move("right", 800)
    assert platform.rect.x == 700


def test_platform_move_properties():
    """Verifies that the platform moves
    as expected when using mocked properties."""
    platform = PlatformObject(x=50, y=0,
                              width=100, height=10, speed=5, color=(255, 0, 0)
                              )
    platform.rect.x = 50
    platform.move("left", 800)
    assert platform.rect.x == 45


def test_platform_move_right_edge(platform):
    """Tests that the platform cannot move past
    the right edge of the screen."""
    platform.rect.x = 750
    platform.move("right", 800)
    assert platform.rect.x == 750


def test_platform_color_change(platform):
    """Verifies that the platform's color
    can be successfully changed."""
    platform.color = (0, 255, 0)
    assert platform.color == (0, 255, 0)


@pytest.mark.parametrize("initial_x, direction, expected_x", [
    (400, "left", 395),
    (400, "right", 405)
])
def test_platform_move_with_boundaries(platform, initial_x,
                                       direction, expected_x):
    """Ensures the platform moves correctly within
    the screen boundaries for various starting positions."""
    platform.rect.x = initial_x
    platform.move(direction, 800)
    assert platform.rect.x == expected_x
