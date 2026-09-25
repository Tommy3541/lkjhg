import random

hrac = [
  "Sobeslav",
  "Jarmila",
  "John",
  "Mohi",
  "marek",
  "dan"
]

souper = [
  "jiri",
  "adam",
  "libuse",
  "kristyna",
  "profi",
  "mohyprofi"
]


def hod_hrace():
    nahodne_cislo = random.randint(0, 5)
    hrac.pop(nahodne_cislo)

def hod_soupere():
    nahodne_cislo2 = random.randint(0, 5)
    souper.pop(nahodne_cislo2)

hod_hrace()
hod_soupere()