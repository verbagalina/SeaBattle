from board import Board, Board_Exception_Ship
from dot import Dot
from ship import Ship
from ai import AI
from user import User
from random import randint


#класс игры

class Game:
    def __init__(self):
        komp_b = self.random_board(False)
        user_b = self.random_board(True)
        #komp_b = Board(False)
        #user_b = Board(True)
        self.komp_ai = AI(komp_b, user_b)
        self.user = User(user_b, komp_b)



    def greet(self): #приветствие
        print('''Приветствую Вас в игре 'Морской бой'! 
        Формат ввода для игры Х У, где Х - номер строки, У - номер столбца. 
        Вводить необходимо целые числа от 1 до 6 через пробел.''')

    def loop(self): #игровой цикл
        tur = 1
        while True:
            print("Доска пользователя")
            self.user.b_user.print_fild()
            print("Доска компьютера")
            self.komp_ai.b_user.print_fild()
            a = False
            if tur % 2 == 1:
                print("Ходит пользователь!")
                a = self.user.move()
            else:
                print("Ходит компьютер!")
                a = self.komp_ai.move()
            if not a:
                tur += 1
            if self.user.b_user.ship_death == 7:
                print("Выиграл компьютер!")
                break
            if self.komp_ai.b_user.ship_death == 7:
                print("Выиграл пользователь!")
                break

    def start(self):
        self.greet()
        self.loop()

    def add_ships(self, hid):
        list_b = [1, 1, 1, 1, 2, 2, 3]
        board = Board(hid)
        for a in list_b:
            iterations = 0
            while True:
                iterations += 1
                if iterations > 2000:
                    return None
                vg = randint(0, 1)
                if a == 1:
                    ko = Ship(Dot(randint(0, 5), randint(0, 5)), a, vg)
                else:
                    if vg == 0:
                        ko = Ship(Dot(randint(0, (6 - a)), randint(0, 5)), a, vg)
                    else:
                        ko = Ship(Dot(randint(0, 5), randint(0, (6 - a))), a, vg)
                try:
                    board.add_ship(ko)
                    break
                except Board_Exception_Ship:
                    pass

        board.ships_x = []
        return board

    def random_board(self, hid):
        board = None
        while board is None:
            board = self.add_ships(hid)
        return board

