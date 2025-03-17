import random
import os

def welcome_msg():
    print("Welcome to the Number Guessing Game!")
    print("Im thinking of a Random Number")
    print("You will be given a number of chances to guess the random number based on the difficulty you select")

def random_number():
    return random.randint(1,101)

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

def main():
    os.system("cls")
    welcome_msg()
    number = random_number()
    chances = difficulty()
    
if __name__ == "__main__":
    main()