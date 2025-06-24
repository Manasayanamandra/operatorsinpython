'''Triangle Type Finder 
Take 3 side lengths and check 
1. All equal -->Equilateral
2. Any two equal -->Isosceles
3. Else -->Scalene'''
a = int(input("First side = "))
b = int(input("Second side = "))
c = int(input("Third side = "))
if a==b==c:
    print("Given Triangle is Equilateral Triangle")
elif a==b or b==a or c==a:
    print("Given triangle is Isosceles Triangle")
else:
    print("Given triangle is Scalene")