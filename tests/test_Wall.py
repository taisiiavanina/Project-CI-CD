import pytest
from Block import Block
from Wall import Wall


@pytest.fixture
def wall():
    """Fixture для створення стіни зі складністю 'easy'."""
    return Wall("easy")


def test_wall_initialization(wall):
    """Перевіряє, що стіна ініціалізується правильно."""
    assert wall.difficulty == "easy"
    assert len(wall.blocks) > 0  # Переконуємось, що блоки створені


def test_wall_difficulty_levels():
    """Перевіряє, що для кожної складності створюється
    правильна кількість блоків.
    """
    difficulties = {"easy": 3, "medium": 5, "hard": 7}

    for level, expected_rows in difficulties.items():
        wall = Wall(level)
        cols = 800 // (wall.block_width + 10)
        expected_blocks = expected_rows * cols
        assert len(wall.blocks) == expected_blocks


def test_wall_set_difficulty(wall):
    """Перевіряє, що зміна складності змінює кількість блоків."""
    initial_count = len(wall.blocks)

    wall.set_difficulty("medium")
    assert len(wall.blocks) > initial_count  # Має додатися більше блоків

    wall.set_difficulty("hard")
    assert len(wall.blocks) > initial_count  # Ще більше блоків

    wall.set_difficulty("easy")
    assert len(wall.blocks) == initial_count


def test_wall_draw(wall, mocker):
    """Перевіряє, що всі блоки викликають метод draw."""
    screen_mock = mocker.Mock()
    mocker.patch.object(Block, "draw")

    wall.draw(screen_mock)

    assert Block.draw.call_count == len(wall.blocks)
    # Всі блоки повинні викликати draw
