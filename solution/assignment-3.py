def fibonacci_3(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
n = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence up to {n} terms: {list(fibonacci_3(n))}")

