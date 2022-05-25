invoer = ""
som = 0
while(not invoer == "stop"):
    invoer = input("geef een invoer in")
    if (invoer == "stop"):
        break
    else:
        try:
            invoer = int(invoer)
            som = som+invoer
        except ValueError:
            print("geef een getal waarde in")
print("de som is = ", som)


