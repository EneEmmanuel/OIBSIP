# Password Generator - OIBSIP Task 3
# Author: Ene Emmanuel

import random
import string

print("--- PASSWORD GENERATOR ---")

length = int(input("Enter password length: "))

print("\nChoose what to include:")
use_letters = input("Include letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

characters = ""
if use_letters:
    characters += string.ascii_letters
if use_numbers:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

if characters == "":
    print("You must select at least one type!")
else:
    password = "".join(random.choice(characters) for _ in range(length))
    print(f"\nYour Generated Password is: {password}")
    print("\nThank you for using Password Generator!")
