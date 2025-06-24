'''gradecalculator.py'''
'''maths = 100
physics = 95
aptitude = 100
total = maths+physics+aptitude
avg = total/3
if avg > 90:
    print("Grade A")
else:
    print("Grade B")'''

# program using logical operators 
telugu = int(input("telugu marks ="))
hindi = int(input("hindi marks ="))
english = int(input("English matks ="))
total = telugu+hindi+english
print("total marks = ",total)
avg = total/3
print("avg of 3 subjects =",avg)

if avg>=90 and avg<=100:
    print("Grade A")
elif avg >= 80 and avg<=90:
    print("Grade B")
elif avg >=70 and avg <=80:
    print("Grade c")
elif avg >=60 and avg <=70:
    print("Grade d")
elif avg >=50 and avg<=60:
    print("Grade e")
else:
    print("fail")
print(avg)


