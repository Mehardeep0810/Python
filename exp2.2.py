def calculate_income_tax(income):
    tax = 0
    if income <= 300000:
        tax = 0
    elif income <= 700000:
        tax = (income - 300000) * 0.05
    elif income <= 1000000:
        tax = (income - 700000) * 0.10 + 20000
    elif income <= 1200000:
        tax = (income - 1000000) * 0.15 + 50000
    elif income <= 1500000:
        tax = (income - 1200000) * 0.20 + 80000
    else:
        tax = (income - 1500000) * 0.30 + 140000

    # Adding 4% cess on the calculated tax
    tax += tax * 0.04
    return tax

# Input the annual income
income = float(input("Enter your annual income: "))

# Calculate the tax
tax = calculate_income_tax(income)

# Print the result
print(f"The income tax for an annual income of ₹{income:.2f} is ₹{tax:.2f}")
