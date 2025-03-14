print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

option = int(input("Choose an operation: "))
result = 0

if option in [1, 2, 3, 4]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if option == 1:
        result = num1 + num2
    elif option == 2:
        result = num1 - num2
    elif option == 3:
        result = num1 * num2
    elif option == 4:
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed")
            exit()

    # Check if both numbers and the result are integers to display as int
    if num1.is_integer() and num2.is_integer() and result.is_integer():
        result = int(result)

    print("The result of the operation is: {}".format(result))

else:
    print("Invalid operation entered")

  