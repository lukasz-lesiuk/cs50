import sys
from sys import argv
import string
import crypt


def main(argv):

    #check if correct number of arguments
    if len(argv) != 3:
        exit("Usage: python crack.py infile outfile error")
    #put password into variable
    key = argv[1]
    salt = argv[2]
    key_hashed = crypt.crypt(key, salt)
    print(key)
    print(key_hashed)

if __name__ == "__main__":
    main(argv)
