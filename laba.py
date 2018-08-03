import HW.Lub


class Market(HW.Lub.Building):
    def __init__(self, material, color, number=0):
        super////////(питання щодо супер)
        self.material = material
        self.color = color
        self.number = number

    def plus(self, number):
        self.number = number + number


white_brick = Market(color="white", number=300, material="brick")
brown_plank = Market(color="brown", number=20, material="plank")
print(white_brick)




