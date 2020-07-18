# Find e to the Nth Digit

from math import e
from src.utils.get_number_input import get_number_input

# Get a number from user
num = get_number_input()

exp_val = round(e, num)
print(exp_val)
