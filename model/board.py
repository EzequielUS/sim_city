import random

class Board:
    def __init__(self, rows=10, cols=10, terrain_distribution=None):
        """
        Initializes the board with a customizable size and terrain distribution.
        
        Parameters:
        - rows: Number of rows on the board (default is 10).
        - cols: Number of columns on the board (default is 10).
        - terrain_distribution: Dictionary defining the percentage of each terrain type.
          Example: {'Agua': 0.3, 'Tierra': 0.6, 'Calle': 0.1}
        """
        self.rows = rows
        self.cols = cols
        self.terrain_distribution = terrain_distribution or {'Agua': 0.3, 'Tierra': 0.6, 'Calle': 0.1}
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.initialize_terrains()

    def initialize_terrains(self):
        """Fills the board with terrains based on the configured distribution."""
        total_cells = self.rows * self.cols
        terrain_counts = {terrain: int(percentage * total_cells) for terrain, percentage in self.terrain_distribution.items()}
        
        # Flatten grid and fill with terrain types based on counts
        flat_grid = []
        for terrain, count in terrain_counts.items():
            flat_grid.extend([terrain] * count)
        
        # Shuffle flat grid to randomize positions and reshape into 2D grid
        random.shuffle(flat_grid)
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j] = flat_grid.pop()

    # def can_build_Casa(self, x, y):
    #     """Checks if a Casa can be built on the specified position."""
    #     return self.grid[x][y] == 'Calle'
    
    # def build(self, x, y, structure_type):
    #     """Builds a structure (e.g., Casa) on the specified position."""
    #     if structure_type == "Casa" and self.can_build_Casa(x, y):
    #         self.grid[x][y] = "Casa"
    
    # def can_demolish(self, x, y):
    #     """Checks if the specified position can be demolished."""
    #     return self.grid[x][y] in ["Casa", "Calle"]
    
    # def demolish(self, x, y):
    #     """Demolishes the structure on the specified position, turning it back to Tierra."""
    #     if self.can_demolish(x, y):
    #         self.grid[x][y] = "Tierra"
    
    def get_state(self):
        """Returns the current state of the board."""
        return self.grid
