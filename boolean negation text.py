'''
Boolean nagation test 
take input True or False and print its opposite using not
'''
value = input("Given boolean function is = ")
if value =="True":
    print("Opposite is",not True)
elif value =="False":
    print("Opposite is",not False)
else:
    print("Invalid Input")
print(value)