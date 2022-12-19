l=[]
n=int(input("Enter the number of elements:"))

for i in range(0,n):
    ele=(input("Enter the items in list:"))
    l.append(ele)
print(l)
print("First colour:",l[0])
print("Last colour:",l[n-1])
