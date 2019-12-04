import random
from solution import Solution

class Population:
    def __init__(self, t: int, points: list, size: int = 30) -> None:
        self.size = size
        self.t = t
        # wstepna inicjalizacja dla t=0
        self.solutions = []
        for i in range(len(points)):
            self.solutions.append(random.randrange(1, len(points), 1))
        # korzystam z  random.randrange(start, stop[, step])

    def copy(self, previous_population) -> None:
        self.size = previous_population.size
        self.t = previous_population.t + 1
        self.solutions = []  # napisać funkcję tworzącą nową populację ze starej

    def get_size(self) -> int:
        return self.size

    def get_solution(self, number) -> Solution:
        return self.solutions[number]