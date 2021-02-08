#Oop python- crete class

Class Account:
  def __init__(self,owner,balace=0)
   Self. Owner=owner
   Self. Balance=balance

  def __repr__(self):
   Return f"Account owner:{self.owner}, balance:{self.balance}"
  
  def deposit(self, dep_amt):
   Self. Balance=Self. Balance+dep_amt
   Print("deposit was accepted ") 

  def withdrawal(self, wd_amt):
     If self. Balance>=wd_amt:
       Self. Balance=Self. Balance-wd_amt
        Print("Withdrawal successful") 
     Else:
        Print (" Fund not available ") 

#initiate the class

Acct =Account ('jyoti', 200) 

#print the object
Print(Acct) 

#show the account owner attribute
Acc. Owner

#show the account balance attribute
Print (acc.balance) 

# make series of deposit And withdrawal
Acc. deposit (50) 
Acc. Withdrawal (75) 

# make a withdrawal that exceeds the available balance
Acc. Withdrawal (500) 

*********Output*********
Account owner: jyoti balance:200
Jyoti
200
Deposit was accepted
Withdrawal successful
Funds not available
