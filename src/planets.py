import json
import os

# JSON file route with all the planet data
DATA_PATH = os.path.join(os.path.dirname(__file__) + "\data" , "planet_data.json")

#Load all the planet data
try:
    with open(DATA_PATH, "r") as f:
        PLANET_DATA = json.load(f)
except FileNotFoundError:
    raise FileNotFoundError(f"Data file not found: {DATA_PATH}")


class Planets:
    def __init__(self, planetA, planetB):
        
        self.planetA = planetA
        self.planetB = planetB

        dataA, dataB = self._get_planet_param()
        self._load_planet_attributes(dataA, suffix="A")
        self._load_planet_attributes(dataB, suffix="B")

    def _load_planet_attributes(self, data, suffix):
        setattr(self, f"name{suffix}", data["name"])
        setattr(self, f"radius{suffix}", data["radius"])
        setattr(self, f"orbital_period{suffix}", data["orbital_period"])
        setattr(self, f"mu{suffix}", data["mu"])
        setattr(self, f"soi{suffix}", data["soi"])
        setattr(self, f"orbital_radius{suffix}", data["orbital_radius"])

    def info(self):
        A, B = self._get_planet_param()
        print(A, B)


    def _get_planet_param(self):
        
        planets = [self.planetA, self.planetB]
        results = []

        for planet in planets:    
            try:
                 results.append(PLANET_DATA[planet])
            except KeyError:
                raise ValueError(f"Planet {planet} not found in .JSON")
        return results[0], results[1]
    

planetas = Planets("Mercury", "Earth")
planetas.info()
print(planetas.__dict__)