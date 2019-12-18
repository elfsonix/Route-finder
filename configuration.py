
class Configuration:
    def __init__(self, file: str = "config.txt"):
        f = open(file)
        temp_dict: dict = {             # default algorithm parameters
            "alfa": 1,                  # penalty function constant
            "population_size": 30,      # size of each population
            "target_value": 100,        # target objective function value
            "g": 3.71,                  # gravitational acceleration [m/s^2]
            "rover_mass": 20.2,         # mass in kilograms
            "base_x": 0,                # base coordinates in x, y, z
            "base_y": 0,
            "base_z": 0,
            "init_fuel_need": 10,       # initial fuel needed to start moving
            "fuel": 100,                # initial fuel value
            "max_generation": 100,       # max number of generations

        }
        for line in f:
            key, content = line.split()
            temp_dict[key] = content
        f.close()
        self.config = temp_dict
