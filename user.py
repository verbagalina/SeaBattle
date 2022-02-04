from player import Player
from dot import Dot

#класс игрока чел

class User(Player):
    def ask(self):
        while True:
            a = input("Введите координаты Х и Н от 1 до 6 через пробел:").split()
            if len(a) != 2:
                print("Введено некорректное значениею")
                continue
            elif not a[0].isdigit() or not a[1].isdigit():
                print("Введено некорректное значениею")
                continue
            else:
                return Dot(int(a[0]) - 1, int(a[1]) - 1)
