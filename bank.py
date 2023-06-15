class Bank:
    Account=[]
    total_loan=0
    total_balance=50000000
    loan_system=True
    def __init__(self,name,email,password,money)-> None:
        self.name=name
        self.email=email
        self.password=password
        self.balance=money
        self.withdraw=0
        self.loan=0
        self.Account.append(name)
        self.transaction_history=[]
        Bank.total_balance+=money

    def Deposit(self,amount):
        if amount>0:
            self.balance+=amount
            Bank.total_balance+=amount
            print(f'total balance is {self.balance}')
            a=f'you have dposit {amount}'
            self.transaction_history.append(a)
        else:
            print("impossible")
    
    def Withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            Bank.total_balance-=amount
            print(f'take the money {amount} and your available balance is {self.balance-amount}')
            a=f'withdraw amount {amount}'
            self.transaction_history.append(a)
        else:
            print('bank is bankrupt')

    def Loan(self,amount):
        if Bank.loan_system==True:
            if(amount<=2*self.balance) and   Bank.total_balance>amount:
                self.loan+=amount
                Bank.total_loan+=amount
                Bank.total_balance-=amount
                print(f'take your money {amount} and your loan is {self.loan}')
                a=f'you have take a loan of amount {amount}'
                self.transaction_history.append(a)
            else:
                print ('no loan')
        else:
            print('loan system is off')
    
    def Transfer(self,amount,name,account):
        if name in self.Account:
            if amount <= self.balance:
                self.balance-=amount
                account.balance+=amount
                print(f'Your available balance is {self.balance}')
                a=f'you have tranfered {amount} to {name}'
                self.transaction_history.append(a)
            else:
                print('impossible')
        else:
            print('no account')

    def Total_loan(self):
        return Bank.total_loan
    
    def Total_balance(self):
        return Bank.total_balance
    
    def Loan_system(self,a):
        Bank.loan_system=a

    def show_loan(self,name,password):
        if name in self.Account and self.password==password:
            return self.loan
        else:
            return 'password or name does not match'
    def show_balance(self,name,password):
        if name in self.Account and self.password==password:
            return self.balance
        else:
            return 'password or name does not match'
    def Transaction_history(self):
        for i in self.transaction_history:
            print(i)
    def Total_account(self):
        print(len(Bank.Account))
        for i in Bank.Account:
            print(i)


class User(Bank):
    def __init__(self, name, email, password, money) -> None:
        super().__init__(name, email, password, money)  
    def Total_balance(self):
        return (f'You do not have access of it only Admin')
    def Total_loan(self):
        return (f'You do not have access of it only Admin')
    def Deposit(self, amount):
        return super().Deposit(amount)
    def Withdraw(self, amount):
        return super().Withdraw(amount)
    def Transfer(self, amount, name,account):
        return super().Transfer(amount, name,account)
    def Loan(self, amount):
        return super().Loan(amount)
    def show_balance(self, name, password):
        return super().show_balance(name, password)
    def show_loan(self, name, password):
        return super().show_loan(name, password)
    def Transaction_history(self):
        return super().Transaction_history()
    def Loan_system(self,a):
        print(f'you do not have the access of it only Admin can see it')
    def Total_account(self):
        print('you can not show that only Admin can see it')

class Admin(Bank):
    def __init__(self, name, email, password, money) -> None:
        super().__init__(name, email, password, money)
    def Total_balance(self):
        return super().Total_balance()
    def Total_loan(self):
        return super().Total_loan()
    def Loan_system(self,a):
        return super().Loan_system(a)




    
