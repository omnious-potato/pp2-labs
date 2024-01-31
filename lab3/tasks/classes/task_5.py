class Account:
    def __init__(self):
        self.owner = input("Creating new account, owner:")
        self.balance = .0
        

    def deposit(self, deposit_amount):
        if(float(deposit_amount) < .0):
            print("Cannot deposit negative amount!")
        else:
            self.balance += float(deposit_amount)
            print(f"Succesfully deposited {deposit_amount}!")


    def withdraw(self, withdrawal_amount):
        if(float(withdrawal_amount ) < .0):
            print("Cannot withdraw negative amount!")          
        elif(self.balance - float(withdrawal_amount) < .0):
            print("Insufficient balance!")
        else:
            self.balance -= float(withdrawal_amount)
            print(f"Succesfully withdrawed {withdrawal_amount}!")



if __name__ == "__main__":
    print("This is demonstration of \"Account\" class, you can use following operations \n(entering corresponding character will result in desired action):\n")
    
    some_text = """ 
    (1) Create new account
    (2) List available accounts
    (3) Make a deposit
    (4) Commit withdrawal
    (Everything else) Terminate a program"""
    
    accounts = []
    
    while(True):
        print(some_text)
        op = input()
        match op:
            case "1":
                new_account = Account()
                accounts.append(new_account)
            case "2":
                for x in accounts:
                    print(f"Account of {x.owner}, balance: {x.balance}")
            case "3":
                owner = input("Enter name of account owner to deposit into: ")
                try: 
                    [x for x in accounts if x.owner == owner][0].deposit(input("Enter deposit amount: "))
                except IndexError:
                    print("Account not found!")
            case "4":
                owner = input("Enter name of account owner to withdraw from: ")
                try: 
                    [x for x in accounts if x.owner == owner][0].withdraw(input("Enter witdrawal amount: "))
                except IndexError:
                    print("Account not found!")
            case _:
                break


                
        
        

    
    