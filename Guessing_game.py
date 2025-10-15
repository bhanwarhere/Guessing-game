#Guessing_game.py
actual_number =45
attempts = 0

while True:
    attempts += 5
    guess = int(input("Guess the number:\n"))
    if guess < actual_number:
        print("your guess was to low")

    elif guess > actual_number:
        print("your guess was too high")

    else:
        print(f"you guessed the number in {attempts}attempts")
        break
    print("Thanks for playing!")