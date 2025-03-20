import config
from utils.utils_module import calculate_distance



class Aircraft:
    def __init__(self, id, position, fuel):
        self.id = id
        self.position = position
        self.fuel = fuel
        self.status = 'waiting'

    def update_position(self, new_position):
        self.position = new_position

    def consume_fuel(self, amount):
        self.fuel -= amount

    def is_in_collision_range(self, other):
        return calculate_distance(self.position, other.position) < config.COLLISION_DISTANCE



