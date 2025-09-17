class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        self.balance -= amount
        return self.balance


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate
        return self.balance


class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Exceeded overdraft limit")
        self.balance -= amount
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        if not isinstance(account, Account):
            raise ValueError("Must be an Account")
        self.accounts.append(account)

    def total_balance(self):
        return sum(account.balance for account in self.accounts)
