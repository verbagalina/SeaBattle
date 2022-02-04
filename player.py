from board import Board
from board import Board_Exception
# класс игрока

class Player:
    def __init__(self, b_user, b_komp):
        self.b_user = b_user
        self.b_komp = b_komp

    def ask(self): #спрашивает игрока в какую кдетку делать выстрел
        raise NotImplementedError()

    def move(self): #метод ход игроков
        while True:
            try:
                a = self.ask()
                s = self.b_komp.shot(a)
                return s
            except Board_Exception as e:
                print(e)
