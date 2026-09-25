import random

hrac = [
  "Sobeslav",
  "Jarmila",
  "John",
  "Mohi",
  "marek",
  "dan",
]

souper = [
  "jiri",
  "adam",
  "libuse",
  "kristyna",
  "profi",
  "mohyprofi",
]

for hraci in hrac:
    for souperi in souper:
        if len(souper) == 0:
            print("vyhra")
        elif len(hrac) == 0:
            print("prohra")
            exit
        else:
            def hod_hrace():
                nahodne_cislo = random.randint(0, 5)
                souper.pop(nahodne_cislo)
                print(souperi)

            def hod_soupere():
                nahodne_cislo2 = random.randint(0, 5)
                hrac.pop(nahodne_cislo2)
                print(hraci)

hod_hrace()
hod_soupere()
