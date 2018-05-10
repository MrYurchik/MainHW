y = 0
print("input-god")
x = input()
if x.isdigit():
    x = int(x)
    if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0):
        print("XAROW")
    else:
        print("ne XAROW")
        if x % 4 == 3:
            x += 1
            print("blijaewii", x)
        elif x % 4 == 2:
          x = y
          x += 2
          y -= 2
          print("blijaewii", x, y, sep=" and ")
        else:
          x -= 1
          print("blijaewii", x)
else:
  print("PLOXOI BBOD")