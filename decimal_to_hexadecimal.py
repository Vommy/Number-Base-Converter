def binaryBreaker(answer_binary):
    # Creating a function that will separate a binary number into nibbles.
    # for each element in the range from 0 to the length of the binary number in spaces of 4
    # separate them into lists of 4
    for i in range(0, len(answer_binary), 4):
        yield answer_binary[i:i + 4]

def decimal_to_hexadecimal(user_input_number):
    """
    This function takes the user's input of a decimal number and converts it into its hexadecimal equivalent
    FORMAT: decimal_to_hexadecimal(user_input_number)
    user_input_number == any decimal number
    """
    import menu
    # Importing the math module
    import math  # Importing Math module
    # Importing the time module
    # Creating a variable called nibble_length that will determine how long a nibble is (4 elements)
    nibble_length = [0, 0, 0, 0]
    # Creating a variable called positional_list.
    # This is the variable that we will use to multiply against our binary nibbles.
    positional_list = [8, 4, 2, 1]
    # Create a variable named answer_hexadecimal that will store our hexadecimal answer
    # Create a variable named answer_binary that will store our binary answer
    answer_hexadecimal = []
    answer_binary = []
    # Check to see if the user has input a numerical value.
    if user_input_number.isnumeric():
        # Convert it into an integer value
        user_input_number = int(user_input_number)
        # Store the user's input number into a temporary variable called res_of_div_2
        res_of_div_2 = user_input_number
        # Divide the user's input number by 2 and then floor the result
        res_of_div = math.floor(user_input_number / 2)
        # Modulus divide the user's input number by 2 and store it in a variable named rem_of_div
        # Then append the result into the variable answer_binary.
        rem_of_div = res_of_div_2 % 2
        answer_binary.append(rem_of_div)
        # While the variable res_of_div is above 1, keep floor dividing res_of_div by 2
        # And modulus dividing res_of_div by 2, and then append the answer to the answer_binary variable.
        while res_of_div >= 1:
            res_of_div_2 = res_of_div
            res_of_div = math.floor(res_of_div_2 / 2)
            rem_of_div = res_of_div_2 % 2
            answer_binary.append(rem_of_div)
        # Once the res_of_div variable is less than 1, run the else statement
        else:
            # Put our binary number into the binary_breaker function,
            # Make it a list,
            # Store it into the variable hexadecimalNum
            hexadecimalNum = list(binaryBreaker(answer_binary))
            for i in range(0, len(hexadecimalNum), 1):
                # Continuously assign the "i"th nibble in hexadecimalNum to a temporary list
                temporary_list = hexadecimalNum[i]
                # If the length of of the "i"th nibble is less than 4 (length of nibble)
                # While the length of that nibble is less than the length of 4
                # Append as many 0's needed to the end of the list to make it into a nibble of 4
                # Once the nibble is equal to the length of 4
                # Re-assign the new nibble in temporary list -
                # to the original "i"th element in the variable hexadecimalNum
                if len(hexadecimalNum[i]) < len(nibble_length):
                    while len(temporary_list) < len(nibble_length):
                        temporary_list.append(0)
                    hexadecimalNum[i] = temporary_list
            # Reverse the entire list of hexadecimalNum
            hexadecimalNum.reverse()
            # For each nibble in hexadecimal num in the "i"th position
            # Assign that nibble to the temp_list variable
            # Reverse that nibble so that the 1's and 0's are in the right position.
            # Re-assign the new reversed nibble back to the original "i"th position in hexadecimalNum
            for i in range(0, len(hexadecimalNum), 1):
                temp_list = (hexadecimalNum[i])
                temp_list.reverse()
                hexadecimalNum[i] = list(temp_list)

            for i in range(0, len(hexadecimalNum), 1):
                # Create an empty list variable to store the new hexadecimal value
                zero_to_eight_list =[]
                # For each nibble in hexadecimalNum
                # Assign the "i"th nibble in hexadecimalNum to the variable list_to_multiply
                list_to_multiply = hexadecimalNum[i]
                # For each bit in the list_to_multiply, multiply it by the corresponding number in positional_list
                for num1, num2 in zip(list_to_multiply, positional_list):
                    zero_to_eight_list.append(num1 * num2)
                # Each nibble will now have 4 numbers in each bit place, either; 0, 1, 2, 4 or 8
                # Re-assign the new list to the "i"th element in hexadecimalNum
                hexadecimalNum[i] = zero_to_eight_list

            # For each nibble in the variable hexadecimalNum
            for i in range(0, len(hexadecimalNum), 1):
                # If the sum of "i"th nibble is less than or equal to 9
                # Append the answer to the list variable answer_hexadecimal
                if sum(hexadecimalNum[i]) <= 9:
                    answer_hexadecimal.append(sum(hexadecimalNum[i]))
                # If the sum of the "i"th nibble is greater than 9
                # Run the else statement
                else:
                    # If the sum of the "i"th nibble is equal to 10,
                    # Append the string "A" to the list answer_hexadecimal
                    if sum(hexadecimalNum[i]) == 10:
                        answer_hexadecimal.append("A")
                    # If the sum of the "i"th nibble is equal to 11,
                    # Append the string "B" to the list answer_hexadecimal
                    elif sum(hexadecimalNum[i]) == 11:
                        answer_hexadecimal.append("B")
                    # If the sum of the "i"th nibble is equal to 12,
                    # Append the string "C" to the list answer_hexadecimal
                    elif sum(hexadecimalNum[i]) == 12:
                        answer_hexadecimal.append("C")
                    # If the sum of the "i"th nibble is equal to 13,
                    # Append the string "D" to the list answer_hexadecimal
                    elif sum(hexadecimalNum[i]) == 13:
                        answer_hexadecimal.append("D")
                    # If the sum of the "i"th nibble is equal to 14,
                    # Append the string "E" to the list answer_hexadecimal
                    elif sum(hexadecimalNum[i]) == 14:
                        answer_hexadecimal.append("E")
                    # If the sum of the "i"th nibble is equal to anything else (15 is the only other possible sum),
                    # Append the string "F" to the list answer_hexadecimal
                    else:
                        answer_hexadecimal.append("F")
            # Print the answer to the user
            print("Answer = ")
            print("0x", end='')
            print(*answer_hexadecimal, sep="")
            print("")

            # Define the exit loop for this function
            def exitLoop2():
                import time
                # Ask the user if they would like to convert another decimal number to hexadecimal
                answer = input("Would you like to convert another decimal number to hexadecimal? (Y/N) \n")
                # If the user presses "y" (Yes) on the keyboard,
                # Ask them for another decimal number to convert,
                # Then re-run the decimal-hexadecimal function
                if answer.upper() == "Y":
                    user_input_number = input("What number would you like to convert? \n")
                    decimal_to_hexadecimal(user_input_number)
                # If the user presses "n" (No) on the keyboard,
                # Ask if they would like to return to the main menu
                elif answer.upper() == "N":
                    answer = input("Would you like to return to the menu? (Y/N) \n")
                    # If the user presses "Y" (Yes) on the keyboard,
                    # Bring them back to the main menu
                    if answer.upper() == "Y":
                        menu.menu()
                    # If the user presses "N" (No) on the keyboard,
                    # Thank them for using the number converter,
                    # Close the program.
                    elif answer.upper() == "N":
                        print("Thank you for using the number converter")
                        time.sleep(2)
                        exit()
                    # If the user presses any other key, re run the exit loop.
                    else:
                        exitLoop2()
                # If the user presses any other key, re run the exit loop.
                else:
                    exitLoop2()
            # Call the exit loop function
            exitLoop2()

    # If the user enters a value that is not numeric,
    # Ask them to enter a valid decimal number
    # Re-run the decimal-hexadecimal converter, using their input as the argument.
    else:
        import time
        print("Please enter a valid decimal number")
        time.sleep(2)
        user_input_number = input("What number would you like to convert? \n")
        decimal_to_hexadecimal(user_input_number)