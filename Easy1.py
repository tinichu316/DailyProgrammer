#Ask the user name, age, and reddit username. Log the information to access later. Return the information as :
#your name is (blank), you are (blank) years old, and your username is (blank)

dataLog = {"Username" : ["Name", 18]}
form = False #whether or not the form has been completed properly

while form == False:
    thisUser = input("Please enter your Reddit username: ")
    thisAge = int(input("Please enter your Age: "))
    thisName = input("Please enter your Name: ")
    if thisUser in ["quit","exit","stop"]: 
        print("Program Terminated")
        exit()
    elif type(thisAge) is int and thisAge > 0:
        print("Your name is %s, you are %s years old, and your username is %s." 
              %(thisName, thisAge, thisUser))
        dataLog[thisUser] = [thisName, thisAge]
        form = True
    else:
        print("You have entered invalid information! \nTry again!")
