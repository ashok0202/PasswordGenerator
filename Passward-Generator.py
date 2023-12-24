import random
import string

def create_pw(pw_length):
    letters=string.ascii_letters
    digits=string.digits
    special_char=string.punctuation

    alpha=letters+digits+special_char
    passward=''.join(random.choice(alpha) for i in range(pw_length))
    return passward
def lengthcheck():
    while True:
        try:
            pw_length=int(input("Enter the desired length of the password: "))
            if(pw_length<=0):
                print("Please enter a pasitive length")
            else:
                return pw_length
        except ValueError:
            print("Invalid input, Please enter a valid number.")

def genpassword():
    print("Welcome to the Password Generator")
    len=lengthcheck()
    password=create_pw(len)
    print("Generated Password:",password)
genpassword()


   