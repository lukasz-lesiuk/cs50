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
    #get a salt
    salt = password[0] + password[1] # +'\0'

    for key in letters:
        print(key)
        key_hashed = crypt.crypt(key, salt)
        print(key_hashed)

        if password == key_hashed:
            print("PASSWORD FOUND")
            break


#        else:
#            for key_letter1 in letters:
#                for key_letter2 in letters:
#                    key = key_letter1 + key_letter2
#                    print(key)
#                    key_hashed = crypt.crypt(key, salt)
#                    print(key_hashed)
#                    compare(key, password)

    print(key)



if __name__ == "__main__":
    main(argv)
