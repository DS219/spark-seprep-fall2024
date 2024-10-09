import random
import string

def generate_password(length=8):
    # Create a list of all letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters and join them into a password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Ask the user for the desired password length
length = int(input("Enter the length of the password: "))
print(f"Your random password is: {generate_password(length)}")
