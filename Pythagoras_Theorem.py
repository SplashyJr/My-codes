# this is a program that uses the Pythagoras's theorem
# to calculate the hypotenuse or other side of a right angled triangle

import math  # this is needed so i could use math.sqrt

print("Hi are u trying to find the length of the hypotenuse or one of the two sides")

print("Enter H for Hypotenuse or S for another side")

userinput = input()

if userinput == "H":  # this is for the hypotenuse
    print("Enter the length of the two sides.\nDo not enter them as squares I automatically square them.")

    side1 = int(input())
    side2 = int(input())

    hypotenuse = side1 * side1 + side2 * side2
    thypotenuse = math.sqrt(hypotenuse)

    print("The length of the hypotenuse is", thypotenuse)

if userinput == "S":  # this is for the other side
    print("Enter the length of the hypotenuse")

    Hypotenuse2 = int(input())

    print("Please enter the side")

    Side3 = int(input())

    side_first_part_of_formula = Hypotenuse2 * Hypotenuse2 - Side3 * Side3
    sidefinally = math.sqrt(side_first_part_of_formula)

    print(sidefinally)
