def reverse_string_5(s):
    stack = list(s)  # Convert string to list (stack)
    reversed_str = ''
    
    while stack:
        reversed_str += stack.pop()  # Pop elements from stack (LIFO)
    
    return reversed_str

# Example usage:
input_string = input("Enter a string: ")
print(f"Reversed string: {reverse_string_5(input_string)}")

