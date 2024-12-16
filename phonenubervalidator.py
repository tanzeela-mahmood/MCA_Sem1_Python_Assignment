import re

def validate_indian_mobile_number(number):
    # Regular expression for validating the format +91-XXXXXXXXXX
    pattern = r'^\+91-[6-9]\d{9}$'
    
    # Check if the number matches the pattern
    if re.match(pattern, number):
        return "Valid Indian mobile number"
    else:
        return "Invalid Indian mobile number"

# Test cases
test_numbers = [
    "+91-9876543210",  # Valid
    "+91-6123456789",  # Valid
    "+91-1234567890",  # Invalid (starts with 1)
    "9876543210",      # Invalid (missing +91-)
    "+91-98765432",    # Invalid (less than 10 digits)
    "+91-98765432101"  # Invalid (more than 10 digits)
]

# Check each test case
for number in test_numbers:
    print(f"{number}: {validate_indian_mobile_number(number)}")
