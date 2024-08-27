class BankAccount(object):
    ''' Doc '''
    def __init__(self, accountID="1001", balance=0):
        self.ID = accountID
        self.balance = balance
    def set_account_ID(self, newID):
        self.ID = newID
    def set_balance(self, new_balance):
        self.balance = new_balance
    def get_account_ID(self):
        res = self.ID
        return res
    def get_balance(self):
        temp1 = self.balance
        return temp1
    def deposit(self, amount):
        self.balance += float(amount)
    def withdrawal(self, amount):
        self.balance -= float(amount)
    def __str__(self):
        return f"ID: {self.ID}, Balance: {self.balance:.2f}"