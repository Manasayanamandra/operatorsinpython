'''discount checker 
input purchase amount apply
1. 1000 --> 20% discount
2. 500 --> 10% 
3. --> No discount
'''
Amount = float(input("Enter Amount"))
if Amount>1000:
    discount = Amount *0.20
elif Amount>500:
    discout = Amount*0.10
else:
    discount =0
print("Discount =",discount)
print("Final Amount = ",Amount-discount)


