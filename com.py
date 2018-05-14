#Calculates the centre of mass of multiple objects on a 2d plane

objectsMass = []    
objectsXPos = []
objectsYPos = []

def objects():
    n = 0
    x = True
    while x:
        n+=1
        objectsMass.append(int(input("Please enter the mass of the object on the 2d plane: ")))
        objectsXPos.append(int(input("Please enter the X position of the object on the 2d plane: ")))
        objectsYPos.append(int(input("Please enter the Y position of the object on the 2d plane: ")))
        increment = input("Add another object? yes/no: ")
        if increment == "yes":
            x = True
        else:
            x = False
objects()
