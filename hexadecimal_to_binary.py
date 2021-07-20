def hexadecimal_to_binary(user_input_number):
    import menu
    hex_0 = [0, 0, 0, 0]
    hex_1 = [0, 0, 0, 1]
    hex_2 = [0, 0, 1, 0]
    hex_3 = [0, 0, 1, 1]
    hex_4 = [0, 1, 0, 0]
    hex_5 = [0, 1, 0, 1]
    hex_6 = [0, 1, 1, 0]
    hex_7 = [0, 1, 1, 1]
    hex_8 = [1, 0, 0, 0]
    hex_9 = [1, 0, 0, 1]
    hex_A = [1, 0, 1, 0]
    hex_B = [1, 0, 1, 1]
    hex_C = [1, 1, 0, 0]
    hex_D = [1, 1, 0, 1]
    hex_E = [1, 1, 1, 0]
    hex_F = [1, 1, 1, 1]
    valid_hex_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    user_input_number = user_input_number.upper()
    binary_ans = []
    actual_hex_number = [characters in valid_hex_num for characters in user_input_number]
    actual_hex_number = all(actual_hex_number)
    if not actual_hex_number:
        user_input_number = input("Please enter a valid hexadecimal number \n")
        hexadecimal_to_binary(user_input_number)
    else:
        user_input_number = list(user_input_number)
        for i in range(0, len(user_input_number), 1):
            if (user_input_number[i] == "0") or (user_input_number[i] == "1") or (user_input_number[i] == "2") or (
                    user_input_number[i] == "3") \
                    or (user_input_number[i] == "4") or (user_input_number[i] == "5") or (user_input_number[i] == "6") \
                    or (user_input_number[i] == "7") or (user_input_number[i] == "8") or (user_input_number[i] == "9") \
                    or (user_input_number[i] == "A") or (user_input_number[i] == "B") or (user_input_number[i] == "C") \
                    or (user_input_number[i] == "D") \
                    or (user_input_number[i] == "E") or (user_input_number[i] == "F"):
                if user_input_number[i] == "0":
                    user_input_number[i] = hex_0
                elif user_input_number[i] == "1":
                    user_input_number[i] = hex_1
                elif user_input_number[i] == "2":
                    user_input_number[i] = hex_2
                elif user_input_number[i] == "3":
                    user_input_number[i] = hex_3
                elif user_input_number[i] == "4":
                    user_input_number[i] = hex_4
                elif user_input_number[i] == "5":
                    user_input_number[i] = hex_5
                elif user_input_number[i] == "6":
                    user_input_number[i] = hex_6
                elif user_input_number[i] == "7":
                    user_input_number[i] = hex_7
                elif user_input_number[i] == "8":
                    user_input_number[i] = hex_8
                elif user_input_number[i] == "9":
                    user_input_number[i] = hex_9
                elif user_input_number[i] == "A":
                    user_input_number[i] = hex_A
                elif user_input_number[i] == "B":
                    user_input_number[i] = hex_B
                elif user_input_number[i] == "C":
                    user_input_number[i] = hex_C
                elif user_input_number[i] == "D":
                    user_input_number[i] = hex_D
                elif user_input_number[i] == "E":
                    user_input_number[i] = hex_E
                else:
                    user_input_number[i] = hex_F
            else:
                print("Oops, an unexpected error occurred. \n "
                      "We're redirecting you back to the main menu.")
                menu.menu()
        for i in range(0, len(user_input_number), 1):
            for j in range(0, len(user_input_number[i]), 1):
                binary_ans.insert(0, user_input_number[i][j])
        binary_ans.reverse()
        print("Answer = \n ", end="")
        print(*binary_ans, sep="")
        print("")

        def exitLoop6():
            import time
            # Ask the user if they would like to convert another decimal number to hexadecimal
            answer = input("Would you like to convert another hexadecimal number to binary? (Y/N) \n")
            # If the user presses "y" (Yes) on the keyboard,
            # Ask them for another decimal number to convert,
            # Then re-run the decimal-hexadecimal function
            if answer.upper() == "Y":
                user_input_number = input("What number would you like to convert? \n")
                hexadecimal_to_binary(user_input_number)
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
                    exitLoop6()
            # If the user presses any other key, re run the exit loop.
            else:
                exitLoop6()

            # Call the exit loop function

        exitLoop6()
