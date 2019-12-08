class Map:
    def __init__(self, file: str) -> None:
        plik = open(file)
        map = []
        i: int = 0
        for linia in plik:
            linia = linia.split()
            for elem in linia:
                map[i].append(int(elem))
            i = i+1
        self.map = map
        plik.close()

    def get_z(self, x: int, y: int) -> int:
        return self.map[x][y]


class Points: #cała klasa do edycji
    def __init__(self, file: str) -> None:
        plik = open(file)
        point_list = []
        for linia in plik:
            linia = linia.split()
            # dodany profit jako czwarta cecha punktu
            dictionary: dict = {'x': int(linia[0]), 'y': int(linia[1]), 'z': int(linia[2]), 'profit': int(linia[3])}
            point_list.append(dictionary)
        self.points = point_list
        plik.close()

    def get_points_id(self) -> list:
        return self.points

    def get_max_points_num(self):
        return len(self.points)