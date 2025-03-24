def move_aircraft(aircraft, direction):
    # Direction to np. krotka (dx, dy, dz) – gdzie każdy element może być -1, 0 lub 1
    i, j, k = aircraft.grid_coords
    dx, dy, dz = direction
    new_coords = (i + dx, j + dy, k + dz)
    aircraft.update_grid_coords(new_coords)