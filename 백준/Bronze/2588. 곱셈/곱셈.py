a = int(input())
b = int(input())
a_1= a%10
a_10= int((a%100)/10)
a_100= int(a/100)
b_1= b%10
b_10= int((b%100)/10)
b_100= int(b/100)

print(a*b_1)
print(a*b_10)
print(a*b_100)
print((a*b_1)+((a*b_10)*10)+((a*b_100)*100))