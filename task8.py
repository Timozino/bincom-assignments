import random


### Generate a random 4-digit number of 0s and 1s and convert to base 10
def generate_binary_and_convert():
    binary_number = ''.join(random.choice('01') for _ in range(4))
    decimal_number = int(binary_number, 2)
    return binary_number, decimal_number


binary, decimal = generate_binary_and_convert()
print(f"Generated binary: {binary}, Decimal: {decimal}")
