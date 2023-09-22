#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import string
import random

def generate_password(length, avoid_symbols, avoid_dangerous_symbols, avoid_numbers, avoid_lowercase, avoid_umlauts):
    characters = string.ascii_uppercase + string.ascii_uppercase

    if not avoid_symbols:
        characters += '@#%^*()_+-={}[]:;<>,.?~'
        # string.punctuation

    if not avoid_dangerous_symbols:
        characters += '$&|\'"`\!'

    if not avoid_numbers:
        characters += string.digits + string.digits

    if not avoid_lowercase:
        characters += string.ascii_lowercase + string.ascii_lowercase

    if not avoid_umlauts:
        characters += 'äöüßÁÉÍÓÚÑáéíóúñÇçØøÅåÐð'
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure password based on user input.")

    # Positional argument for length
    parser.add_argument('length', type=int, nargs='?', default=24, 
                        help="Specify the length of the password. Defaults to 24.")

    # Shorthand avoid flags
    parser.add_argument('-s', '--avoid-symbols', default=False, action='store_true', help="Avoid using symbols in the password.")
    parser.add_argument('-d', '--avoid-dangerous-symbols', default=False, action='store_true', help="Avoid using dangerous symbols in the password.")
    parser.add_argument('-n', '--avoid-numbers', default=False, action='store_true', help="Avoid using numbers in the password.")
    parser.add_argument('-l', '--avoid-lowercase', default=False, action='store_true', help="Avoid using lowercase letters in the password.")
    parser.add_argument('-u', '--avoid-umlauts', default=False, action='store_true', help="Avoid using umlauts letters in the password.")

    args = parser.parse_args()

    password = generate_password(args.length, args.avoid_symbols, args.avoid_dangerous_symbols, args.avoid_numbers, args.avoid_lowercase, args.avoid_umlauts)
    print(password)

if __name__ == '__main__':
    main()