def print_pattern_5(n):
    for i in range(1, n + 1):
        # Create the increasing sequence
        increasing = [chr(64 + j) for j in range(1, i + 1)]
        
        # Create the decreasing sequence
        decreasing = [chr(64 + j) for j in range(i - 1, 0, -1)]
        
        # Combine the increasing and decreasing parts
        row = increasing + decreasing
        
        # Print with leading spaces
        print(" " * (n - i) + " ".join(row))

# Example usage:
n = 3
print_pattern_5(n)

