invoer = ""
totaal_ex_btw = 0

while not invoer.lower() == "einde":
    procent= 0
    aantal = int(input("geef aantal in"))
    prijs = float(input("geef de prijs in"))
    regeltotaal = aantal*prijs
    korting_jofn  = input("korting")
    if(korting_jofn == "ja"):
        procent = int(input("geeft aantal procent"))
        regeltotaal = regeltotaal-regeltotaal*(procent/100)
    print("{} stuks aan {} = {} korting {} procent".format(aantal,prijs,regeltotaal, procent))
    totaal_ex_btw = totaal_ex_btw+regeltotaal
    invoer = input("verder of einde")

if(totaal_ex_btw>500):
    totaal_ex_btw = totaal_ex_btw*0.95

print("bedrag ex btw: {}\nbtw: {}\ntotaal btw incl: {} ".format(totaal_ex_btw,
                                                                round(totaal_ex_btw*0.21,2),
                                                                round(totaal_ex_btw*1.21,2)
                                                                ))



