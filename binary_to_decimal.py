def binary_to_decimal(user_input_number):
    import menu
    # Check to see if the user's number is numeric
    if user_input_number.isnumeric():
        # Check to see if the user's number is a binary number
        binary_numbers = ["1", "0"]
        # Compare each number in the user's input and see if they are equal to either one or zero
        # Store a Boolean value inside the variable actual_binary_number
        # Stores True if all the booleans inside the previous value of actual_binary_number were True
        # Stores False otherwise
        actual_binary_number = [characters in binary_numbers for characters in user_input_number]
        actual_binary_number = all(actual_binary_number)
        # If the user did not enter a binary number, prompt them to enter a binary number
        # Then run the converter again.
        if not actual_binary_number:
            user_input_number = input("Please enter a valid binary number \n")
            binary_to_decimal(user_input_number)
        # If the user did enter a binary number, run the converter
        else:
            # Create a list variable named answer_decimal that will store our decimal number answer
            answer_decimal = []
            # Convert the user's input from a string into a list
            user_input_number = list(user_input_number)
            # for each element in the list user_input_number
            # Convert it to an integer
            for i in range(0, len(user_input_number), 1):
                user_input_number[i] = int(user_input_number[i])
            # Create a new list variable named position
            # Will store the values from 0 to the length of the user's input numbers, in increments of 1
            # We will use this list in our conversion
            # Reverse the position list so that the
            position = [*range(0, len(user_input_number), 1)]
            position.reverse()
            # For each bit in the user's binary number
            # Multiply the bit by 2 to the power of the "j"th element in the list position.
            # Append the answer to the list variable answer_decimal
            for j in range(0, len(user_input_number), 1):
                answer_decimal.append(user_input_number[j] * (2 ** position[j]))
            # Sum all the elements inside the answer_decimal list
            # Then print the sum as the answer.
            answer_decimal = sum(answer_decimal)
            print("Answer: \n" + str(answer_decimal))
            print("")

            # Define the exit loop code for the binary-decimal converter
            def exitLoop3():
                # Ask if the user would like to convert another binary number to decimal.
                answer = \
                    input("Would you like to convert another binary number to decimal? (Y/N) \n")
                # If the user presses "y" (Yes) on their keyboard,
                # Ask for another binary number to convert
                # Re-run the binary to decimal converter.
                if answer.upper() == "Y":
                    user_input_number = \
                        input("What binary number would you like to convert? \n")
                    binary_to_decimal(user_input_number)
                # If the user presses "n" (No) on their keyboard,
                # Ask if they would like to return to the main menu
                elif answer.upper() == "N":
                    answer = input("Would you like to return to the menu? (Y/N) \n")
                    # If the user presses "y" (Yes) on their keyboard,
                    # Return to the main menu
                    if answer.upper() == "Y":
                        menu.menu()
                    # If the user presses "n" (No) on their keyboard
                    # Thank them for using the number converter and exit the program.
                    elif answer.upper() == "N":
                        print("Thank you for using the number converter")
                        exit()
                    # If the press any other key, re run the exit loop
                    else:
                        exitLoop3()
                # If the press any other key, re run the exit loop
                else:
                    exitLoop3()
            # Call the exit loop function
            exitLoop3()
    # If the user's number is not numeric, ask them to enter a valid binary number
    # Then re-run the binary-decimal converter, using their answer as an argument.
    else:
        print("Please enter a valid binary number")
        user_input_number = input("What number would you like to convert? \n")
        binary_to_decimal(user_input_number)
