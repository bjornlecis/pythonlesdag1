#even of oneven
""""
x = int(input("geef de waarde van x in"))
if(x%2 == 0):
    print("het getal is even")
else:
    print("het getal is oneven")
"""
#keuze dollar pond.
munt = input("kies uit pond/dollar")

if(munt.lower() == "dollar" or munt.lower() == "pond"):
    euro = float(input("geef het bedrag in euro in"))
    if(munt.lower() == "dollar"):
        print("{} euro is {} dollar".format(euro,round(euro*1.07,2)))
    else:
        print("{} euro is {} pond".format(euro,round(euro*0.85,2)))
else:
    print("Enkel dollar of pond")
