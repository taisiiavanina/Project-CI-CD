from Settings import Settings


def test_change_background_color():
    """Tests if the background color is correctly changed."""
    settings = Settings()
    new_color = (100, 100, 100)
    settings.change_background_color(new_color)
    assert settings.background_color == new_color
