class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color
    
class Mammal(Animal):
    def __init__(self, name, color, fur):
        super().__init__(name, color)
        self.fur = fur
    def get_fur(self):
        return self.fur
    
class Giraffe(Animal):
    def __init__(self, name, color, height):
        super().__init__(name, color)
        self.height = height
    def get_height(self):
        return self.height

class Insect(Mammal):
    def __init__(self, name, color, wingspon, scale):
        super().__init__(name, color, wingspon)
        self.scale = scale
    def get_scale(self):
        return self.scale