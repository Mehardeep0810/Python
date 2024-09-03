# Function to validate PAN card number
def is_valid_pan(pan):
    return len(pan) == 10 and pan[:5].isalpha() and pan[5:9].isdigit() and pan[9].isalpha()

# Input user's name and PAN card number
name = input("Enter your name: ")
pan = input("Enter your PAN card number: ")

# Validate the inputs
if name.isalpha() and is_valid_pan(pan):
    print("\nDetails:")
    print(f"Name: {name}")
    print(f"PAN Card Number: {pan}")
else:
    print("\nInvalid input. Please ensure the name contains only letters and the PAN card number is in the correct format.")

# Example PAN format: ABCDE1234F
