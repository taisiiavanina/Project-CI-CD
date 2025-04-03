import pytest
import pygame
import math
from Ball import Ball
from Block import Block


@pytest.fixture
def ball():
    pygame.init()
    return Ball(x=400, y=300)


@pytest.fixture
def platform():
    class Platform:
        def __init__(self):
            self.rect = pygame.Rect(350, 500, 100, 10)

    return Platform()


@pytest.fixture
def wall():
    class Wall:
        def __init__(self):
            self.blocks = []

    return Wall()


def test_initialization(ball):
    """Test the initialization of the ball."""
    assert ball.x == 400
    assert ball.y == 300
    assert ball.radius == 8
    assert ball.speed == 3
    assert ball.color == (255, 255, 0)
    assert ball.dx == math.cos(math.radians(45)) * ball.speed
    assert ball.dy == -math.sin(math.radians(45)) * ball.speed


def test_move_bounce_off_walls(ball, platform, wall):
    """Test the ball bouncing off-screen walls."""
    ball.x = 0
    ball.dx = -5
    ball.move(800, 600, platform, wall)
    assert ball.dx > 0

    ball.x = 800
    ball.dx = 5
    ball.move(800, 600, platform, wall)
    assert ball.dx < 0


def test_move_bounce_off_platform(ball, platform, wall):
    """Test the ball bouncing off the platform."""
    ball.x = 400
    ball.y = 490
    ball.dy = 5

    ball.move(800, 600, platform, wall)
    assert ball.dy < 0


def test_move_ball_out_of_screen(ball, platform, wall):
    """Test the ball moving out of the screen."""
    ball.y = 700
    result = ball.move(800, 600, platform, wall)
    assert not result


def test_move_win_condition(ball, platform, wall):
    """Test the win condition after all blocks are destroyed."""
    wall.blocks = []
    result = ball.move(800, 600, platform, wall)
    assert result == "win"


def test_ball_collision_with_blocks(ball, wall, platform):
    """Test ball collision with blocks."""
    block = Block(390, 290, 20, 20, 0)
    wall.blocks = [block]

    ball.x = 390
    ball.y = 290
    ball.dy = -5

    ball.move(800, 600, platform, wall)

    assert 5 <= block.points <= 20


def test_ball_draw(ball):
    """Test the correct drawing of the ball."""
    screen = pygame.Surface((800, 600))
    ball.draw(screen)
    assert screen.get_at((int(ball.x), int(ball.y)))[0] == 255


@pytest.fixture(autouse=True)
def pygame_cleanup():
    """Clean up pygame after the tests."""
    yield
    pygame.quit()
