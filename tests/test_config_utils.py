# test_config_utils.py
from config import get_constants
from utils.utils_module import calculate_distance, random_position_on_boundary


def main():
    # Testujemy odczyt konfiguracji
    constants = get_constants()
    print("Wczytane ustawienia:")
    for key, value in constants.items():
        print(f"{key} = {value}")

    # Testujemy funkcję calculate_distance
    p1 = (0, 0, 0)
    p2 = (3, 4, 0)
    distance = calculate_distance(p1, p2)
    print(f"Odległość między {p1} a {p2} wynosi: {distance}")  # Oczekujemy 5

    # Testujemy funkcję random_position_on_boundary
    airspace_dims = constants['AIRSPACE_DIMENSIONS']
    random_pos = random_position_on_boundary(airspace_dims)
    print(f"Losowo wygenerowana pozycja na granicy: {random_pos}")


if __name__ == "__main__":
    main()
