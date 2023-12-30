import random
import logo


def number_guesser(correct_answer, chances):
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


secret_number = random.randint(0, 100)
print(logo.logo)
print("Welcome to the number guessing game!")
result = 0
difficulty_level = input("I'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ")
if difficulty_level == "easy":
    result = number_guesser(secret_number, 10)
elif difficulty_level == "hard":
    result = number_guesser(secret_number, 5)
else:
    print("Wrong choice! Please try again.")

if result == 0:
    print("Congratulations! You got it right.")
else:
    print(f"You couldn't guess the number. You lose!\nThe correct answer is {secret_number}")
