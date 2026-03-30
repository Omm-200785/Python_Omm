a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

addition = a + b
subtraction = a - b
multiplication = a * b

if b != 0:
    division = a / b
    modulus = a % b
    floor_division = a // b
else:
    division = "Undefined (division by zero)"
    modulus = "Undefined (division by zero)"
    floor_division = "Undefined (division by zero)"

exponent = a ** b

print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Floor Division:", floor_division)
print("Exponent:", exponent)
