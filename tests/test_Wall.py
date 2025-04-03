import pytest
from Block import Block
from Wall import Wall


@pytest.fixture
def wall():
    """Fixture for creating a wall with 'easy' difficulty."""
    return Wall("easy")


def test_wall_initialization(wall):
    """Tests if the wall initializes correctly."""
    assert wall.difficulty == "easy"
    assert len(wall.blocks) > 0  # Ensure blocks are created


def test_wall_difficulty_levels():
    """Tests that the correct number of blocks is created for difficulty."""
    difficulties = {"easy": 3, "medium": 5, "hard": 7}

    for level, expected_rows in difficulties.items():
        wall = Wall(level)
        cols = 800 // (wall.block_width + 10)
        expected_blocks = expected_rows * cols
        assert len(wall.blocks) == expected_blocks


def test_wall_set_difficulty(wall):
    """Tests that changing the difficulty updates the number of blocks."""
    initial_count = len(wall.blocks)

    wall.set_difficulty("medium")
    assert len(wall.blocks) > initial_count  # More blocks should be added

    wall.set_difficulty("hard")
    assert len(wall.blocks) > initial_count  # Even more blocks

    wall.set_difficulty("easy")
    assert len(wall.blocks) == initial_count


def test_wall_draw(wall, mocker):
    """Tests if all blocks call the draw method."""
    screen_mock = mocker.Mock()
    mocker.patch.object(Block, "draw")

    wall.draw(screen_mock)

    assert Block.draw.call_count == len(wall.blocks)
    # All blocks should call draw
