import random

print("This is a game where you guess a number from 0 to 9")
print("Do you want to play against a human or a computer.\nPress H for human and C for computer.")
choice = input()

# this is the list that contains the numbers to guess
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

answer = random.choice(numbers)  # this picks a random number from the list

if choice == "H":

    while True:
        print("Please enter your name Player1.")
        player1 = input()  # this gets player 1s name

        print("Please enter your name Player2.")
        player2 = input()  # this gets player 2s name

        print("Player 1 please enter a number through 0 to 9")
        users_answer1 = int(input())  # this gets player 1s answer

        print("Player 2 please enter a number through 1 to 9")
        users_answer2 = int(input())  # this gets player 2s answer

        if users_answer1 == answer:  # this if else deals with player 1s loss or win
            print("You Won!\nCongratulations!", player1)
        else:
            print("You Lost! The answer is", answer)
            print("Better luck next time", player1)

        if users_answer2 == answer:  # this if else deals with player 2s loss or win
            print("You Won!\nCongratulations!", player2)
        else:
            print("You Lost! The answer is", answer)
            print("Better luck next time", player2)

        print("Do you want to play again?\nType Y or N.")

        play_again = input()

        if play_again == "Y":
            print("Thanks for playing again!")

        if play_again == "N":
            print("Hope you had fun!")
            break

if choice == "C":

    while True:
        print("Please enter your name Player.")
        player = input()  # this gets players name

        print("Player please enter a number through 0 to 9")
        users_answer = int(input())

        if users_answer == answer:  # this if else deals with player 1s loss or win
            print("You Won!\nCongratulations!", player)
        else:
            print("You Lost! The answer is", answer)
            print("Better luck next time", player)

        comp_answer = random.choice(numbers)

        if comp_answer == answer:
            print("The computer answer was right.")
        else:
            print("The computers answer was wrong.")

        if comp_answer == answer and users_answer != answer:
            print("Oh no the computer beat you!")

        if comp_answer != answer and users_answer == answer:
            print("Yay! You beat the computer.")

        if comp_answer != answer and users_answer != answer:
            print("Neither of you won!")

        print("Do you want to play again?\nType Y or N.")

        play_again2 = input()

        if play_again2 == "Y":
            print("Thanks for playing again!")

        if play_again2 == "N":
            print("Hope you had fun!")
            break
