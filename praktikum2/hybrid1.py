class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Drawable:
    def draw(self):
        print("Drawing object at: ", self.x, self.y)

class Moveable:
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Player(GameObject, Drawable, Moveable):
    def __init__(self, x, y):
        super().__init__(x, y)
    def update(self):
        self.move(1, 1)
        self.draw()