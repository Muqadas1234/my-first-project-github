import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"\nYou rolled: {die1} and {die2}")
    print(f"Total: {die1 + die2}")

print("🎲 Welcome to the Dice Rolling Simulator! 🎲")

while True:
    roll = input("\nRoll the dice? (y/n): ").lower()
    if roll == 'y':
        roll_dice()
    elif roll == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Please enter 'y' or 'n'.")
