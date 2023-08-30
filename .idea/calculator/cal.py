#calculator program


operation = input("choose operator.. (+,-,*,/ ):")

a= float(input("enter a value:"))

b=float(input("enter b value:"))


if operation == "+":

    result=a+b

    print("The sum is:", result)

elif operation == "-":

    result = a - b

    print("The subtraction is:", result)

elif operation == "*":

    result = a * b
    print("The multiplication is: " , result)

elif operation== "-":

    result = a / b

    print("The division is:",result)

else:

    print("invalid operation")