import random

import string

def generate_password(length, use_letters, use_digits, use_symbols):

    # Define character sets based on user preferences

    characters = ''

    if use_letters:

        characters += string.ascii_letters

    if use_digits:

        characters += string.digits

    if use_symbols:

        characters += string.punctuation

    # Generate the password

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():

    print("Welcome to the Random Password Generator!")

    length = int(input("Enter the desired length of the password: "))

    use_letters = input("Include letters (y/n)? ").lower() == 'y'

    use_digits = input("Include digits (y/n)? ").lower() == 'y'

    use_symbols = input("Include symbols (y/n)? ").lower() == 'y'

    password = generate_password(length, use_letters, use_digits, use_symbols)

    print("Generated Password:", password)

if __name__ == '__main__':

    main()

