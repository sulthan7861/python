# Check if a string is a palindrome
text = "madam"

# Method 1: Using slicing
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
