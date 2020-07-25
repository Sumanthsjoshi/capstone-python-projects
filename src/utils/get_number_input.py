# Utility to get a number input from user


def get_number_input(msg="Provide a number: ", num_type=int):
    """Utils function to get a number from user"""
    while True:
        try:
            num = num_type(input(msg))
        except ValueError:
            print(f"Whoops!! Please enter a correct number of {num_type}!!")
            continue
        else:
            print("Number accepted!!")
            return num
