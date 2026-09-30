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
                for x in range(random.randint(0,5)):
                    souper.pop(random.randint(0, (len(souper)-1)))

            def hod_soupere():
                for x in range(random.randint(0,5)):
                    hrac.pop(random.randint(0, (len(hrac)-1)))

hod_hrace()
hod_soupere()
