import sys
from sys import argv
import string
import crypt

#source: https://stackoverflow.com/questions/35328953/how-to-compare-individual-characters-in-two-strings-in-python-3
#def compare(key, password):
#    for x, y in zip(key, password):
#        if x == y:
#            print("PASSWORD FOUND")
#            print("key = ", key)
#            print("password = ", password)
#            sys.exit(0)

def main(argv):

    #check if correct number of arguments
    if len(argv) != 2:
        exit("Usage: python crack.py infile outfile error")
    #put password into variable
    password = argv[1]

    #get list of all relevant letters
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    letters = letters_lower + letters_upper
    print(letters)
    #get a salt
    salt = password[0] + password[1]

    #check all 1 letter passwords
    for key_letter1 in letters:
        key = key_letter1
        print(key)
        key_hashed = crypt.crypt(key, salt)
        if password == key_hashed:
            print("PASSWORD FOUND:", key)
            sys.exit(0)

    #check all 2 letter passwords
    for key_letter1 in letters:
        for key_letter2 in letters:
            key = key_letter1 + key_letter2
            print(key)
            key_hashed = crypt.crypt(key, salt)
            if password == key_hashed:
                print("PASSWORD FOUND:", key)
                sys.exit(0)

    #check all 3 letter passwords
    for key_letter1 in letters:
        for key_letter2 in letters:
            for key_letter3 in letters:
                key = key_letter1 + key_letter2 + key_letter3
                print(key)
                key_hashed = crypt.crypt(key, salt)
                if password == key_hashed:
                    print("PASSWORD FOUND:", key)
                    sys.exit(0)

    #check all 4 letter passwords
    for key_letter1 in letters:
        for key_letter2 in letters:
            for key_letter3 in letters:
                for key_letter4 in letters:
                    key = key_letter1 + key_letter2 + key_letter3 + key_letter4
                    print(key)
                    key_hashed = crypt.crypt(key, salt)
                    if password == key_hashed:
                        print("PASSWORD FOUND:", key)
                        sys.exit(0)

    #check all 5 letter passwords
        for key_letter1 in letters:
            for key_letter2 in letters:
                for key_letter3 in letters:
                    for key_letter4 in letters:
                        for key_letter5 in letters:
                            key = key_letter1 + key_letter2 + key_letter3 + key_letter4 + key_letter5
                            print(key)
                            key_hashed = crypt.crypt(key, salt)
                            if password == key_hashed:
                                print("PASSWORD FOUND:", key)
                                sys.exit(0)


if __name__ == "__main__":
    main(argv)
