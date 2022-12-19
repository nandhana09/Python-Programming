class Bank:
    def __init__(self,accno,name,acctyp,bal):
        self.accno=accno
        self.name=name
        self.acctyp=acctyp
        self.bal=bal
    def deposit(self):
        d=float(input("Enter the amount to be deposited"))
        self.bal=self.bal+d
       
    def withdraw(self):
        w=float(input("Enter the amount to be withdrawn"))
        if(self.bal>=w):
            self.bal=self.bal-w
            
        else:
            print("INSUFFICIENT BALANCE")
    def display(self):
        print("Acc Number:",self.accno)
        print("Name:",self.name)
        print("Acc Type:",self.acctyp)
        print("Balance=:",self.bal)
b1= Bank(10000203,"Nandhana","Savings",50000)
while(True):
    accno=int(input("Enter the account number"))
    print("1.WITHDRAW")
    print("2.DEPOSIT")
    n=int(input("Enter your choice"))
    if(n==1):
         
           b1.display()
           b1.withdraw()
    elif(n==2):
          b1.display()
          b1.deposit()
         
    else:
          printf("INVALID")
    
        
                

b1.display()
b1.deposit()
b1.display()
b1.withdraw()
b1.display()
        
