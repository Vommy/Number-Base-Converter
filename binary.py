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
    user_choice = input()
    if user_choice.isnumeric():
        if int(user_choice) == 1 || int(user_choice) == 2:
            user_input_number = input("What number would you like to convert? \n")
            if(use_choirce == 1):
                binaryconverter(user_input_number)
            elif(user_choice == 2):
                 decimal_to_hexadecimal(user_input_number)s
        elif int(user_choice) == 3:
            print("Still working on it")
            menu()
            # Run binary to decimal converter
        elif int(user_choice) == 4:
            print("Still working on it")
            menu()
            # Run binary to hexadecimal
        elif int(user_choice) == 5:
            print("Still working on it")
            menu()
            # Run hexadecimal to decimal
        elif int(user_choice) == 6:
            print("Still working on it")
            menu()
            # Run hexadecimal to binary
        else:
            print("Please choose an option using the assigned keys.")
            menu()

    elif user_choice == "e" or user_choice == "E":
        print("Thank you for using the number converter")
        exit()

    else:
        print("Please choose an option using the assigned keys.")
        menu()

def binaryconverter(user_input_number):
    """
    This functions takes a user input number and converts it into it's equivalent binary number.
    FORMAT: binaryconverter(x)
    :param x: x = userinput number
    :return: binary equivalent
    """
    import math                                                                     #Importing Math module
    binary_num = []                                                                  #Creates a list variable named binary_num
    if user_input_number.isnumeric:
        user_input_number = int(user_input_number)
        res_of_div_2 = user_input_number                                                     #Holding the user's input number in a temporary variable
        res_of_div = math.floor(user_input_number/2)                                        #Divides the user's input number by 2 and then floors the result
        rem_of_div = res_of_div_2 % 2                                                         #Modulus operator used on the user's input number. Result is either 1 or 0
        binary_num.append(rem_of_div)                                                      #Appends the modulus operation result to the end of binary_num.
        while res_of_div >= 1:                                                           #Creates a While loop that will run until the variable "res_of_div" is less than 1.
            res_of_div_2 = res_of_div
            res_of_div = math.floor(res_of_div_2/2)
            rem_of_div = res_of_div_2 % 2
            binary_num.append(rem_of_div)
        else:                                                                           #Once the while loop finishes, print out the result.
            binary_num.reverse()
            print("Answer = {} " .format(binary_num), sep="")
            print("")
            def exitLoop():
                    answer = \
                        input("Would you like to convert another number to binary? (Y/N) \n")
                    if answer == "Y" or answer == "y":
                        user_input_number = \
                        input("What number would you like to convert? \n")
                        binaryconverter(user_input_number)
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


def binaryBreaker(binary_num):
    for i in range(0, len(binary_num), 4):
        yield binary_num[i:i + 4]

def decimal_to_hexadecimal(user_input_number):
    import math  # Importing Math module
    nibble_length = [0, 0, 0, 0]
    positional_list = [8, 4, 2, 1]
    conversion_answer = []
    binary_num = []  # Creates a list variable named binary_num
    if user_input_number.isnumeric:
        user_input_number = int(user_input_number)
        res_of_div_2 = user_input_number  # Holding the user's input number in a temporary variable
        res_of_div = math.floor(user_input_number / 2)  # Divides the user's input number by 2 and then floors the result
        rem_of_div = res_of_div_2 % 2  # Modulus operator used on the user's input number. Result is either 1 or 0
        binary_num.append(rem_of_div)  # Appends the modulus operation result to the end of binary_num.
        while res_of_div >= 1:  # Creates a While loop that will run until the variable "res_of_div" is less than 1.
            res_of_div_2 = res_of_div
            res_of_div = math.floor(res_of_div_2 / 2)
            rem_of_div = res_of_div_2 % 2
            binary_num.append(rem_of_div)
        else:  # Once the while loop finishes, separate the binary number list into lists of 4, then for each group of 4 bits, mathematically operate on each list, and then assign the result of the operation to the hexadecimal list.
            hexadecimalNum = list(binaryBreaker(binary_num)) #Separates the binary number into groups of 4.
            for i in range(0, len(hexadecimalNum), 1):
                temporarylist = hexadecimalNum[i]
                if len(hexadecimalNum[i]) < len(nibble_length):
                    while len(temporarylist) < len(nibble_length):
                        temporarylist.append(0)
                    hexadecimalNum[i] = temporarylist
            hexadecimalNum.reverse() #Reversing
            for i in range(0, len(hexadecimalNum), 1):
                temp_list = (hexadecimalNum[i])
                temp_list.reverse()
                hexadecimalNum[i] = list(temp_list)
            for i in range(0, len(hexadecimalNum), 1):
                empty_list =[]
                list_to_multiply = hexadecimalNum[i]
                for num1, num2 in zip(list_to_multiply, positional_list):
                    empty_list.append(num1 * num2)
                hexadecimalNum[i] = empty_list
            for i in range(0, len(hexadecimalNum), 1):
                if sum(hexadecimalNum[i]) <= 9:
                    conversion_answer.append(sum(hexadecimalNum[i]))
                else:
                    if sum(hexadecimalNum[i]) == 10:
                        conversion_answer.append("A")
                    elif sum(hexadecimalNum[i]) == 11:
                        conversion_answer.append("B")
                    elif sum(hexadecimalNum[i]) == 12:
                        conversion_answer.append("C")
                    elif sum(hexadecimalNum[i]) == 13:
                        conversion_answer.append("D")
                    elif sum(hexadecimalNum[i]) == 14:
                        conversion_answer.append("E")
                    else:
                        conversion_answer.append("F")
            print("Answer = ")
            print("0x", end='')
            print(*conversion_answer, sep="")


            def exitLoop():
                answer = \
                    input("Would you like to convert another number to hexadecimal? (Y/N) \n")
                if answer == "Y" or answer == "y":
                    user_input_number = \
                        input("What number would you like to convert? \n")
                    decimal_to_hexadecimal(user_input_number)
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
    import time
    print("Welcome to the number converter program! \n")
    time.sleep(2)
    print("In this program, "
          "you can convert any number between decimal, "
          "hexadecimal and binary \n")
    time.sleep(3)
    menu()


converterPage()


