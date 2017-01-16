#write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.
#for extra credit, add a "decrypt" function to your program!

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']

#program cannot return upper or lower cases

def encode(word, shift):    
    listInput = list(word)
    
    for i in range(len(listInput)):
        if listInput[i].lower() in alphabet: #if it's not a number symbol, or whitespace
            a = alphabet.index(listInput[i].lower())
            if a <= shift: #checks if adding the rightward shift will go out of the list
                listInput[i] = alphabet[a + shift]
            else:
                listInput[i] = alphabet[a + shift - 26]
    print("Your encoded message is: %s" %"".join(listInput))    
    return "".join(listInput)

#decrypting function

def decode(codedWord, shift):
    listInput = list(codedWord)
    
    for i in range(len(listInput)):
        if listInput[i].lower() in alphabet:
            a = alphabet.index(listInput[i].lower())
            if a >= shift:
                listInput[i] = alphabet[a - shift]
            else:
                listInput[i] = alphabet[a - shift + 26]
    print("The original message is: %s" %"".join(listInput))    
    return "".join(listInput)        
            
        
        