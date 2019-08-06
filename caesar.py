# Encrypts messages using Caesar's cipher
import sys
from sys import argv
from cs50 import get_string


def main():
    # Signifies an error when user does not input two command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python caesar.py key")

    # Converts argv[1] to an integer and storing it to variable k
    key = int(sys.argv[1])

    # Signifies an error when user does not input a positive integer
    if key <= 0:
        sys.exit("Usage: python caesar.py key")

    # User inputs plaintext
    pt = get_string("plaintext: ")

    print("ciphertext: ", end="")

    # Encrypts message
    for c in pt:
        # Keep case of letter
        if c.isupper():
            cu = ord('A') + (ord(c) - ord('A') + key) % 26
            print(chr(cu), end="")

        elif c.islower():
            cl = ord('a') + (ord(c) - ord('a') + key) % 26
            print(chr(cl), end="")

        # Return unchanged
        else:
            print(c, end="")

    print()
    sys.exit(0)


# Executes main function
if __name__ == "__main__":
    main()