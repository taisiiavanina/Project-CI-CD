import pytest
import pygame
from Block import Block


def test_block_initialization():
    """Test the initialization of a Block object."""
    block = Block(100, 200, 50, 20)
    assert block.rect.x == 100
    assert block.rect.y == 200
    assert block.rect.width == 50
    assert block.rect.height == 20
    assert isinstance(block.color, tuple) and len(block.color) == 3
    assert all(50 <= c <= 255 for c in block.color)
    assert 5 <= block.points <= 20


def test_random_color():
    """Test the random color generation in a Block."""
    block = Block(0, 0)
    color = block.random_color()
    assert isinstance(color, tuple) and len(color) == 3
    assert all(50 <= c <= 255 for c in color)


def test_block_draw():
    """Test drawing the Block on the screen."""
    pygame.init()
    screen = pygame.Surface((800, 600))  # Creating a temporary screen
    block = Block(100, 200, 50, 20)
    try:
        block.draw(screen)  # Test the method call without errors
    except Exception as e:
        pytest.fail(f"Block.draw() raised an error: {e}")
    pygame.quit()
