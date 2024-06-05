#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ATM():
    def __init__(self):
        self.pin= 1234
        self.balance=10000
        self.menu()
    def menu(self):
        print("""
            What would you like to do!
            1. Check Balance
            2. Withraw Balance
            3. Deposite Balance
            4. Exit
            """
             )
        option= int(input("Enter your option:"))
        if option== 1:
            self.check_balance()
            
        elif option== 2:
            self.withdraw_amount()
        elif option==3:
            self.deposit_amount()
        else:
            print("Thanks!!!")
    def check_balance(self):
        input_pin= int(input("Enter your Pin:"))
        if input_pin==self.pin:
            print("*"*20)
            print(f"Your Balance is: {self.balance}")
            print("*"*20)
        else:
            print("Enter Correct Pin")
        self.menu()    
    def withdraw_amount(self):
        input_pin= int(input("Enter your Pin:"))
        if input_pin== self.pin:
            input_balance= int(input("Enter your withdrawal amount:"))
            if input_balance<=self.balance:                
                self.balance= self.balance-input_balance
                print("*"*20)
                print(f"Remaining Amount{self.balance}")
                print("*"*20)
            else:
                print("Insufficient Balance")
        else:
            print("EnterCorrect Pin!")
        self.menu()    
    def deposit_amount(self):
        input_pin= int(input("Enter your Pin:"))
        if input_pin== self.pin:
            input_deposit= int(input("Enter your Deposit amount:"))                
            self.balance= self.balance+input_deposit
            print("*"*20)
            print(f"New Amount {self.balance}")
            print("*"*20)
        else:
            print("EnterCorrect Pin!")
    
            
SBI= ATM()


# In[ ]:





# In[ ]:




