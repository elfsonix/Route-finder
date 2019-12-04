import random


class Solution(object):
    pass


class Rover:
    def __init__(self, start_weight: float, start_location: int) -> None:
        self.current_weight = start_weight
        self.current_location = start_location

    def go(self, route: Solution):
        return 1 # koszt przebytej trasy

class Solution:
    def __init__(self, points: list) ->None:
        self.route = points

    def get_length(self):
        return len(self.route)

    def goal(self) -> float:
        return Rover.go(self)

    def punishment(self) -> float:
        pass

    def rate(self, alfa: float = 1, beta: float = 1):
        return alfa*self.goal() + beta*self.punishment()


class Population:
    def __init__(self, t: int, points: list, size: int = 30) -> None:
        self.size = size
        self.t = t
        # wstepna inicjalizacja dla t=0
        self.solutions = []
        for i in range(len(points)):
            self.solutions.append(random.randrange(1, len(points), 1))
        # korzystam z  random.randrange(start, stop[, step])

    def __init__(self, previous_population) -> None:
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

class Points: #cała klasa do edycji

    def __init__(self, file: str) -> None:
        plik = open(file)
        point_list = []
        for linia in plik:
            linia = linia.split()
            dictionary: dict = {'x': int(linia[0]), 'y': int(linia[1]), 'z': int(linia[2])}
            point_list.append(dictionary)
        self.points = point_list
        plik.close()

    def get_points_id(self) -> list:
        return self.points