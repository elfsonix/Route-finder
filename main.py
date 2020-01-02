import evolutionary_algorithm
from map import Map
import population
import specimen
import configuration
from exceptions import *


def main():
    configuration.load_config_file()
    alg_map = Map()
    best_ratings = evolutionary_algorithm.run_multiple_times(alg_map, 100)



    # for elem in final_population.current_generation:
    #     print("ROUTE", elem.route, "RATING", elem.rating, "IS ALLOWED", elem.is_allowed)
    #
    # print("BEST:", final_population.select_best_specimen().route, "RATING:",
    #       final_population.select_best_specimen().rating)
    # print("BEST ALLOWED:", final_population.select_best_allowed_specimen().route, "RATING:",
    #       final_population.select_best_allowed_specimen().rating)
    #
    # print(final_population.gen_num)
    # print(alg_map.cost_matrix)
    print("DONE")
    for rating in best_ratings:
        print("Try", rating[0], ":", rating[1], rating[2])
    pass


if __name__ == '__main__':
    # TODO wywołanie algorytmu
    main()
    pass
