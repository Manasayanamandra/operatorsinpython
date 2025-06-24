'''write a program to ask user for username and password if both 
match, show success'''

username = str(input("enter username"))
password = str(input("enter password"))
if username == "Manasa" and password == "Manasa@2001":
    print("Login Successful!")
else:
    print("Login Not successful!")
