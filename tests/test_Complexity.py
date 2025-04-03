from Complexity import Complexity


def test_get_difficulty():
    """Перевіряє, чи коректно повертається встановлений рівень складності."""
    complexity = Complexity()
    complexity.difficulty = "medium"
    assert complexity.get_difficulty() == "medium"
