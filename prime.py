import sys

def prime():

    print('''This function will print all prime numbers in between a range given by the user.''')
    low = int(input("Please provide a starting number: \n"))
    high = int(input("Please provide an ending number: \n"))
    if low <= 0 or high <= 0:
        sys.exit("Your number is either zero or negative")
    else:
        for number in range(low, high+1):
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                print("{} is a prime number!\n".format(number))


prime()
