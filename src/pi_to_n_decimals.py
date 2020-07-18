# Find the pi to Nth digit precision

from math import pi

from src.utils.get_number_input import get_number_input

# Get user input
n = get_number_input()

# print the pi to n digit precision
print(round(pi, n))
