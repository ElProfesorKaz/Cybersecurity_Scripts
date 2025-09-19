#!/usr/bin/env python3
"""
password_generator.py (Simplified)

Generates cryptographically secure passwords with minimal configuration.
By default, generates 16-character passwords using lowercase, uppercase,
numbers, and symbols — ensuring at least one of each.

Usage:
    python password_generator.py
    python password_generator.py --length 20
    python password_generator.py --count 5 --length 24

Author: ElProfesorKaz
License: MIT
"""

import argparse
import secrets
import string
import sys

SYMBOLS = '!@#$%^&*()-_=+[]{};:,.<>?'

def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    # At least one char from each set
    password_chars = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(SYMBOLS)
    ]

    # Fill the rest with a full alphabet
    alphabet = string.ascii_letters + string.digits + SYMBOLS
    password_chars += [secrets.choice(alphabet) for _ in range(length - 4)]

    # Shuffle to avoid predictable placement of character types
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Generate secure random passwords easily.")
    parser.add_argument('--length', '-l', type=int, default=16, help='Password length (default: 16)')
    parser.add_argument('--count', '-c', type=int, default=1, help='Number of passwords to generate (default: 1)')
    return parser.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)

    if args.length > 1024:
        print("Error: Maximum supported password length is 1024", file=sys.stderr)
        sys.exit(2)

    for i in range(args.count):
        pw = generate_password(args.length)
        if args.count == 1:
            print(pw)
        else:
            print(f"{i+1}: {pw}")

if __name__ == '__main__':
    main()
