n=int(input("Enter the limit for fibonacci series"))
a=0
b=1
print(a)
for i in range (n-1):
    s=a+b
    print(s)
    a=b
    b=s
