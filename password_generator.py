import string
import random

def password_generator(min_length, special characters="True", numbers="True"):
    numbers = string.digits
    letters = string.ascii_letters
    special_characters = string.punctuation

    