# coding: utf-8
# This program generates Fibonacci sequence of provided length


# Function to generate Fibonacci series
def gen_fibonacci(n):
    """
    This generator function returns the next value in a Fibonacci series
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b


# Get the number from user
while True:
    try:
        num = int(input("Please provide a number: "))
    except ValueError:
        print("Oops!! that's not a number.")
    else:
        print("Accepted!!")
        break

print("Generating a Fibonacci series upto {} values".format(num))

# Create a generator instance
get_next = gen_fibonacci(num)

# Print the generated series
print(list(get_next))
print("Fibonacci series created successfully!!")
