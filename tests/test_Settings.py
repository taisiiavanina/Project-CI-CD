from Settings import Settings


def test_change_background_color():
    """Перевіряє, чи змінюється колір фону."""
    settings = Settings()
    new_color = (100, 100, 100)
    settings.change_background_color(new_color)
    assert settings.background_color == new_color
