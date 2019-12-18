import cost_calculator
import evolutionary_algorithm
import map
import population
import rover
import specimen
import configuration


def main():
    configuration.load_config_file()
    alg_map = map.Map()
    final_population = evolutionary_algorithm.run(alg_map)
    pass


if __name__ == '__main__':
    # TODO wywołanie algorytmu
    main()
    pass
