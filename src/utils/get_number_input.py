# Utility to get a number input from user


def get_number_input():
    """Utils function to get a number from user"""
    while True:
        try:
            num = int(input("Provide a number: "))
        except ValueError:
            print("Whoops!! That's not a number!!")
            continue
        else:
            print("Number accepted!!")
            return num
