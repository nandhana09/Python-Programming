s=input("Enter the string")
l=s.split()
n=len(l[0])
s=l[0]
for i in l:
    if len(i)>n:
     s=i
     l=len(i)
print("Longest word:",s)
print("Length:",len(s))
