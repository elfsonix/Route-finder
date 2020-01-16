from evolutionary_algorithm import EAlgorithm
from multi_track_drifting import MultiInstanceEAlgorithm
from map import Map
from output_presentation import Plotter


class GUI:
    def __init__(self):
        print("Algorytm ewolucyjny analizujący trasę łazika z poborem próbek")
        print("Stworzony na zajęcia 'Matematyczne Metody Wspomagania Decyzji', III rok AiR I stopnia, WEAIiIB, AGH")
        print("Jacek Lichwa, Karolina Świerczek, Sonia Wittek")
        print()
        print("Wprowadź znak aby wybrać opcję z listy")
        pass

    def main_menu(self):
        print("1. Pojedyncze uruchomienie")
        print("2. Wielokrotne uruchomienie dla różnych przypadków")
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
        pass

    def custom_instance_menu(self):
        print("Pojedynczy przypadek z parametrami:")
        print("1. Domyślnymi")
        print("2. Wprowadzonymi")
        print("3. Losowymi")
        print("R - Powrót")
        choice = input()
        if choice == "1":
            ea_map = Map()
            ea = EAlgorithm()
            result = ea.run(ea_map)
            for elem in result.current_generation:
                print("Specimen:", elem.route, "rating:", elem.rating)
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "R" or "r":
            self.main_menu()
        else:
            pass
        pass
