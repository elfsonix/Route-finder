values: dict = {                        # default algorithm parameters
        "alpha": 0.0000001,               # penalty function constant
        "population_size": 30,          # size of each population
        "target_value": 10000,          # target objective function value
        "g": 3.71,                      # gravitational acceleration [m/s^2]
        "mi": 0.5,                      # dynamic friction coefficient
        "rover_mass": 20.2,             # rover's initial mass in kilograms
        "init_fuel_need": 10,           # initial fuel needed to start moving
        "fuel": 1000,                   # initial fuel value
        "max_generation": 99,           # max number of generations
        "mutation_probability": 10,     # chance that a specimen will be mutated in %
        "mutation_rate": 50,            # chance that a gene will mutate in %
        "parent_group_size": 50,        # size of parent group in % of the whole population
        "Ni_max": 1,                    # Ni_max c <1,2>
    }


def load_config_file(file: str = "config.txt"):
    global values
    floats = ["g", "mi", "alpha", "rover_mass", "Ni_max"]
    f = open(file)
    for line in f:
        key, content = line.split()
        if key in floats:
            values[key] = float(content)
        else:
            values[key] = int(content)
    f.close()
