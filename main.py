import cost_calculator
import evolutionary_algorithm
from map import Map
import population
import rover
import specimen
import configuration


def main():
    configuration.load_config_file()
    alg_map = Map()
    final_population = evolutionary_algorithm.run(alg_map)
    print(final_population.select_best_specimen().route)
    print(final_population.select_best_specimen().rating)
    print(final_population.gen_num)
    pass


if __name__ == '__main__':
    # TODO wywołanie algorytmu
    main()
    pass
