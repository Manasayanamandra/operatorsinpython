''' 
Calculator 
take 2 numbers and an operator (+,-,*,/) perform operation
use : if-elif, artgmetic operations, input
'''
a = float(input("Enter first number = "))
b = float(input("Enter second number = "))
operator = input("Enter operator")

if operator =='+':
    print("Addition",a+b)
if operator =='-':
    print("Subtraction",a-b)
if operator == '*':
    print("Multiplication",a*b)
if operator == '/':
    print("Division",a/b)
if operator == '//':
    print("Floor dividion operator",a//b)
if operator == '%':
    print("Modulo",a%b)
else:
    print("Invalid operator")