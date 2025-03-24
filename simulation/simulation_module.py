import asyncio
from movement import move_aircraft
from simulation.grid import Grid
from config import AIRSPACE_DIMENSIONS

async def simulation_loop(airspace, grid):
    while True:
        # Przykładowo: każdy samolot może losowo wybrać jeden z sąsiednich ruchów
        for aircraft in airspace.aircrafts:
            # Możemy użyć losowego ruchu w siatce:
            from random import choice
            directions = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]
            move = choice(directions)
            move_aircraft(aircraft, move)
        # Sprawdzenie kolizji można zrobić analogicznie, wywołując np. aircraft.is_in_collision_range(other)
        await asyncio.sleep(1)