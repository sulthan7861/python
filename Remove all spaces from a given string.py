def remove_spaces(s):
    result = ""
    for char in s:
        if char != " ":
            result += char
    return result

# Example usage:
text = "Hello World From Python"
print(remove_spaces(text))  # Output: HelloWorldFromPython
