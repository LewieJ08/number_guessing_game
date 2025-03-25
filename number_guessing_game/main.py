import random
import os

def welcome_msg():
    print("Welcome to the Number Guessing Game!")
    print("Im thinking of a random number between 1 and 100.")
    print("You will be given a number of chances to guess the random number based on the difficulty you select\n")


def random_number():
    return random.randint(1,100)


def difficulty():
    print("Easy: 10 Chances")
    print("Meduim: 5 Chances")
    print("Hard: 3 Chances")

    while True:
        option = input("Select a Difficulty> ").lower().strip()
        if option == "easy":
            return 10
        elif option == "medium":
            return 5
        elif option == "hard":
            return 3
        else:
            print("Invalid input.")
            continue


def start_game():
    number = random_number()
    chances = difficulty()
    guesses = 0

    while guesses < chances:
        try:
            guess = int(input("Guess> "))
            guesses += 1
            if guess == number:
                print(f"Congratulations! You guessed the number in {guesses} guesses\n")
                return guesses
            
            elif guess <= 0 :
                print("Guess must be between 1-100")
                guesses -= 1
                continue
            
            elif guess >= 100 :
                print("Guess must be between 1-100")
                guesses -= 1
                continue

            elif guess != number:
                if guess > number:
                    print(f"Incorrect! The number is less than {guess}")
                    continue

                elif guess < number:
                    print(f"Incorrect! The number is greater than {guess}")
                    continue

        except ValueError:
            print("Invalid Input")
            continue

    print(f"Game over! You run out of chances. The number was {number}\n")
    return guesses

def main():
    os.system("cls")
    welcome_msg()
    while True:
        guesses = start_game()

        game_end = True
        while game_end:
            choice = input("Would you like to play again? (y/n)> ").lower().strip()
            if choice == "y":
                continue
            elif choice == "n":
                break
            else:
                print("Invalid input:")
            

if __name__ == "__main__":
    main()