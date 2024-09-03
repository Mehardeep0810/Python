# Input the string and the character to search for
input_string = input("Enter the string: ")
char_to_find = input("Enter the character to find: ")

# Initialize a flag to indicate if the character is found
found = False

# Iterate through the string to find the character
for index in range(len(input_string)):
    if input_string[index] == char_to_find:
        print(f"The character '{char_to_find}' is present at index {index}.")
        found = True
        break

# If the character is not found, print a message
if not found:
    print(f"The character '{char_to_find}' is not present in the string.")
