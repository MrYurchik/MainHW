print("input-nachalo")
nachalo = input()
print("input-konec")
konec = input()
i = 0
spisokBisocosnix = []
chislo = 0
if nachalo.isdigit():
    nachalo = int(nachalo)
else:
  print("PLOXOI BBOD")
if konec.isdigit():
    konec = int(konec)
else:
  print("PLOXOI BBOD")
spisok = list(range(nachalo, konec))
print(spisok)
k = konec-nachalo-1
for chislo in spisok:
    if chislo % 400 == 0 or (chislo % 4 == 0 and chislo % 100 != 0):
        spisokBisocosnix.append(chislo)
print(spisokBisocosnix)



