import random

Z = 0
name = input("Enter your name ")
print("PRIBET - " + name)
plus_xod = int(random.random() * 10)
minus_xod = int(random.random() * 10)
double_xod = int(random.random() * 10)


def kidok():
    # локальні змінні і глобал Z
    global Z
    n = 0
    xod = int(random.random() * 10)
    xod2x = int(random.random() * 10)

    # Іфчики перевіряючі скільки вам нарандомило
    if xod == 0:

        print("xod nazad")

        print(xod)

        n = n - 1

    elif xod == 1 or xod == 2 or xod == 3:

        print("Odin xod Bpered")

        print(xod)

        n = n + 1

    elif xod == 4 or xod == 5 or xod == 6:

        n = n + 2

        print("Dva xod Bpered")

        print(xod)

    else:

        n = n + 3

        print("tri xod Bpered")

        print(xod)
    if xod == xod2x:
        print("Bonusnii xod")
        kidok()
    Z = Z + n
    # Плюс мінус і дабл скор, рандомиться на початку ^^^^
    if Z % plus_xod == 0:
        print("U win +1 score")
        Z = Z + 1
    elif Z % minus_xod == 0:
        print("U lost 1 score")
        Z = Z - 1
    elif Z % double_xod == 0:
        print("U double your score")
        Z = Z * 2

    print("Bi prowli' {} kletok".format(Z))

#Цикл з меню


while True:
    print("Menu:")
    print("Eneter 'GO' to begin the game")
    print("Eneter 'SCORE' to get the score")
    print("Eneter 'quit' to end the game")
    vopros = input()

    if vopros == "GO":

        kidok()
    elif vopros == "SCORE":

        print(Z)
    elif vopros == "quit":
        break
    else:
        print("Eror enter")

    if Z >= 100:
        print("Peremoga!")
        break
