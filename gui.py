from evolutionary_algorithm import EAlgorithm
from multi_track_drifting import MultiInstanceEAlgorithm
from map import Map
from output_presentation import Plotter


class GUI:  # TODO całe GUI
    def __init__(self):
        print("Algorytm ewolucyjny analizujący trasę łazika z poborem próbek")
        print("Stworzony na zajęcia 'Matematyczne Metody Wspomagania Decyzji', III rok AiR I stopnia, WEAIiIB, AGH")
        print("Jacek Lichwa, Karolina Świerczek, Sonia Wittek")
        print()
        print("Wprowadź znak aby wybrać opcję z listy")
        pass

    def main_menu(self):
        print("1. Pojedyncze uruchomienie")
        print("2. Wielokrotne uruchomienie")
        print("Q - Zakończ")
        choice = input()
        if choice == "1":
            self.custom_instance_menu()
        elif choice == "2":
            self.multi_instance_menu()
        elif choice == "q" or "Q":
            pass
        else:
            self.main_menu()

    def multi_instance_menu(self):
        print("Wielokrotne uruchomienie dla:")
        print("1. Domyślnych wartości i losowych osobników startowych")
        print("2. Przypadków testowych i predefiniowanych osobników startowych")
        choice = input()
        if choice == "1":
            print("Ile razy?")
            n = input()
            ea_map = Map()
            ea = EAlgorithm()
            [routes, ratings, time] = ea.run_multiple_times(ea_map, int(n))
            print()
            for i in range(len(routes)):
                print("TIME", time[i], "RATING", ratings[i], "ROUTE", routes[i])

        elif choice == "2":
            mea = MultiInstanceEAlgorithm(set_specimen=True)
            best, worst, avg, std = mea.execute_algorithm(times=10)
            Plotter().grouped_barplot(best, worst, avg, std, ["", "", "", ""], ["", "", "", ""], "", "")
        pass

    def custom_instance_menu(self):
        print("Pojedynczy przypadek z parametrami:")
        print("1. Start")
        print("R - Powrót")
        choice = input()
        if choice == "1":
            ea_map = Map()
            ea = EAlgorithm()
            result = ea.run(ea_map)
            for elem in result.current_generation:
                print("Specimen:", elem.route, "rating:", elem.rating, elem.is_allowed)
            print("BEST:", result.select_best_allowed_specimen().route, result.select_best_allowed_specimen().rating)
        elif choice == "2":
            pass
        elif choice == "R" or "r":
            self.main_menu()
        else:
            pass
        pass
