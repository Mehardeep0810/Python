print(f"{'Decimal':<10} {'Hexadecimal':<15} {'Octal':<10} {'Binary':<10}")
print("-" * 45)

for i in range(1, 21):
    decimal = i
    hexadecimal = hex(i)[2:].upper()
    octal = oct(i)[2:]
    binary = bin(i)[2:]
    print(f"{decimal:<10} {hexadecimal:<15} {octal:<10} {binary:<10}")
