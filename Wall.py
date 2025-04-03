from Block import Block


class Wall:
    """
    Represents a collection of blocks forming a wall.
    """

    def __init__(self, difficulty, block_width=50, block_height=20):
        """
        Initializes the wall with default difficulty ('easy').
        Parameters:
        screen_width (int): Width of the game screen.
        block_width (int): Width of a single block.
        block_height (int): Height of a single block.
        """
        self.blocks = []
        self.block_width = block_width
        self.block_height = block_height
        self.difficulty = difficulty
        self.generate_blocks()

    def generate_blocks(self):
        """
        Generates blocks based on the current difficulty.
        """
        self.blocks.clear()

        if self.difficulty == "easy":
            rows = 3
        elif self.difficulty == "medium":
            rows = 5
        elif self.difficulty == "hard":
            rows = 7
        else:
            rows = 2  # Безпечний дефолт

        cols = 800 // (self.block_width + 10)

        for row in range(rows):
            for col in range(cols):
                x = col * (self.block_width + 10) + 10
                y = row * (self.block_height + 10) + 50
                self.blocks.append(Block(x, y,
                                         self.block_width, self.block_height)
                                   )

    def set_difficulty(self, difficulty):
        """
        Changes the difficulty level, regenerates the blocks.
        Parameters:
        difficulty (str): New difficulty level ('easy', 'medium', 'hard').
        """
        self.difficulty = difficulty
        self.generate_blocks()

    def draw(self, screen):
        """
        Draws all blocks on the screen.
        Parameters:
        screen (pygame.Surface): The screen to draw on.
        """
        for block in self.blocks:
            block.draw(screen)
