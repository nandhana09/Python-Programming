import math
start=int(input("Start Number:"))
end=int(input("End number:"))
l=[]
for i in range(start,end+1):
  for j in str(i):
      if int(j)%2!=0:
        break
  else:
        s=math.sqrt(i)
        if(s%1==0):
          l.append(i)
print(l)
             
