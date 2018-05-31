class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self.number = number
        self.place_place()

    def __repr__(self):
        return "Building(%r, %r, %r)" % (self.material, self.color, self.number)

    def __str__(self):
        return "material=%s, color=%s, number=%s" % (self.material, self.color, self.number)

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


b = Building("asd", "red")
print(b.__repr__())
c = eval(b.__repr__())
c.color = "blue"
print(c)
print(b)
print(b.material, b.color, b.number, b.place)

