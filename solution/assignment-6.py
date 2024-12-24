def print_triangle_2(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")

        # Print numbers in the current row
        for j in range(1, 2 * i):
            print(j, end=" ")

        print()  # Move to the next line

# Example usage:
n = 4
print_triangle_2(n)

