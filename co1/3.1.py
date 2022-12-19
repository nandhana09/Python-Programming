s=[x**2 for x in range(10)]
print("Square of numbers is",s)
x={x for x in 'python' if x in 'aeiou'}
print("Vowels in python are:",x)
p=[x for x in[-1,2,-3,0,4,8,9] if x>0]
print("Positive numbers are:",p)
o=[ord(x) for x in 'cat']
print("Ordinal values are",o)
