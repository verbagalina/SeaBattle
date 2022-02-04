from dot import Dot
# класс кораблей
class Ship:
    def __init__(self, D, L, VG):
        self.D = D
        self.L = L
        self.VG = VG #если тру то горизонтально, фолс - вертикально
        self.lives = L
    @property
    def dots(self):
        list_dots = []
        x_temp = self.D.x
        y_temp = self.D.y
        for _ in range(self.L):
            list_dots.append(Dot(x_temp, y_temp))
            if self.VG:
                x_temp += 1
            else:
                y_temp += 1
        return list_dots