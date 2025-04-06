# get User Input

num = float(input("get first number"))
num2 = float(input("get second number"))

operator = input("Enter operator(+,-,*,/): ")

# perform operation
result = None

if operator == "+":
    result = num + num2
elif operator == "-":
    result = num - num2
elif operator == "*":
    result = num * num2
elif operator == "/":
    if num2 == 0:
        print("Error! Division by zero")
    else:
        result = num / num2
else:
    print("Error! Invalid operator")

    # print result
print(f"{num} {operator} {num2} = {result}")
