import math


class Map:
    def __init__(self, file: str = "points.txt") -> None:
        f = open(file)
        i: int = 0
        self.map = []
        for line in f:
            line = line.split()
            dictionary: dict = {'x': int(line[0]), 'y': int(line[1]), 'z': int(line[2]), 'profit': int(line[3])}
            self.map.append(dictionary)
        f.close()

    def get_z(self, point_id: int) -> int:
        return self.map[point_id]['z']

    def get_xy_len(self, point_id: int) -> float:
        return math.sqrt(self.map[point_id]['x']**2 + self.map[point_id]['y']**2)

    def get_profit(self, point_id: int):
        return self.map[point_id]['profit']

    def get_max_point(self):
        return len(self.map)

