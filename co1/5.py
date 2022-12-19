l=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    num=int(input("Enter the elements"))
    l.append(num)
print(l)
for i in range(len(l)):
    if(l[i]>100):
        l[i]="over"
print(l)
