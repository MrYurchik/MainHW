i = input("BBedite Birajenie: ")


def proмerka(i):
    z = 0
    i = list(i)
    count1 = 0
    for z in range(len(i)):
        if i[z] == "(":
            count1 = count1 - 1
            z += 1
        elif i[z] == ")":
            count1 = count1 + 1
            z += 1
        else:
            z += 1
    if count1 == 0:
        print("Bse XOROWO")
    else:
        print("Bse ploxo")


proмerka(i)
