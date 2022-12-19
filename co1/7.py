l1=[1,2,3,4,5]
l2=[3,4,5,6,7,8]
print(l1)
print(l2)
i1=len(l1)
i2=len(l2)
if(l1==l2):
 print("The length is same")
print("Length is not same")
s1=sum(l1)
s2=sum(l2)
print("Sum of elements in first list is",s1)
print("Sum of elements in second list is",s2)
t1=set(l1)
t2=set(l2)
t=t1.intersection(t2)
print("Common element in the list are:",t)
