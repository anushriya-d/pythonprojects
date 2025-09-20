# This is a calculator program which is build using only conditional statments.

op = input("Enter the operator (+,-,*,%(for remainder),/):")

num1 = float(input("Enter the 1st number :"))
num2 = float(input("Enter the 2nd number :"))

if op == "+" :
    result = num1 + num2
    print(round(result,3))
elif op == "-" :
    result = num1 - num2
    print(round(result,3))
elif op == "*":
    result = num1 * num2
    print(round(result,3))
elif op == "%":
    result = num1 % num2
    print(round(result,3))
elif op == "/":
    result = num1 / num2
    print(round(result,3))
else:
    print (f"{op} is not valid operator.")