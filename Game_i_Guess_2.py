import random

print("This is a game where you guess a number from 0 to 9")
print("Please enter your name Player.")
player1 = input()  # this gets players name
print("Do you want to play against a human or a computer.\nPress H for human and C for computer.")
choice = input()

# this is the list that contains the numbers to guess
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

answer = random.choice(numbers)  # this picks a random number from the list

if choice == "H":  # this is the player vs player mode
    print("Please enter your name Player2.")
    player2 = input()  # this gets player 2s name

    while True:
        # this is so that the number always changes every time the loop is run
        answer = random.choice(numbers)

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

        # This is used to determine whether to break from the loop or not
        print("Do you want to play again?\nType Y or N.")

        play_again = input()

        if play_again == "Y" or play_again == 'y':
            print("Thanks for playing again!")

        if play_again == "N" or play_again == 'n':
            print("Hope you had fun!")
            break

if choice == "C":  # this is the computer mode

    while True:
        # this is so that the number always changes every time the loop is run
        answer = random.choice(numbers)

        print("Player please enter a number through 0 to 9")
        users_answer = int(input())

        if users_answer == answer:  # this if else deals with player 1s loss or win
            print("You Won!\nCongratulations!", player1)
        else:
            print("You Lost! The answer is", answer)
            print("Better luck next time", player1)

        comp_answer = random.choice(numbers)  # this takes the cpus answer

        if comp_answer == answer:  # this deals with the computers loss or win
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

        if play_again2 == "Y" or play_again2 == 'y':  # this sees if it should break from the loop
            print("Thanks for playing again!")

        if play_again2 == "N" or play_again2 == 'n':
            print("Hope you had fun!")
            break
