values: dict = {             # default algorithm parameters
        "alpha": 1000,                  # penalty function constant
        "population_size": 30,      # size of each population
        "target_value": 100000000000,        # target objective function value
        "g": 3.71,                  # gravitational acceleration [m/s^2]
        "mi": 0.5,                  # dynamic friction coefficient
        "rover_mass": 20.2,         # rover's initial mass in kilograms
        "base_id": 0,               # base point number
        "base_x": 0,                # base coordinates in x, y, z
        "base_y": 0,
        "base_z": 0,
        "init_fuel_need": 10,       # initial fuel needed to start moving
        "fuel": 10,                # initial fuel value
        "max_generation": 99,       # max number of generations
    }


def load_config_file(file: str = "config.txt"):
    global values
    floats = ["g", "mi", "alpha", "rover_mass"]
    f = open(file)
    for line in f:
        key, content = line.split()
        if key in floats:
            values[key] = float(content)
        else:
            values[key] = int(content)
    f.close()
