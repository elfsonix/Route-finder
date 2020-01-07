import evolutionary_algorithm
from map import Map
import configuration
from output_presentation import Plotter


def main():
    configuration.load_config_file()
    alg_map = Map()
    data = evolutionary_algorithm.run_multiple_times(alg_map, 100)
    print("DONE")
    [best_ratings, routes, time] = data
    for element in range(len(best_ratings)):
        print("Try", time[element], ":", best_ratings[element], routes[element])
    routes_len = []
    for route in routes:
        routes_len.append(len(route))

    Plotter().style_setup()
    Plotter().histogram(time, best_ratings)
    Plotter().scatter_plot(routes_len, best_ratings)
    # Plotter().scatter_and_histogram(routes_len, best_ratings)


if __name__ == '__main__':
    # TODO wywołanie algorytmu
    main()
    pass
