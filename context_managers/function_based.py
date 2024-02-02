from contextlib import contextmanager

PLANET_INFO = {
    "Mercury": {"moons": 0, "position_from_sun": 1, "vol_km3": 6.083e10},
    "Venus": {"moons": 0, "position_from_sun": 2, "vol_km3": 9.2843e11},
    "Earth": {"moons": 1, "position_from_sun": 3, "vol_km3": 1.08321e12},
    "Mars": {"moons": 2, "position_from_sun": 4, "vol_km3": 1.6318e11},
    "Jupiter": {"moons": 79, "position_from_sun": 5, "vol_km3": 1.43128e15},
    "Saturn": {"moons": 83, "position_from_sun": 6, "vol_km3": 8.2713e14},
    "Uranus": {"moons": 27, "position_from_sun": 7, "vol_km3": 6.833e13},
    "Neptune": {"moons": 14, "position_from_sun": 8, "vol_km3": 6.254e13}
}
UNITS_CONSUMED_TO_LEAVE_JUPITER = 20
FUEL_CONSUMPTION_RATE = UNITS_CONSUMED_TO_LEAVE_JUPITER / PLANET_INFO['Jupiter']['vol_km3']  # Adjusted for illustration

@contextmanager
def planet_context_manager(planet,fuel):
    print(f"Entering the {planet} context...")        
    yield PLANET_INFO[planet]
    fuel = fuel - (PLANET_INFO[planet]['vol_km3'] * FUEL_CONSUMPTION_RATE)
    print(f"Leaving {planet}...You will have {fuel} units of fuel left")
        
with planet_context_manager("Jupiter",100) as planet:
    print(planet)
    # print(planet['distance_from_sun'])