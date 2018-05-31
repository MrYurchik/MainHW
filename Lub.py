class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self.number = number
        self.place = 0
        self.place_place()

    def __repr__(self):
        return "Building(%r, %r, %r)" % (self.material, self.color, self.number)

    def __str__(self):
        return "material=%s, color=%s, number=%s, places=%s" % (self.material, self.color, self.number, self.place)

    def plus(self, plus1):
        self.number = self.number + plus1

    def minus(self, minus1):
        self.number = self.number - minus1

    def set_material(self, value):
        self.material = value

    def set_color(self, value):
        self.color = value

    def set_number(self, value):
        self.number = value

    def place_place(self):
        if self.number < 0:
            self.place = "out of stock"
        elif 0 < self.number < 100:
            self.place = "warehouse"
        else:
            self.place = "Remote warehouse"


white_brick = Building(color="white", number=300, material="brick")
brown_brick = Building(color="brown", number=20, material="plank")
print(white_brick)
print(brown_brick)
white_brick.plus(50)
brown_brick.minus(3)
print(white_brick)
print(brown_brick)

