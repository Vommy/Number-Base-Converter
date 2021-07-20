def converterPage():
    import menu
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
    menu.menu()


