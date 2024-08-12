num=int(input("enter a number"))
sum=0
while num>0:
    r=num%10
    sum = sum*10 + r
    num=num//10
print("Reverse of",num,"is",sum)           
