def program():
    e = input("Enter the coefficient of restitution:")

    speed1 = input("Enter the speed of the first ball:")
    mass1 = input("Enter the mass of the first ball")

    speed2 = input("Enter the speed of the second ball:")
    mass2 = input("Enter the mass of the second ball")


    def collision(u1, u2, m1, m2):

        momentum = float(u1*m1) + float(u2*m2)

        v1 = (float(momentum) - float(float(e) * float(m2) * (float(u1) - float(u2)))) / (float(m1) * float(m2)) 
        v2 = (float(momentum) - float(v1) * float(m1)) / float(m2)

        print("The total momentum of the system is: ", momentum)
        print("The speed of the first ball after collision is: ", v1)
        print("The speed of the second ball after collision is: ", v2)

    collision(float(speed1), float(speed2), float(mass1), float(mass2))

program()
