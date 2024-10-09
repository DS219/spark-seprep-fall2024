import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    print("Generating a random number between 1 and 100...")
    random_number = generate_random_number()
    print(f"Your random number is: {random_number}")

if __name__ == "__main__":
    main()


