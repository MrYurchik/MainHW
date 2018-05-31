import HW.Lub
print(HW.Lub.white_brick)
yellow_brick = HW.Lub.Building(color="yellow", number=200, material="brick")
red_plank = HW.Lub.Building(color="red", number=10, material="plank")
print(vars())
yellow_brick.plus(1)
red_plank.minus(2)
print(vars())