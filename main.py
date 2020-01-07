import evolutionary_algorithm
from map import Map
import configuration
from output_presentation import *


def main():
    configuration.load_config_file()
    alg_map = Map()
    data = evolutionary_algorithm.run_multiple_times(alg_map, 10)
    print("DONE")
    [best_ratings, routes, time] = data
    for element in range(len(best_ratings)):
        print("Try", time[element], ":", best_ratings[element], routes[element])

    fig, ax = plt.subplots()
    ax.plot(time, best_ratings)

    ax.set(xlabel='try', ylabel='best rating',
           title='Super Sonia')
    plt.show()


if __name__ == '__main__':
    # TODO wywołanie algorytmu
    main()
    pass
