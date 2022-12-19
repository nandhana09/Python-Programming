l1=['red','blue','green','yellow']
l2=['red','blue']
print("list 1:",l1)
print("list 2:",l2)
s1=set(l1)
s2=set(l2)
print("Colours: ",s1.difference(s2))
