def menu():
    """
    Runs the menu for the converter program
    :return:
    """
    print("Choose which conversion you would like to perform:")
    print("""
       Press 1 to convert decimal to binary. \n 
       Press 2 to convert decimal to hexadecimal. \n
       Press 3 to convert binary to decimal. \n
       Press 4 to convert binary to hexadeimal. \n
       Press 5 to convert hexadecimal to decimal. \n
       Press 6 to convert hexadecimal to binary. \n
       Press E to exit \n
       """)
    userChoice = input()
    if userChoice.isnumeric():
        if int(userChoice) == 1:
            userInputNumber = input("What number would you like to convert? \n")
            binaryconverter(userInputNumber)
        elif int(userChoice) == 2:
            userInputNumber = input("What number would you like to convert? \n")
            decimalToHexadecimal(userInputNumber)
            # Run decimal to hexadecimal converter
        elif int(userChoice) == 3:
            print("Still working on it")
            menu()
            # Run binary to decimal converter
        elif int(userChoice) == 4:
            print("Still working on it")
            menu()
            # Run binary to hexadecimal
        elif int(userChoice) == 5:
            print("Still working on it")
            menu()
            # Run hexadecimal to decimal
        elif int(userChoice) == 6:
            print("Still working on it")
            menu()
            # Run hexadecimal to binary
        else:
            print("Please choose an option using the assigned keys.")
            menu()

    elif userChoice == "e" or userChoice == "E":
        print("Thank you for using the number converter")
        exit()

    else:
        print("Please choose an option using the assigned keys.")
        menu()

def binaryconverter(userInputNumber):
    """
    This functions takes a user input number and converts it into it's equivalent binary number.
    FORMAT: binaryconverter(x)
    :param x: x = userinput number
    :return: binary equivalent
    """
    import math                                                                     #Importing Math module
    binaryNum = []                                                                  #Creates a list variable named binarynum
    if userInputNumber.isnumeric:
        userInputNumber = int(userInputNumber)
        resofDiv2 = userInputNumber                                                     #Holding the user's input number in a temporary variable
        resOfDiv = math.floor(userInputNumber/2)                                        #Divides the user's input number by 2 and then floors the result
        remofDiv= resofDiv2 % 2                                                         #Modulus operator used on the user's input number. Result is either 1 or 0
        binaryNum.append(remofDiv)                                                      #Appends the modulus operation result to the end of binarynum.
        while  resOfDiv >= 1:                                                           #Creates a While loop that will run until the variable "resOfDiv" is less than 1.
            resofDiv2 =resOfDiv
            resOfDiv = math.floor(resofDiv2/2)
            remofDiv = resofDiv2 % 2
            binaryNum.append(remofDiv)
        else:                                                                           #Once the while loop finishes, print out the result.
            binaryNum.reverse()
            print("Answer = {} " .format(binaryNum), sep="")
            print("")
            def exitLoop():
                    answer = \
                        input("Would you like to convert another number to binary? (Y/N) \n")
                    if answer == "Y" or answer == "y":
                        userInputNumber = \
                        input("What number would you like to convert? \n")
                        binaryconverter(userInputNumber)
                    elif answer == "N" or answer == "n":
                        answer = input("Would you like to return to the menu? (Y/N) \n")
                        if answer == "Y" or answer == "y":
                            menu()
                        elif answer == "N" or answer == "n":
                            print("Thank you for using the number converter")
                            exit()
                        else:
                            menu()
                    else:
                        exitLoop()
            exitLoop()
    else:
        x = input("Please enter a valid number value")
        binaryconverter(x)


def binaryBreaker(lengthofbinarynum):
    for i in range(0, len(lengthofbinarynum), 4):
        yield lengthofbinarynum[i:i + 4]

def decimalToHexadecimal(userInputNumber):
    import math  # Importing Math module
    binaryNum = []  # Creates a list variable named binarynum
    if userInputNumber.isnumeric:
        userInputNumber = int(userInputNumber)
        resofDiv2 = userInputNumber  # Holding the user's input number in a temporary variable
        resOfDiv = math.floor(userInputNumber / 2)  # Divides the user's input number by 2 and then floors the result
        remofDiv = resofDiv2 % 2  # Modulus operator used on the user's input number. Result is either 1 or 0
        binaryNum.append(remofDiv)  # Appends the modulus operation result to the end of binarynum.
        while resOfDiv >= 1:  # Creates a While loop that will run until the variable "resOfDiv" is less than 1.
            resofDiv2 = resOfDiv
            resOfDiv = math.floor(resofDiv2 / 2)
            remofDiv = resofDiv2 % 2
            binaryNum.append(remofDiv)
        else:  # Once the while loop finishes, separate the binary number list into lists of 4, then for each group of 4 bits, mathematically operate on each list, and then assign the result of the operation to the hexadecimal list.
            hexadecimalNum = list(binaryBreaker(binaryNum)) #Separates the binary number into groups of 4.


            def exitLoop():
                answer = \
                    input("Would you like to convert another number to binary? (Y/N) \n")
                if answer == "Y" or answer == "y":
                    userInputNumber = \
                        input("What number would you like to convert? \n")
                    binaryconverter(userInputNumber)
                elif answer == "N" or answer == "n":
                    answer = input("Would you like to return to the menu? (Y/N) \n")
                    if answer == "Y" or answer == "y":
                        menu()
                    elif answer == "N" or answer == "n":
                        print("Thank you for using the number converter")
                        exit()
                    else:
                        menu()
                else:
                    exitLoop()

            exitLoop()


def converterPage():
    """
    Runs the introduction to the converter program
    :return:
    """
    userChoice = 0
    import time
    print("Welcome to the number converter program! \n")
    time.sleep(2)
    print("In this program, "
          "you can convert any number between decimal, "
          "hexadecimal and binary \n")
    time.sleep(3)
    menu()


converterPage()


