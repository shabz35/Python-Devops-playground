file = open("calculations.txt", "r")

lines = file.read().splitlines()

total = 0

for expression in lines:
    parts = expression.split()
    operator = parts [1]
    number_1 = float(parts[2])
    number_2 = float(parts[3])

    if operator == "+":
        result = number_1 + number_2
    elif operator == "-":
        result = number_1 - number_2
    elif operator == "x":
        result = number_1 * number_2
    elif operator == "/":
        result = number_1 / number_2


    print(result)
    
    total += result