class Child:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
    def get_details(self):
        print(f"Name: {self.name}, Birth: {self.birth}")

class Hospital(Child):
    def __init__(self, name, birth, id, Mom):
        super().__init__(name, birth)
        self.id = id
        self.Mom = Mom
    def get_details(self):
        super().get_details()
        print(f"ID: {self.id}, Mom's of: {self.Mom}")

class Baby(Hospital):
    def __init__(self, name, birth, id, Mom, blood):
        super().__init__(name, birth, id, Mom)
        self.blood = blood
    def get_details(self):
        super().get_details()
        print(f"Blood: {self.blood}")

baby = Baby("tasya", 3501, 20151139, "Muzdalifah", "B")
baby.get_details()