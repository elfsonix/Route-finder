import evolutionary_algorithm
from map import Map
import configuration
from output_presentation import Plotter


def main():
    configuration.load_config_file()
    alg_map = Map()
    data = evolutionary_algorithm.run_multiple_times(alg_map, 1000)
    print("DONE")
    [best_ratings, routes, time] = data
    for element in range(len(best_ratings)):
        print("Try", time[element], ":", best_ratings[element], routes[element])

    Plotter().style_setup()
    Plotter().histogram(time, best_ratings)


if __name__ == '__main__':
    # TODO wywołanie algorytmu
    main()
    pass
