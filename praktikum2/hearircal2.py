class Family:
    def __init__(self, name, age, blood):
        self.name = name
        self.age = age
        self.blood = blood
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_blood(self):
        return self.blood
    
class Grandparents(Family):
    def __init__(self, name, age, blood, status):
        super().__init__(name, age, blood)
        self.status = status
    def get_status(self):
        return self.status
    
class Parents(Family):
    def __init__(self, name, age, blood, work):
        super().__init__(name, age, blood)
        self.work = work
    def get_work(self):
        return self.work

class Children(Parents):
    def __init__(self, name, age, blood, work, religion):
        super().__init__(name, age, blood, work)
        self.religion = religion
    def get_religion(self):
        return self.religion
