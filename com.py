#Calculates the centre of mass of a composite shape on a 2d plane
#!python3
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
            
    i = 0
    totalWeight = 0
    while i < n:
        totalWeight += objectsMass[i]
        i+=1
    
    #xcomponent of the com
    i = 0
    xWeights = 0
    while i < n:
        xWeights += objectsMass[i] * objectsXPos[i]
        i+=1
    xPos = xWeights / totalWeight
    #ycomponent of the com
    i = 0
    yWeights = 0
    while i < n:
        yWeights += objectsMass[i] * objectsYPos[i]
        i+=1
    yPos = yWeights / totalWeight

    print("The x component of the centre of mass of the composite object is: " + str(xPos) + " and the y component is: " + str(yPos))
objects()

