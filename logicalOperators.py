'''
USED TO COMBINE LOGICAL STATEMENTS
| Operator | Meaning               | Example                |
| -------- | --------------------- | ---------------------- |
| `and`    | True if both are true | `True and True → True` |
| `or`     | True if one is true   | `True or False → True` |
| `not`    | Inverts result        | `not True → False`     |

'''
num = 20

if num > 0 and num%2==0:
    print("POstivie and even")
if num<0 or num%2 !=0:
    print("Negative and odd")  
if  not(num<0):
    print("Number is not negative") 