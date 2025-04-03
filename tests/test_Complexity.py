from Complexity import Complexity


def test_get_difficulty():
    """Tests if the set difficulty level is correctly returned."""
    complexity = Complexity()
    complexity.difficulty = "medium"
    assert complexity.get_difficulty() == "medium"
