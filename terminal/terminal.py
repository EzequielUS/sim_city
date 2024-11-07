import os

class Terminal:
    SYMBOLS = {
        "Agua": "🔵",
        "Tierra": "🟤",
        "Calle": "⚪",
        "Casa": "🏠"
    }

    def clear_screen(self):
        """Clears the console screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def show_main_menu(self):
        print("1. Build house")
        print("2. Demolish")
        print("3. Show state")
        print("4. Exit")
        return input("Choose an option: ")

    def show_message(self, message):
        print(message)
    
    def show_board(self, board):
        """
        Displays the board in a visually appealing matrix with row and column identifiers.
        
        Parameters:
        - board: 2D list representing the current state of the board.
        """
        rows = len(board)
        cols = len(board[0]) if rows > 0 else 0

        # Header with column numbers
        print("   " + " ".join(f"{col:3}" for col in range(cols)))
        print("   " + "---" * cols)

        # Rows with row numbers and terrain symbols
        for i, row in enumerate(board):
            row_visual = [f"{self.SYMBOLS.get(cell, ' '):^3}" for cell in row]
            print(f"{i:2} | " + " | ".join(row_visual) + " |")
        
        print("\n")

    def show_balance(self, balance):
        print(f"Balance: {balance}")
