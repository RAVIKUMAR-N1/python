income=int(input("enter your income:"))
if income<=10000:
    tax=0
elif 10000>income<=20000:
    tax=10000*0.10
else:
    tax=(10000*0.10)+((income-20000)*0.20)
print("tar for your income is",tax)
