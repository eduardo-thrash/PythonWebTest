cost = 0

def BranSelecter(nameBrand): 
    validate = False
    while validate != True:       
        if(nameBrand == "Ford" or nameBrand == "Chevrolet" or nameBrand == "Fiat"):
            if(nameBrand == "Ford"):
                brandCost = 100000
            elif(nameBrand == "Chevrolet"):
                brandCost = 120000
            elif(nameBrand == "Fiat"):
                brandCost = 80000
            validate = True          
        else:
            print("\noption {} is invalid. The options are: 'Ford', 'Chevrolet' or 'Fiat'".format(nameBrand))
            nameBrand = str(input("Enter brand of car among 'Ford', 'Chevrolet' and 'Fiat'... "))
    print("\n additional cost for brand {}: {}".format(nameBrand, brandCost))
    return brandCost

def DoorsSelecter(doorsNumber):
    validate = False
    while validate != True:
        if(doorsNumber == 2 or doorsNumber == 4 or doorsNumber == 5):
            if(doorsNumber == 2):
                doorsNumberCost = 50000
            elif(doorsNumber == 4):
                doorsNumberCost = 65000
            elif(doorsNumber == 5):
                doorsNumberCost = 78000
            validate = True
            doors = doorsNumber
        else:
            print("\doors number {} is invalid.!!!".format(doorsNumber))
            doorsNumber = int(input("Enter doors number... "))
    print("\n additional cost for {} doors: {}".format(doorsNumber, doorsNumberCost))
    return doorsNumberCost

def ColorSelecter(nameColor):
    validate = False
    while validate != True:
        if(nameColor == "White" or nameColor == "Blue" or nameColor == "Black"):
            if(nameColor == "White"):
                colorCost =  10000
            elif(nameColor == "Blue"):
                colorCost =  20000
            elif(nameColor == "Black"):
                colorCost =  30000
            validate = True
            color = nameColor
        else:
            print("\noption {} is invalid.!!!".format(nameColor))
            nameColor = str(input("Enter color of car among 'Black', 'White' and 'Blue'... "))
    print("\n additional cost for {} color: {}".format(nameColor, colorCost))
    return colorCost

name = str(input("Enter name and surname of buyer... "))

brand = str(input("Enter brand of car among 'Ford', 'Chevrolet' and 'Fiat'... "))
cost = cost + BranSelecter(brand)

doors = int(input("Enter doors number... "))
cost = cost + DoorsSelecter(doors)

color = str(input("Enter color of car among 'Black', 'White' and 'Blue'... "))
cost = cost + ColorSelecter(color)

print("\n The Cost of car for {} is: {}".format(name, cost))