from player import Player
from random import randint
from dot import Dot
#класc аи

class AI(Player):
    def ask(self):
        a = Dot(randint(0, 5), randint(0, 5))
        print(f"Компьютер ходит на {a.x+1}, {a.y+1}")
        return a
    