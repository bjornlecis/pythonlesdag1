import math

aantal_m2 =0.0
aantal_muren = int(input("geef het aantal muren"))
for i in range(0,aantal_muren):
    breedte = float(input("geef de breedte van de muur in m"))
    hoogte = float(input("geef de hoogte van de muur in m"))
    aantallagen=int(input("1 of 2 lagen"))
    oppv = breedte*hoogte*aantallagen
    aantal_m2 += oppv

aantal_uur = math.ceil(aantal_m2/15)
aantal_litter = math.ceil(aantal_m2/5)
kostprijs = aantal_uur*30+aantal_litter*3
print("prijs ex btw = {}\nbtw ={}\nprijs btw in = {}".format(kostprijs,
                                                           kostprijs*0.21,
                                                           kostprijs*1.21))


