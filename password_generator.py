import string
import random

def password_generator(min_length, special_characters="True", numbers="True"):
    digits = string.digits
    letters = string.ascii_letters
    special = string.punctuation

    characters = letters
    
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    password = " "
    correct_requirements = False
    number_present = False
    special_present = False

    while not correct_requirements or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            number_present = True
        elif new_char in special_characters:
            special_present = True

        
        correct_requirements = True
        if numbers:
            correct_requirements = number_present
        if special_characters:
            correct_requirements += correct_requirements + special_present
        
    return password


min_length  = int(input("Please enter a minumum length for your password: "))
number_present = input("Will your password have numbers? (y/n) ").lower() == "y"
special_present = input("Will your password have special characters? (y/n) ").lower() == "y"
password = password_generator(20, number_present, special_present)
print(password)
