def binary_converter(user_input_number):
    """
    This functions takes a user input number and converts it into it's equivalent binary number.
    FORMAT: binary_converter(x)
    :param user_input_number:
    :return: binary equivalent
    """
    import menu

    # Importing Math Module
    import math
    # Creating a list variable that will store our binary number answer
    answer_binary = []
    # Checking to see if the user's input is a number
    if user_input_number.isnumeric():
        # Changing the user input into an integer value.
        user_input_number = int(user_input_number)
        # Assigning the res_of_div_2 (temporary variable) variable the value of user_input_number.
        res_of_div_2 = user_input_number
        # Dividing the user's input number by 2 and then flooring the result
        # Then storing the result of the division into a variable res_of_div for the next division.
        res_of_div = math.floor(user_input_number/2)
        # Modulus dividing the user's input number and then appending the result into the answer_binary variable
        rem_of_div = res_of_div_2 % 2
        answer_binary.append(rem_of_div)
        # While the variable res_of_div is above 1,
        # keep floor dividing res_of_div by 2
        # keep modulus dividing res_of_div by 2,
        # keep appending the answer to the answer_binary variable.
        while res_of_div >= 1:
            res_of_div_2 = res_of_div
            res_of_div = math.floor(res_of_div_2/2)
            rem_of_div = res_of_div_2 % 2
            answer_binary.append(rem_of_div)
        # Once the res_of_div variable is less than 1,
        # reverse the answer_binary list
        # And then print the answer.
        else:
            answer_binary.reverse()
            print("Answer = \n ", end="")
            print(*answer_binary, sep="")
            print("")

            # Defining the function that will allow the user to exit the program or convert more numbers
            def exitLoop1():
                # Ask the user if they would like to perform the same conversion for another number
                answer = input("Would you like to convert another decimal number to binary? (Y/N) \n")
                # If the user presses "y", ask them for a decimal number to
                # convert and then re-run the decimal-binary converter
                if answer.upper() == "Y":
                    user_input_number = input("What number would you like to convert? \n")
                    binary_converter(user_input_number)
                # If the user presses "N", ask if they would like to return to the main menu.
                elif answer.upper() == "N":
                    answer = input("Would you like to return to the menu? (Y/N) \n")
                    # If the user presses "y", run the menu() function
                    if answer.upper() == "Y":
                        menu.menu()
                    # If the user presses "n", thank them for using the converter and close the program.
                    elif answer.upper() == "N":
                        print("Thank you for using the number converter")
                        exit()
                    # If the user presses any other key, return them to the main menu.
                    else:
                        menu.menu()
                # If the user presses any other key, re-run this exit loop
                else:
                    exitLoop1()
            # Call the exit loop function within the decimal-binary converter
            exitLoop1()
    # If the user enters a value that is not a decimal number, ask them for a valid number.
    # Then, use their answer as the argument and re-run the decimal-binary converter.
    else:
        user_input_number = input("Please enter a valid decimal number value.")
        binary_converter(user_input_number)
