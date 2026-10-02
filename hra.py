import random
import time

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

maxhrac = 5
maxsouper = 5

while True:
    inasdasda = input("chcete hodit kostku: \n")
    if inasdasda == "ano":
        time.sleep(0.5)
        rand = random.randint(0, maxhrac)
        print(f"  bylo zabito {rand} soudruhu")
        time.sleep(0.5)
        for x in range(rand):
            number = random.randint(0, (len(hrac)-1))
            
            print(f"{hrac[number]} was killed") 
            hrac.pop(number)
            time.sleep(0.5)
        rand = random.randint(0,maxsouper)
        print(f"  bylo zabito {rand} souperu")
        for x in range(rand):
            number = random.randint(0, (len(souper)-1))
    
            print(f"{  souper[number]} was killed") 
            souper.pop(number)
            time.sleep(0.5)

        print(f"\n   zbyvajici pocet souperu {len(souper)} a zbyvaciji pocet hracu {len(hrac)}")

        maxhrac = len(hrac)
        maxsouper = len(souper)

        if len(souper) == 0:
            print("vyhra")
        elif len(hrac) == 0:
            print("prohra")
            break
        elif len(hrac) == 0 and len(souper) == 0:
            print("remiza")
            break
                

                

<<<<<<< HEAD
            def hod_soupere():
                for x in range(random.randint(0,5)):
                    hrac.pop(random.randint(0, (len(hrac)-1)))
                    
hod_hrace()
hod_soupere()
=======

>>>>>>> 22ea772d2ddd1f1b37a31dd443038c83322629a2
