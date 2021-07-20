
def binary_to_hexadecimal(user_input_number):  # Fixed
    import menu  # Importing the menu module
    # Check to see if the user entered a number
    if user_input_number.isnumeric():
        # Check to see if the user entered a binary number
        binary_numbers = ["1", "0"]
        # Compare each number in the user's input and see if they are equal to either one or zero
        actual_binary_number = [characters in binary_numbers for characters in user_input_number]
        actual_binary_number = all(actual_binary_number)
        # If the user did not enter a binary number, prompt them to enter a binary number
        # Then run the converter again.
        if not actual_binary_number:
            user_input_number = input("Please enter a valid binary number \n")
            binary_to_hexadecimal(user_input_number)
        # If the user did enter a binary number, run the converter
        else:
            # Make the user's number into a list from a string
            user_input_number = list(user_input_number)
            # For every 1 or 0 in the list, convert them into an integer value
            for i in range(0, len(user_input_number), 1):
                user_input_number[i] = int(user_input_number[i])
            # Create a positional list for later use.
            # We will multiply this list against every nibble of the binary number
            positional_list = [8, 4, 2, 1]
            # Create a list to store our answer. This is where our hexadecimal answer will be stored.
            answer_hexadecimal = []
            # If the user's binary number can be evenly split into nibbles,
            # make each element of the list a list of 4 adjacent binary numbers (nibble)
            if len(user_input_number) % 4 == 0:
                for i in range(0, len(user_input_number), 4):
                    user_input_number[i] = user_input_number[i:i+4]
                user_input_number = user_input_number[::4]
            # If the user's binary number cannot be evenly split into nibbles,
            # Add zeros to the beginning of the list until the number can be evenly split into nibbles.
            else:
                while len(user_input_number) % 4 != 0:
                    user_input_number.insert(0, 0)
                for i in range(0, len(user_input_number), 4):
                    user_input_number[i] = user_input_number[i:i + 4]
                user_input_number = user_input_number[::4]
            # Create a list variable called hexadecimal_num that will store the value of the hexadecimal number
            hexadecimal_num = user_input_number
            for i in range(0, len(user_input_number), 1):
                # Create an empty list variable to store the new hexadecimal value
                zero_to_eight_list = []
                # For each nibble in hexadecimal_num
                # Assign the "i"th nibble in hexadecimal_num to the variable nibble_to_multiply
                nibble_to_multiply = hexadecimal_num[i]
                # For each bit in the nibble_to_multiply, multiply it by the corresponding number in positional_list
                for num1, num2 in zip(nibble_to_multiply, positional_list):
                    zero_to_eight_list.append(num1 * num2)
                # Each nibble will now have 4 numbers in each bit place, either; 0, 1, 2, 4 or 8
                # Re-assign the new list to the "i"th element in hexadecimal_num
                hexadecimal_num[i] = zero_to_eight_list
                # For each nibble in the variable hexadecimal_num, sum it.
            for i in range(0, len(hexadecimal_num), 1):
                # If the sum of "i"th nibble is less than or equal to 9
                # Append the answer to the list variable answer_hexadecimal
                if sum(hexadecimal_num[i]) <= 9:
                    answer_hexadecimal.append(sum(hexadecimal_num[i]))
                # If the sum of the "i"th nibble is greater than 9
                # Run the else statement
                else:
                    # If the sum of the "i"th nibble is equal to 10,
                    # Append the string "A" to the list answer_hexadecimal
                    if sum(hexadecimal_num[i]) == 10:
                        answer_hexadecimal.append("A")
                    # If the sum of the "i"th nibble is equal to 11,
                    # Append the string "B" to the list answer_hexadecimal
                    elif sum(hexadecimal_num[i]) == 11:
                        answer_hexadecimal.append("B")
                    # If the sum of the "i"th nibble is equal to 12,
                    # Append the string "C" to the list answer_hexadecimal
                    elif sum(hexadecimal_num[i]) == 12:
                        answer_hexadecimal.append("C")
                    # If the sum of the "i"th nibble is equal to 13,
                    # Append the string "D" to the list answer_hexadecimal
                    elif sum(hexadecimal_num[i]) == 13:
                        answer_hexadecimal.append("D")
                    # If the sum of the "i"th nibble is equal to 14,
                    # Append the string "E" to the list answer_hexadecimal
                    elif sum(hexadecimal_num[i]) == 14:
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
            def exitLoop4():
                import time
                # Ask the user if they would like to convert another decimal number to hexadecimal
                answer = input("Would you like to convert another decimal number to hexadecimal? (Y/N) \n")
                # If the user presses "y" (Yes) on the keyboard,
                # Ask them for another decimal number to convert,
                # Then re-run the decimal-hexadecimal function
                if answer.upper() == "Y":
                    user_input_number = input("What number would you like to convert? \n")
                    binary_to_hexadecimal(user_input_number)
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
                        exitLoop4()
                # If the user presses any other key, re run the exit loop.
                else:
                    exitLoop4()

            # Call the exit loop function
            exitLoop4()

    else:
        print("Please enter a valid binary number")
        user_input_number = input("What number would you like to convert? \n")
        binary_to_hexadecimal(user_input_number)





