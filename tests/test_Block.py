import pytest
import pygame
from Block import Block

def test_block_initialization():
    block = Block(100, 200, 50, 20)
    assert block.rect.x == 100
    assert block.rect.y == 200
    assert block.rect.width == 50
    assert block.rect.height == 20
    assert isinstance(block.color, tuple) and len(block.color) == 3  # Колір має бути кортежем з трьох елементів
    assert all(50 <= c <= 255 for c in block.color)  # Кожен компонент кольору в допустимому діапазоні
    assert 5 <= block.points <= 20  # Очки мають бути в межах [5, 20]

def test_random_color():
    block = Block(0, 0)
    color = block.random_color()
    assert isinstance(color, tuple) and len(color) == 3
    assert all(50 <= c <= 255 for c in color)  # Кожен компонент кольору має бути в межах діапазону

def test_block_draw():
    pygame.init()
    screen = pygame.Surface((800, 600))  # Створюємо тимчасовий екран
    block = Block(100, 200, 50, 20)
    try:
        block.draw(screen)  # Тестуємо виклик методу без помилок
    except Exception as e:
        pytest.fail(f"Block.draw() викликало помилку: {e}")
    pygame.quit()
