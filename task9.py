
###Sum the first 50 Fibonacci numbers

def sum_fibonacci(n):
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total


print(f"Sum of first 50 Fibonacci numbers: {sum_fibonacci(50)}")
