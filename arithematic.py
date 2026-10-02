# Taking numeric inputs from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Addition and Division
sum_result = num1 + num2
print(f"Sum: {num1} + {num2} = {sum_result}")

if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    div_result = num1 / num2
    print(f"Division: {num1} / {num2} = {div_result}")
