class Rover:
    def __init__(self, start_weight: float, start_location: int) -> None:
        self.current_weight = start_weight
        self.current_location = start_location

class Solution:
    pass


class Population:
    def __init__(self, size: int, t: int, points:list) -> None:
        self.size = size
        self.t = t
        # wstepna inicjalizacja dla t=0
        self.solutions = [random.randrange(1, len(points), 1) for i in range(len(points))]
        # korzystam z  random.randrange(start, stop[, step])

        
    def __init__(self, previous_population: Population) -> None:
        self.size = previous_population.size
        self.t = previous_population.t + 1
        self.solutions = []  # napisać funkcję tworzącą nową populację ze starej

    def get_size(self) -> int:
        return self.size

    def get_solution(self, number) -> Solution:
        return self.solutions[number]


class Map:
    def __init__(self, file: str) -> None:
        plik = open(file)
        point_list = []
        for linia in plik:
            linia = linia.split()
            dictionary: dict = {'x': int(linia[0]), 'y': int(linia[1]), 'z': int(linia[2])}
            point_list.append(dictionary)
        self.points = point_list
        plik.close()
