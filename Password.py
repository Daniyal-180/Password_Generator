import random
import string

length = int(input("Enter the length of a password: "))
print("Choose the number:\n1. Letters\n2. Digits\n3. Special Characters\n4. Exit")

characters = ""

while True:
    choice = int(input("Enter a choice:"))
    if choice == 1:
        characters += string.ascii_letters

    elif choice == 2:
        characters += string.digits

    elif choice == 3:
        characters += string.punctuation

    elif choice == 4:
        break

    else:
        print("Please enter a valid number")

password = []

if length >= 8:
    for i in range(length):
        random_char = random.choice(characters)
        password.append(random_char)
    print(f"The strong password is Successfully generated: {''.join(password)}")
else:
    for i in range(length):
        random_char = random.choice(characters)
        password.append(random_char)
    print(f"The weak password is Successfully generated: {''.join(password)}")