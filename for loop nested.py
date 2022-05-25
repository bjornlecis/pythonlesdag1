tafel = int(input("tot welke tafel wens je te gaan"))
eind = int(input("hoeveel keer moet er vermenigvuldigd worden"))

for i in range(1,eind+1):
    for j in range(1,tafel+1):
        print(i*j,end="\t")
    print("")
