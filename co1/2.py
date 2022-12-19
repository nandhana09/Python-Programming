cy=int(input("Enter the current year:"))
fy=int(input("Enter the final year:"))
print("The leap years are:")
while cy<fy:
    if(cy%4==0)and(cy%100!=0):
        print(cy)

    if(cy%100==0)and(cy%400==0):
        print(cy)
    cy=cy+1
    
