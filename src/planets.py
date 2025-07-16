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

    """
        Load and store planetary data for two celestial bodies.

        This class reads planetary parameters (e.g. radius, mu, orbital period, etc.)
        from a JSON file and stores them as attributes for later use in computations.

        Attributes:
            planetA (str): Name of the departure planet.
            planetB (str): Name of the arrival planet.
            nameA, nameB (str): Planet names.
            radiusA, radiusB (float): Planetary radii [km].
            orbital_periodA, orbital_periodB (float): Orbital periods [s].
            muA, muB (float): Gravitational parameters [km^3/s^2].
            soiA, soiB (float): Spheres of influence [km].
            orbital_radiusA, orbital_radiusB (float): Orbital radii around the Sun [km].
    """
     
    def __init__(self, planetA, planetB):
       
        """
        Initialize the Planets instance with two planet names.

        Loads relevant planetary data from a JSON file and stores
        the parameters for each planet as class attributes.

        Parameters:
        - planetA (str): Name of the first planet (e.g. "Earth").
        - planetB (str): Name of the second planet (e.g. "Mars").

        """

        self.planetA = planetA
        self.planetB = planetB

        dataA, dataB = self._get_planet_param()
        self._load_planet_attributes(dataA, suffix="A")
        self._load_planet_attributes(dataB, suffix="B")

    def _load_planet_attributes(self, data, suffix):

        """
        Dynamically assign planetary attributes using a suffix (e.g., 'A' or 'B').

        This method creates attributes like `nameA`, `radiusB`, etc., 
        based on the provided planet data and suffix. It simplifies 
        initialization when managing two planetary bodies.

        Parameters:
        - data (dict): Dictionary containing the planet's physical and orbital parameters.
        - suffix (str): Suffix to append to the attribute names (e.g., 'A' or 'B').

        Attributes Created:
        - name{suffix}
        - radius{suffix}
        - orbital_period{suffix}
        - mu{suffix}
        - soi{suffix}
        - orbital_radius{suffix}
        """
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

        """
        Retrieve the parameter dictionaries for both selected planets.

        Returns:
        - Tuple[dict, dict]: A tuple containing the data for planet A and planet B.

        Raises:
        - ValueError: If a planet is not found in the JSON data.
        """
        
        planets = [self.planetA, self.planetB]
        results = []

        for planet in planets:    
            try:
                 results.append(PLANET_DATA[planet])
            except KeyError:
                raise ValueError(f"Planet {planet} not found in .JSON")
        return results[0], results[1]
    
