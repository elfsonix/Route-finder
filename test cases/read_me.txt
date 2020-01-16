Każdy plik zawiera 16 kolumn z wartościami dict zgodnie z zawartością pliku "configuration.py".

Przykładowo, bazowy plik o nazwie "0.txt" odpowiada:
"alpha": 0.0000001,             # penalty function constant
"population_size": 30,          # size of each population
"target_value": 10000,          # target objective function value
"g": 3.71,                      # gravitational acceleration [m/s^2]
"mi": 0.5,                      # dynamic friction coefficient
"rover_mass": 20.2,             # rover's initial mass in kilograms
"base_id": 0,                   # base point number
"base_x": 0,                    # base coordinates in x, y, z
"base_y": 0,
"base_z": 0,
"init_fuel_need": 10,           # initial fuel needed to start moving
"fuel": 1000,                   # initial fuel value
"max_generation": 99,           # max number of generations
"mutation_rate": 50,            # chance that a gene will mutate in %
"parent_group_size": 50,        # size of parent group in % of the whole population
"Ni_max": 1,                    # Ni_max c <1,2>