# Python program to demonstrate string functions


# Example string
example_string = "Hello World 123"

print("Original String:", example_string)

# upper() - Converts all characters to uppercase
upper_case = example_string.upper()
print("upper():", upper_case)

# lower() - Converts all characters to lowercase
lower_case = example_string.lower()
print("lower():", lower_case)

# isdigit() - Checks if the string contains only digits
digit_string = "12345"
print("isdigit() on '12345':", digit_string.isdigit())
print("isdigit() on 'Hello123':", example_string.isdigit())

# isalpha() - Checks if the string contains only alphabetic characters
alpha_string = "Hello"
print("isalpha() on 'Hello':", alpha_string.isalpha())
print("isalpha() on 'Hello123':", example_string.isalpha())

# split() - Splits the string into a list based on a delimiter (default is space)
split_string = example_string.split()
print("split():", split_string)

# join() - Joins elements of a list into a string with a specified delimiter
joined_string = "-".join(split_string)
print("join() with '-':", joined_string)

