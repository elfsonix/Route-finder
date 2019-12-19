values: dict = {             # default algorithm parameters
        "alpha": 2,                  # penalty function constant
        "population_size": 30,      # size of each population
        "target_value": 1000,        # target objective function value
        "g": 3.71,                  # gravitational acceleration [m/s^2]
        "mi": 0.5,                  # dynamic friction coefficient
        "rover_mass": 20.2,         # rover's initial mass in kilograms
        "base_id": 0,               # base point number
        "base_x": 0,                # base coordinates in x, y, z
        "base_y": 0,
        "base_z": 0,
        "init_fuel_need": 10,       # initial fuel needed to start moving
        "fuel": 10000,                # initial fuel value
        "max_generation": 99,       # max number of generations
    }


def load_config_file(file: str = "config.txt"):
    global values
    f = open(file)
    for line in f:
        key, content = line.split()
        values[key] = content
    f.close()
