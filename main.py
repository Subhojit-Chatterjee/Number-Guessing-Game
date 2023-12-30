import random
import logo


def number_checker(correct_answer, chances):
    # This function takes the correct answer and the number of turns to guess and checks whether the user got it right
    for i in range(0, chances):
        print(f"You have {chances - i} remaining to guess the number.")
        user_answer = int(input("Make a guess: "))

        if user_answer > correct_answer:
            print("Too high.")
        elif user_answer < correct_answer:
            print("Too low.")
        elif user_answer == correct_answer:
            return 0
    return -1


def set_difficulty():
    # This function set the difficulty of the game depending on user's choice.
    difficulty_level = input("I'm thinking of a number between 1 and 100.\nChoose a difficulty."
                             " Type 'easy' or 'hard': ")
    if difficulty_level == "easy":
        return 10
    elif difficulty_level == "hard":
        return 5
    else:
        print("Wrong choice! Please try again.")


def game():
    # This is the main game function that controls the flow of the game.
    secret_number = random.randint(0, 100)
    print(logo.logo)
    print("Welcome to the number guessing game!")
    no_of_chances = set_difficulty()
    result = number_checker(secret_number, no_of_chances)
    if result == 0:
        print("\nCongrats! You got it right.")
    elif result == -1:
        print(f"Sorry! You couldn't guess the number.\n The correct answer is {secret_number}")


game()
