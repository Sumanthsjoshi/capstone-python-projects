# coding: utf-8
# This program generates Fibonacci sequence of provided length


# Function to generate Fibonacci series
from src.utils.get_number_input import get_number_input


def gen_fibonacci(n):
    """
    This generator function returns the next value in a Fibonacci series
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b


# Get the number from user
num = get_number_input()

print("Generating a Fibonacci series upto {} values".format(num))

# Create a generator instance
get_next = gen_fibonacci(num)

# Print the generated series
print(list(get_next))
print("Fibonacci series created successfully!!")
