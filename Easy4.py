#Create a random password generator
#Allow the user to specify the amount of passwords to create
#Allow the user to specify the length of the string
import random
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']

# if no length is specified, choose a random length between 6 and 18 characters
# store this in an array of length 6-18
# for every element generate a random letter(or number?)


def generatePasswords(amount, length = None):
    pwordsGenerated = 0
    while pwordsGenerated < amount:
        if length is None:
            length = random.randrange(6,19)            
        password = ['']*length
        for i in range(len(password)):
            # generate random letter
            rand = random.randrange(0,25)
            password[i] = alphabet[rand]
        pwordsGenerated += 1
        print(''.join(password))
            
    
