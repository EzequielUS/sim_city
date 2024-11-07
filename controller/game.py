from model.board import Board
from model.player import Player
from model.clock import Clock
from terminal.terminal import Terminal

class Game:
    def __init__(self):
        self.board = None
        self.player = None
        self.clock = None
        self.view = Terminal()

    def start_game(self):
        self.initialize_board()
        self.initialize_player()
        self.initialize_clock()
        self.view.show_message("Welcome to Python SimCity!")
        self.show_initial_state()
        self.main_loop()
    
    def initialize_board(self):
        self.board = Board()
        self.board.initialize_terrains()
        self.view.show_message("Board initialized.")
    
    def initialize_player(self):
        self.player = Player(initial_balance=1000)
        self.view.show_balance(self.player.balance)
    
    def initialize_clock(self):
        self.clock = Clock()
        self.view.show_message(self.clock.get_time())
    
    def show_initial_state(self):
        self.view.show_board(self.board.get_state())
        self.view.show_balance(self.player.balance)
    
    def main_loop(self):
        playing = True
        while playing:
            option = self.view.show_main_menu()
            if option == "1":
                self.build_house()
            elif option == "2":
                self.demolish()
            elif option == "3":
                self.show_state()
            elif option == "4":
                playing = False
                self.view.show_message("Thanks for playing!")
            else:
                self.view.show_message("Invalid option. Please try again.")
    
    def build_house(self):
        x, y = self.view.request_position()
        if self.board.can_build_house(x, y) and self.player.can_pay(50):
            self.player.update_balance(-50)
            self.board.build(x, y, "House")
            self.view.show_message("House successfully built.")
        else:
            self.view.show_message("Cannot build a house in this position or insufficient balance.")
        self.show_state()
    
    def demolish(self):
        x, y = self.view.request_position()
        if self.board.can_demolish(x, y) and self.player.can_pay(10):
            self.player.update_balance(-10)
            self.board.demolish(x, y)
            self.view.show_message("Building successfully demolished.")
        else:
            self.view.show_message("Cannot demolish at this position or insufficient balance.")
        self.show_state()
    
    def show_state(self):
        self.view.clear_screen()
        self.view.show_board(self.board.get_state())
        self.view.show_balance(self.player.balance)
