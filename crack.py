import sys
from sys import argv
import string
import crypt
from itertools import product


def main(argv):

    # check if correct number of arguments
    if len(argv) != 2:
        exit("Usage: python crack.py infile outfile error")
    # put password into variable
    password = argv[1]
    pass_len = 5

    # get list of all relevant letters
    letters = string.ascii_letters
    # get letterst as a list
    letters = list(letters)
    # print(letters)
    # get a salt
    salt = password[0] + password[1]

    # Get possible password check if it is correct and discard
    for i in range(pass_len):#
        for guess_list in list(product(letters, repeat=i)):
            guess = ""
            for j in range(i):
                guess = guess + guess_list[j]
            # print(guess)
            key_hashed = crypt.crypt(guess, salt)
            if password == key_hashed:
                print("PASSWORD FOUND:", guess)
                sys.exit(0)


if __name__ == "__main__":
    main(argv)
