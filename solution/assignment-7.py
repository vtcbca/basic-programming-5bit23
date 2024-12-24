def print_triangle_4(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(" ".join(str(x) for x in range(1, 2 * i)))
    
    # Print each row with appropriate leading spaces
    for i in range(n):
        print(" " * (n - i - 1) + numbers[i])

# Example usage:
n = 4
print_triangle_4(n)

