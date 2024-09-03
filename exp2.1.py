# Get the value of x and the number of terms
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))

# Initialize the sum
sum_series = 1.0

# Calculate the sum of the series
for i in range(1, n):
    sum_series += 1 / (x ** i)

# Print the result
print(f"The sum of the series is: {sum_series:.2f}")
