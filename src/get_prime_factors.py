# Prime Factorization

from src.utils.get_number_input import get_number_input

# Get a number from the user
inp_num = get_number_input()

# Initialize variables
prime_factors = []
all_factors = []

# Check if input number is 2
if inp_num == 2:
    all_factors.append(inp_num)
    prime_factors.append(inp_num)
else:
    # Find the prime factors of input number and append them to the
    # prime_factors list
    for n in range(2, inp_num + 1):
        # Check if n is a factor of input number
        if inp_num % n == 0:
            all_factors.append(n)
            is_prime = True
            # Check if n is a prime number
            for m in range(2, n):
                if n % m == 0:
                    is_prime = False
            if is_prime:
                prime_factors.append(n)
print("All the factors of {}: {}".format(inp_num, all_factors))
print("The prime factors of {}: {}".format(inp_num, prime_factors))
