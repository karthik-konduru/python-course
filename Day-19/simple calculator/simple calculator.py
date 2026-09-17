import add,sub,multi,div

numbers = list(map(int, input("Enter numbers: ").split(",")))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(add.addition(numbers))

elif operation == "-":
    print(sub.subtraction(numbers))

elif operation == "*":
    print(multi.multiplication(numbers))

elif operation == "/":
    print(div.division(numbers))

else:
    print("Invalid operation")