from random import randint

while True:
    max_num = int(input("Enter the max number to guess (e.g., 100): "))
    n = randint(1, max_num)
    a = -1
    guesses = 0

    while a != n:
        guesses += 1
        try:
            a = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if a > n:
            print("Too high!")
        elif a < n:
            print("Too low!")

        if a != n:
            diff = abs(n - a)
            if diff <= 5:
                print("You're very close!")
            elif diff <= 10:
                print(" Getting warm.")
            else:
                print("❄️ Cold guess.")

    print(f" Correct! The number was {n}.")
    print(f"Total guesses: {guesses}")

    again = input(" Play again? (y/n): ")
    if again.lower() != 'y':
        print(" Thanks for playing!")
        break
