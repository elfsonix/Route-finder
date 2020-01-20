from multi_track_drifting import MultiInstanceEAlgorithm
from output_presentation import Plotter
from evolutionary_algorithm import EAlgorithm
from map import Map
import configuration as cnfg


def run_tests(times: int = 1):
    mea = MultiInstanceEAlgorithm(set_specimen=True)
    best, worst, avg, std = mea.execute_algorithm(times=times)
    case_names = []
    map_names = []
    iteretion = 0
    for name in mea.cases_names:
        case_names.append(name[11:].strip(".txt"))
    for name in mea.maps_names:
        map_names.append(name[5:].strip(".txt"))
    for name1 in map_names:
        Plotter().barplot(best[iteretion*6:iteretion*6+6], case_names, "Rating", name1)
        iteretion += 1
    # Plotter().barplot(best, bar_names, "Rating", "BEST")
    return best, worst, avg, std


def single_run_test():
    cnfg.load_config_file()
    alg_map = Map()
    ea = EAlgorithm(alg_map, save_info_per_iter=True)
    ea.run()
    ea.plot_per_iteration()
    print(ea.generation.select_best_allowed_specimen().rating)
    pass


if __name__ == "__main__":
    single_run_test()
    run_tests(100)
