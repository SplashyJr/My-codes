import math


class calculator:

    y = None
    x = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y

    def power(self):
        return pow(self.x, self.y)

    def squareroot(self):
        return math.sqrt(self.x)


if __name__ == '__main__':
    while(True):

        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        calc = calculator(num1, num2)

        print("Select operation:")
        print("1.Add")
        print("2.Subtract")
        print("3.Mutiply")
        print("4.Divide")
        print("5.Power")
        print("6.Squareroot")

        choice = input("Enter 1, 2, 3, 4, 5, 6: ")

        if(choice == "1"):
            print("Your Result was {}".format(calc.add()))

        elif(choice == "2"):
            print("Your Result was {}".format(calc.subtract()))

        elif(choice == "3"):
            print("Your Result was {}".format(calc.multiply()))

        elif(choice == "4"):
            print("Your Result was {}".format(calc.divide()))

        elif(choice == "5"):
            print("Your Result was {}".format(calc.power()))

        elif(choice == "6"):
            print("Your Result was {}".format(calc.squareroot()))

        else:
            print("Invalid input")
