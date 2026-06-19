#                            CALCULATOR PROJECT
# Take inputs from the user
num1=float(input("Enter the value of number1:"))
num2=float(input("Enter the value of number2:"))
# Choose operator
print("Choose Operation:")
print("1.Addition Operator(+)")
print("2.Subtraction Operator(-)")
print("3.Multiplication Operator(*)")
print("4.Division Operator(/)")
# Take operator from the user
Choice=input("Enter the operation number: ")
# Logic of the calculator 
Operation={
    "1":num1+num2,
    "2":num1-num2,
    "3":num1*num2,
    "4":"Error: Due to undefined" if num2 == 0 else num1/num2
}
# Output
print(Operation.get(Choice,"Invalid Choice!"))