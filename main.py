import evolutionary_algorithm
from map import Map
import population
import specimen
import configuration


def main():
    configuration.load_config_file()
    alg_map = Map()
    final_population = evolutionary_algorithm.run(alg_map)

    for elem in final_population.current_generation:
        print("ROUTE", elem.route, "RATING", elem.rating, "IS ALLOWED", elem.is_allowed)

    print("BEST:", final_population.select_best_specimen().route, "RATING:",
          final_population.select_best_specimen().rating)
    print("BEST ALLOWED:", final_population.select_best_allowed_specimen().route, "RATING:",
          final_population.select_best_allowed_specimen().rating)

    print(final_population.gen_num)
    # print(alg_map.cost_matrix)
    pass


if __name__ == '__main__':
    # TODO wywołanie algorytmu
    main()
    pass
