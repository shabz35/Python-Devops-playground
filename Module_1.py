operation = input("please an operation (+ , -, /, x) :")
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

# Perform the requested operation
if operation == "+":
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "x":
    result = number_1 * number_2
elif operation == "/":
    result = number_1 / number_2

# Display the result
    print("Result:", result)