cost = 0
brands = {"Ford": 100000, "Chevrolet": 120000, "Fiat": 80000}
doors = {"2": 100000, "4": 120000, "5": 80000}
colors = {"Blue": 100000, "White": 120000, "Black": 80000}

def ColorSelecter(colorName):
    validate = False
    while validate != True: 
        if(colors.get(colorName)):
            validate = True
            print("\nAdditional cost for {} color: {}".format(colorName, colors[colorName]))         
        else:
            print("\noption {} is invalid. Enter again'".format(colorName))
            colorName = str(input("Enter Car color among {} ... ".format(", ".join(colors))))
    return colors[colorName]

def DoorsSelecter(doorsNumber):
    validate = False
    while validate != True:
        if(doors.get(doorsNumber)):
            validate = True
            print("\nAdditional cost for {} doors: {}".format(doorsNumber, doors[doorsNumber]))
            return doors[doorsNumber]
        else:
            print("\noption {} is invalid. Enter again'".format(doorsNumber))
            doorsNumber = str(input("Enter Car doors among {} ... ".format(", ".join(doors))))

def BrandSelecter(brandName):
    validate = False
    while validate != True:
        if(brands.get(brandName)):
            validate = True
            print("\nAdditional cost for brand {}: {}".format(brandName, brands[brandName]))
            return brands[brandName]
        else:
            print("\noption {} is invalid. Enter again'".format(brandName))
            brandName = str(input("Enter brand of car among {} ... ".format(", ".join(brands))))

name = str(input("Enter name and surname of buyer... "))

brand = str(input("Enter brand of car among {} ... ".format(", ".join(brands))))
cost = cost + BrandSelecter(brand)

door = str(input("Enter Car doors among {} ... ".format(", ".join(doors))))
cost = cost + DoorsSelecter(door)

color = str(input("Enter Car color among {} ... ".format(", ".join(colors))))
cost = cost + ColorSelecter(color)

print("\nThe Cost of car for {} is: {}".format(name, cost))