"""
for i in range(10,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("")
"""
veelvoud = int(input("geef je veelvoud in"))
einde = int(input("geef het einde in"))
verm = 0
#controleren als het veelvoud kleiner dan het einde
while(veelvoud > einde):
    print("het veelvoud moet kleiner zijn dan het einde")
    veelvoud = int(input("geef je veelvoud in"))


teller = 1
#afdrukken van de veelvouden
while(verm < einde):
    verm = veelvoud*teller
    print(verm)
    teller = teller+1
