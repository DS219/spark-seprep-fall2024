def name_meaning(name):
    if len(name) == 0:
        return None
    if 1 <= len(name) <= 5:
        return "Strong"
    if 6 <= len(name) <= 7:  
        return "Sophisticated"
    if len(name) > 7:
        return "Elegant"

user_name = input("Please enter your name: ")

meaning = name_meaning(user_name)

if meaning:
    print(f"The meaning of your name is: {meaning}")
else:
    print("You did not enter a valid name.")

