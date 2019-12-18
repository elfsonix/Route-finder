import cost_calculator
import evolutionary_algorithm
import Map
import Population
import rover
import solution
import configuration


def main():
    alg_config = configuration.Configuration()
    final_population = evolutionary_algorithm.EvolutionaryAlgorithm.run(alg_config.config["population_size"])
    pass


if __name__ == '__main__':
    # TODO wywołanie algorytmu
    main()
    pass
