PLANET_INFO = {
    "Mercury": {"moons": 0, "position_from_sun": 1, "size_km3": 6.083e10},
    "Venus": {"moons": 0, "position_from_sun": 2, "size_km3": 9.2843e11},
    "Earth": {"moons": 1, "position_from_sun": 3, "size_km3": 1.08321e12},
    "Mars": {"moons": 2, "position_from_sun": 4, "size_km3": 1.6318e11},
    "Jupiter": {"moons": 79, "position_from_sun": 5, "size_km3": 1.43128e15},
    "Saturn": {"moons": 83, "position_from_sun": 6, "size_km3": 8.2713e14},
    "Uranus": {"moons": 27, "position_from_sun": 7, "size_km3": 6.833e13},
    "Neptune": {"moons": 14, "position_from_sun": 8, "size_km3": 6.254e13}
}
UNITS_CONSUMED_TO_LEAVE_JUPITER = 20

FUEL_CONSUMPTION_RATE = UNITS_CONSUMED_TO_LEAVE_JUPITER / PLANET_INFO['Jupiter']['size_km3']  # Adjusted for illustration

class PlanetContextManager:
    def __init__(self,planet,fuel):
        self.planet = planet
        self.fuel = fuel

    def __enter__(self):
        print(f"Entering the {self.planet} context...")        
        return PLANET_INFO[self.planet]
    
    def __exit__(self, exc_type, exc_value, exc_tb):       
        self.fuel = self.fuel - (PLANET_INFO[self.planet]['size_km3'] * FUEL_CONSUMPTION_RATE)
        print(f"Leaving {self.planet}...I have {self.fuel} units of fuel left")

        print(exc_type, exc_value, exc_tb, sep="\n")


with PlanetContextManager("Eart",100) as planet:
    print(planet)