# simulation/grid.py
class Grid:
    def __init__(self, width, height, depth, cell_size):
        # Zakładamy, że width, height, depth są w metrach, a cell_size to długość boku kostki
        self.cell_size = cell_size
        self.num_cells_x = int(width / cell_size)
        self.num_cells_y = int(height / cell_size)
        self.num_cells_z = int(depth / cell_size)

    def to_grid_coords(self, position):
        # Pozycja jest ciągła, np. (x, y, z)
        x, y, z = position
        return (int(x / self.cell_size), int(y / self.cell_size), int(z / self.cell_size))

    def from_grid_coords(self, grid_coords):
        # Zamienia indeksy na pozycję w centrum kostki
        i, j, k = grid_coords
        return ((i + 0.5) * self.cell_size, (j + 0.5) * self.cell_size, (k + 0.5) * self.cell_size)
