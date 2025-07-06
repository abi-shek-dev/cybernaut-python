
import random

def load_high_score():
    try:
        with open("/cybernaut/highscore.txt", "r") as file:
            return int(file.read())
    except:
        return None

def save_high_score(score):
    with open("/cybernaut/highscore.txt", "w") as file:
        file.write(str(score))

def main():
    print("🎯 Welcome to Number Guessing Game 🎯")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            high_score = load_high_score()
            if high_score is None or attempts < high_score:
                print("🎉 New High Score!")
                save_high_score(attempts)
            break

if __name__ == "__main__":
    main()
