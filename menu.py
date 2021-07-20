def menu():
    import time
    import decimal_to_binary
    import binary_to_decimal
    import decimal_to_hexadecimal
    import binary_to_hexadecimal
    import hexadecimal_to_decimal
    import hexadecimal_to_binary

    """
    Runs the menu for the converter program
    :return:
    """
    print("Choose which conversion you would like to perform:")
    # Main Menu choices
    print("""
       Press 1 to convert decimal to binary. \n 
       Press 2 to convert decimal to hexadecimal. \n
       Press 3 to convert binary to decimal. \n
       Press 4 to convert binary to hexadecimal. \n
       Press 5 to convert hexadecimal to decimal. \n
       Press 6 to convert hexadecimal to binary. \n
       Press E to exit \n
       """)
    user_choice = input()
    # Check to see if the user's choice is numeric.
    # This would mean that the user may be trying to access one of the converters.
    if user_choice.isnumeric():
        # If the user presses 1, ask for a decimal number and convert it to binary
        if int(user_choice) == 1:
            user_input_number = input("What decimal number would you like to convert? \n")
            decimal_to_binary.binary_converter(user_input_number)
        # If the user presses 2, ask for a decimal number and convert it to hexadecimal
        elif int(user_choice) == 2:
            user_input_number = input("What decimal number would you like to convert? \n")
            decimal_to_hexadecimal.decimal_to_hexadecimal(user_input_number)
        # If the user presses 3, ask for a binary number and convert it to decimal
        elif int(user_choice) == 3:
            user_input_number = input("What binary number would you like to convert? \n")
            binary_to_decimal.binary_to_decimal(user_input_number)
        # If the user presses 4, ask for a binary number and convert it to hexadecimal
        elif int(user_choice) == 4:
            user_input_number = input("What binary number would you like to convert? \n")
            binary_to_hexadecimal.binary_to_hexadecimal(user_input_number)
        # If the user presses 5, ask for a hexadecimal number and convert it to decimal
        elif int(user_choice) == 5:
            user_input_number = input("What hexadecimal number would you like to convert? \n")
            hexadecimal_to_decimal.hexadecimal_to_decimal(user_input_number)
        # If the user presses 6, ask for a hexadecimal number and convert it to binary.
        elif int(user_choice) == 6:
            user_input_number = input("What hexadecimal number would you like to convert? \n")
            hexadecimal_to_binary.hexadecimal_to_binary(user_input_number)
        # If the user presses any other number, prompt them to enter a number key that has a function.
        else:
            print("Please choose an option using the assigned keys.")
            time.sleep(2)
            menu()

    # If the user presses "e" on the keyboard,
    # Thank them for using the number converter and exit the program.
    elif user_choice.upper() == "E":
        print("Thank you for using the number converter")
        time.sleep(2)
        exit()

    # If the user does not use one of the assigned keys
    # Prompt them to use one of the assigned keys.
    else:
        print("Please choose an option using the assigned keys.")
        time.sleep(2)
        menu()




