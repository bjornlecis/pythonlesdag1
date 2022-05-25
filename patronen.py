rijen = int(input("geef aantal rijen in"))
kol = int(input("geef aantal kolommen in"))

for i in range(0,rijen):
    for j in range(0,kol):
        if(i%2==0):
            print("x",end="\t")
        else:
            print("y",end="\t")
    print("")
