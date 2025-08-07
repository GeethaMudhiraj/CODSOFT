import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "You must select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("=== Password Generator ===")

try:
    length = int(input("Enter password length: "))
except ValueError:
    print("Invalid input. Length must be a number.")
    exit()

print("Include the following:")
use_upper = input("Uppercase letters? (y/n): ").lower() == "y"
use_lower = input("Lowercase letters? (y/n): ").lower() == "y"
use_digits = input("Numbers? (y/n): ").lower() == "y"
use_symbols = input("Special symbols? (y/n): ").lower() == "y"

password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
print("\nGenerated Password:", password)
