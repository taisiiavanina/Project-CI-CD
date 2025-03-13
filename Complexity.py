class Complexity:
    """
    Handles difficulty selection through the console.
    """

    def __init__(self):
        self.difficulty = None  # Спочатку рівень складності не встановлено

    def select_difficulty(self):
        """
        Allows the user to select a difficulty level.
        """
        while True:
            print("Select difficulty level:")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard")

            choice = input("Enter the number of the difficulty level: ")

            if choice == "1":
                self.difficulty = "easy"
                break
            elif choice == "2":
                self.difficulty = "medium"
                break
            elif choice == "3":
                self.difficulty = "hard"
                break
            else:
                print("Invalid choice! Please select a valid option.")

        print(f"Difficulty set to: {self.difficulty}")

    def get_difficulty(self):
        """
        Returns the current difficulty level.
        """
        return self.difficulty
