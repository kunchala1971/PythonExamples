class BankAccount:
    def __init__(self, account_number,balance):
        self.account_number = str(account_number)
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient Funds")
    def deposit(self, amount):
        self.balance += amount


def transfer_amount(acc_1, acc_2, amount):
    try:
        acc_1.withdraw(amount)
        acc_2.deposit(amount)
        return True
    except ValueError as e:
        print(str(e))
        print(type(e))
        print(e.args)
        return False

user_1 = BankAccount("001",0)
user_2 = BankAccount("002",0)
user_1.deposit(int(input("Enter Account 1 Deposit Amount")))
user_2.deposit(int(input("Enter Account 2 Deposit Amount")))

print("User 1 Balance: {}/-".format(user_1.get_balance()))
print("User 2 Balance: {}/-".format(user_2.get_balance()))

transferAmount=int(input("Enter how much amount transfer to account 2"))
result=transfer_amount(user_1, user_2, transferAmount)
if result==True:
    print("Transferring " + str(transferAmount) + " /- from User 1 to User 2")
else:
    print("Amount Transfer Fail")

print("User 1 Balance: {}/-".format(user_1.get_balance()))
print("User 2 Balance: {}/-".format(user_2.get_balance()))