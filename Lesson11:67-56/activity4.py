num= int(input("Enter a number:"))
sum=0
a=num
while a>0:
    digit=a%10
    sum=sum+digit**3
    a=a//10
if sum==num:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")     