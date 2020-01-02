from copy import copy
import evolutionary_algorithm
from map import Map
import population
import specimen
import configuration
from exceptions import *
import output_presentation


def main():
    best_ratings = []
    configuration.load_config_file()
    alg_map = Map()
    best_ratings += evolutionary_algorithm.run_multiple_times(alg_map, 10)
    print("DONE")
    for rating in best_ratings:
        print("Try", rating[0], ":", rating[1], rating[2])
    pass


if __name__ == '__main__':
    # TODO wywołanie algorytmu
    main()
    pass
