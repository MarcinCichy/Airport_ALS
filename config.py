# config.py
import os
from configparser import ConfigParser


def load_config():
    """
    Odczytuje konfigurację z pliku config.ini.
    Jeśli zmienna środowiskowa TEST_ENV jest ustawiona na 'test',
    można użyć innego pliku (np. test_database.ini) – tutaj przykładowo używamy config.ini.
    """
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    parser = ConfigParser()
    read_files = parser.read(config_file)
    if not read_files:
        raise Exception(f"Nie udało się odczytać pliku konfiguracyjnego: {config_file}")
    return parser


def get_constants():
    """
    Pobiera ustawienia (stałe) z sekcji [settings] w pliku konfiguracyjnym.
    Zwraca słownik z kluczami takimi jak:
      - MAX_AIRCRAFTS
      - AIRSPACE_DIMENSIONS
      - COLLISION_DISTANCE
      - FUEL_DURATION
      - HOST
      - PORT
    """
    config = load_config()

    constants = {}
    # Odczytujemy liczbowe wartości przy użyciu metod getint (dla int) lub getfloat (dla float)
    constants['MAX_AIRCRAFTS'] = config.getint('settings', 'MAX_AIRCRAFTS', fallback=100)

    # AIRSPACE_DIMENSIONS może być zapisany jako ciąg znaków "(10000,10000,5000)"
    dims_str = config.get('settings', 'AIRSPACE_DIMENSIONS', fallback="(10000,10000,5000)")
    # Używamy eval, aby przekształcić ciąg w krotkę – w produkcji warto rozważyć bezpieczniejsze rozwiązanie
    constants['AIRSPACE_DIMENSIONS'] = eval(dims_str)

    constants['COLLISION_DISTANCE'] = config.getint('settings', 'COLLISION_DISTANCE', fallback=10)
    constants['FUEL_DURATION'] = config.getint('settings', 'FUEL_DURATION', fallback=10800)
    constants['HOST'] = config.get('settings', 'HOST', fallback='127.0.0.1')
    constants['PORT'] = config.getint('settings', 'PORT', fallback=8000)
    return constants
