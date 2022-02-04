
from ship import Ship
from dot import Dot

class Board_Exception(Exception):
    pass

class Board_Exception_Ship(Board_Exception):
    pass

class Bord_Exception_Out(Board_Exception):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"

class Bord_Exception_used(Board_Exception):
    def __str__(self):
        return "Вы уже стреляли в эту клетку!"

class Board: #класс доски
    def __init__(self, hid):
        self.hid = hid # видимость поля
        self.razmer = 6
        self.ships = [] #перечень кораблей
        self.ships_x = [] #стреленные точки
        self.fields = [["_" for _ in range(self.razmer)] for _ in range(self.razmer)]
        self.ship_death = 0 #стрел корабли

    def out(self, dot):
        if dot.x < 0 or dot.x > (self.razmer - 1) or dot.y < 0 or dot.y > (self.razmer - 1):
            return True
        else:
            return False

    def add_ship(self, ship):
        for a in ship.dots:
            if a in self.ships_x or self.out(a):
                raise Board_Exception_Ship()
        for a in ship.dots:
            self.fields[a.x][a.y] = "0"
            self.ships_x.append(a)
            self.ships.append(ship)
            self.contour(ship)

    def contour(self, ship, vfb = False): #рисует контр
        dx_dy = [(-1, -1), (0, -1), (1, -1),
                 (-1, 0), (1, 0),
                 (-1, 1), (0, 1), (1, 1), (0, 0)]
        for a in ship.dots:
            for dx, dy in dx_dy:
                kontr = Dot(a.x + dx, a.y + dy)
                if not self.out(kontr) and kontr not in self.ships_x:
                    self.ships_x.append(kontr)
                    if vfb:
                        self.fields[kontr.x][kontr.y] = "."


    def print_fild(self):
        print("_|1|2|3|4|5|6|")
        for a in range(self.razmer):
            print(f"{a+1}|", end="")
            for b in range(self.razmer):
                if not self.hid and self.fields[a][b] == "0":
                    print("_|", end="")
                else:
                    print(f"{self.fields[a][b]}|", end="")
            print()

    #метод выстрела
    def shot(self, dot):
        if self.out(dot):
            raise Bord_Exception_Out()
        if dot in self.ships_x:
            raise Bord_Exception_used()
        self.ships_x.append(dot)
        for k in self.ships:
            if dot in k.dots:
                k.lives -= 1
                self.fields[dot.x][dot.y] = "X"
                if k.lives == 0:
                    print("Убит!")
                    self.contour(k, True)
                    self.ship_death += 1
                    return False
                else:
                    print("Ранен!")
                    return True
        self.fields[dot.x][dot.y] = "."
        print("Мимо!")
        return False