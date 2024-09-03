def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is negative
if number < 0:
    print("Sorry, factorial does not exist for negative numbers.")
else:
    # Calculate the factorial
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")
