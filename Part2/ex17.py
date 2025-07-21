import random

def generate_codename(name):
    adjectives = ['Noob', 'W', 'L', 'TRASH', 'none']
    animals = ['Dragon', 'Panther', 'Wolf', 'Phoenix', 'Tiger']
    secretstuff = ['Ur Gay', 'Ur Broke', 'Ur Mom likes tea']
    return f"{random.choice(adjectives)} {random.choice(animals)} — {random.choice(secretstuff)}"

def generate_lucky_number():
    return random.randint(0, 101)

def generate_lucky_day():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return random.choice(days)

def main():
    name = input("What is your name?\n")
    codename = generate_codename(name)
    lucky_number = generate_lucky_number()
    lucky_day = generate_lucky_day()

    print(f"\nHey {name}, here's your destiny report 🧙‍♂️")
    print(f"Codename: {codename}")
    print(f"Lucky Number: {lucky_number}")
    print(f"Lucky Day: {lucky_day}")

if __name__ == "__main__":
    main()
