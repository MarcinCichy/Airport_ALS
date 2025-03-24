import config
from utils.utils_module import calculate_distance


class Aircraft:
    def __init__(self, id, grid_coords, fuel, collision_cell_margin=1):
        self.id = id
        self.grid_coords = grid_coords  # Pozycja jako indeksy w siatce, np. (i, j, k)
        self.fuel = fuel # np. 10800 jednostek paliwa dla 3 godzin
        self.status = 'waiting'
        self.collision_cell_margin = collision_cell_margin  # Określa margines bezpieczeństwa w kostkach

    def update_grid_coords(self, new_grid_coords):
        self.grid_coords = new_grid_coords

    def is_in_collision_range(self, other):
        # Sprawdzamy, czy samoloty są w zbyt bliskich kostkach
        dx = abs(self.grid_coords[0] - other.grid_coords[0])
        dy = abs(self.grid_coords[1] - other.grid_coords[1])
        dz = abs(self.grid_coords[2] - other.grid_coords[2])
        # Jeśli różnice w każdej osi są mniejsze lub równe marginesowi, uznajemy to za kolizję
        return (dx <= self.collision_cell_margin and
                dy <= self.collision_cell_margin and
                dz <= self.collision_cell_margin)

    def consume_fuel(self, delta_time):
        # Załóżmy, że zużywamy 1 jednostkę paliwa na sekundę
        self.fuel -= delta_time
