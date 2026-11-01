# Basic Calculator

num_1 = float(input("Enter your Number 1:"))
num_2 = float(input("Enter your Number 2:"))
oper = input("Enter your operator (+, -, *, /, **, %):")
sum = num_1 + num_2
sub = num_1 - num_2
mul = num_1 * num_2
div = num_1 / num_2
power = num_1 ** num_2
rem = num_1 % num_2

if oper == "+":
    print(f"The addition of two number is {sum}")
elif oper == "-":
    print(f"The substration of two number is {sub}")
elif oper == "*":
    print(f"The multiplication of two number is {mul}")
elif oper == "/":
    print(f"The division of two number is {div}")
elif oper == "**":
    print(f"The {num_1} raise to the {num_2} is {power}")
elif oper == "%":
    print(f"The remainder is {rem}")
else:
    print("Please ! Enter the proper opertor")