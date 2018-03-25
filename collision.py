class Ball:
    mass = 1.00
    speed = 0.00
    colour = "white"
    radius = 1.00
    name = ""
    type = ""

    def properties(self):
        properties = "Ball " + str(self.name) + " has a mass of " + str(self.mass) + " and a speed of " + str(
            self.speed) + ". It is a " + str(self.type) + " ball of colour " + str(self.colour)
        return properties


balls = list()
for i in range(16):
    balls.append(Ball())

e = 1
x = 0

while x < 15:
    if x == 0:
        balls[x].name = "cue"
        balls[x].type = "cue ball"
    if x == 1:
        balls[x].name = "8"
        balls[x].type = "8 ball"
    if (x % 2) == 0 & x != 1 & x != 0:
        balls[x].name = str(x - 1)
        balls[x].type = "solid"
    if (x % 2 == 1) & x != 1 & x != 0:
        balls[x].name = str(x - 2)
        balls[x].type = "striped"
    x += 1


def program():
    def collision(u1, u2, m1, m2):
        momentum = float(u1 * m1) + float(u2 * m2)

        v1 = (float(momentum) - float(float(e) * float(m2) * ((float(u1) - float(u2))))) / (float(m1) * float(m2))
        v2 = (float(momentum) - float(v1) * float(m1)) / float(m2)
        return [v1, v2]

    def menu():
        print("1: View the properties of a ball")
        print("2: Change the properties of a ball")
        print("3: Change the coefficient of restitution")
        print("4: Simulate collision between two balls")
        selection = input("Please select an option:")

        if selection == "1":
            ball = int(input("Which ball would you like to view?")) - 1
            print(balls[ball].properties())
            menu()

        if selection == "2":
            ball = int(input("Which ball would you like to change the properties of?")) - 1
            balls[ball].speed = input("Enter the new speed of the ball:")
            balls[ball].mass = input("Enter the new mass of the ball:")
            menu()

        if selection == "3":
            e = input("Enter the coefficient of restitution:")
            menu()

        if selection == "4":
            ball1 = int(input("Please enter the first ball in the collision")) - 1
            ball2 = int(input("Please enter the second ball in the collision")) - 1
            print("These are the properties of the balls after the collision:")
            finalspeeds = collision(float(balls[ball1].speed), float(balls[ball2].speed), float(balls[ball1].mass),
                                    float(balls[ball2].mass))
            balls[ball1].speed = finalspeeds[0]
            balls[ball2].speed = finalspeeds[1]
            print(balls[ball1].properties())
            print(balls[ball2].properties())
            menu()

    menu()


program()
