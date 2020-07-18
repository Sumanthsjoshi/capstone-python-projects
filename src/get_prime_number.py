# This program prints next prime number until user chooses to stop
# Problem statement: Have the program find prime numbers until the user chooses
# to stop asking for the next one.


# Define a generator function
def get_prime():
    num = 3
    yield 2
    while True:
        is_prime = True
        for j in range(3, num, 2):
            if num % j == 0:
                is_prime = False
        if is_prime:
            yield num
        num += 2


# Initialize a generator instance
g = get_prime()

# Get the user input
while True:
    inp = input("Press enter to get next prime number(Enter any key to stop)")
    if not inp:
        print(next(g))
    else:
        print("Stopping the prime generator!!")
        break
