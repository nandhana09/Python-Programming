l=[]
oddl=[]
n=int(input("Enter the limit:"))
for i in range(n):
    num=int(input("Enter the number:"))
    l.append(num)
print("List:",l)
for i in l:
    if(i%2!=0):
        oddl.append(i)
print("List after removing even numbers:",oddl)
