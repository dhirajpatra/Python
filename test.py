#!/usr/bin/python

"""guess no programme
"""

def main():
    print "guess a number"
    randaomNumber = 30
    found = False       # flag variable
    
    # it will loop until found is true
    while not found:
        userNumber = input("Enter your guess: ")

        if userNumber == randaomNumber:
            print "you got it"
            found = True
        elif userNumber > randaomNumber:
            print "your guess is higher"
        else:
            print "you guess is lower"
        
if __name__ == "__main__":
    main()
