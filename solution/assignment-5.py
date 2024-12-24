def is_palindrome_4(s):
    s = s.replace(" ", "").lower()
    stack = []

    # Push all characters onto the stack
    for char in s:
        stack.append(char)
    
    # Pop and compare with original string
    for char in s:
        if char != stack.pop():
            return False
    
    return True

# Example usage:
input_string = input("Enter a string: ")
if is_palindrome_4(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

