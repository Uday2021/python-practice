# Task 1, 2, 3, 4
# Encapsulation

class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def deposite(self, amount):
        if(amount < 0):
            print("Invalid amount")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if (amount > self.__balance):
            print("insufficient balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
bank_account = BankAccount()
bank_account.deposite(1000)
bank_account.withdraw(500)
print(bank_account.get_balance())


# Mentor Challenge 1. -- > s object ke attribute dikahyega i.e "_Student__name"
# Mentor Challenge 2  -- > False, True


# Home work

# 1. public variable we can access publically from anywhere in that module or outside of that module after exporting.
# 2. protected variable is basically we will add one underscore to represent that variable internally like (_name), means we are not exposing the varable with same name adding _.
# 3. private variable we are representing using __name with two underscores and we cannot access outside of that class.
# 4. private me private is not actually private name mangling hoti h like we are storing with __{variableName} but behind the scene it is adding in _{className}__{varableName}.
    

        
