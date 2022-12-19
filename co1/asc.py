import operator
d={}
n=int(input("Enter the number of Entry :"))
for i in range(n):
    name=(input("Enter the name :"))
    roll=int(input("Enter the roll No :"))
    d[name]=roll
    print(d)
    sorted_d=sorted(d.items(),key=operator.itemgetter(0))
    sorted_d1=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print("The array sorted in ascening order",sorted_d)
print("The array sorted in descening order",sorted_d1)
