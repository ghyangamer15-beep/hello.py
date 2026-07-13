print("\n")
print("******Calculator by GP******")
print("\n")


num1 = float(input("Enter 1st number=="))
oprt = input("Enter the operator (+, -, *, /)==")
num2 = float(input("Enter 2nd number=="))

if oprt == "+":
    print("The sum is", num1 + num2)

elif oprt == "-":
    print("The difference is", num1 - num2)

elif oprt == "*":
    print("The product is", num1 * num2)

elif oprt == "/":
    if num2 == 0:
        print("Error: Division by zero")
    else:
        print("The quotient is", num1 / num2)
else:
    print("Unknown operator")