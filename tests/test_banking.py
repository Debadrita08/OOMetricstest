import pytest
from banking import Account, SavingsAccount, CheckingAccount, Bank

def test_account_operations():
    acc = Account("Alice", 100)
    assert acc.deposit(50) == 150
    assert acc.withdraw(30) == 120
    with pytest.raises(ValueError):
        acc.withdraw(200)
    with pytest.raises(ValueError):
        acc.deposit(-10)

def test_savings_account():
    sa = SavingsAccount("Bob", 100, 0.1)
    assert sa.add_interest() == 110

def test_checking_account():
    ca = CheckingAccount("Charlie", 100, 200)
    assert ca.withdraw(250) == -150
    with pytest.raises(ValueError):
        ca.withdraw(400)  # exceeds overdraft limit

def test_bank_operations():
    bank = Bank()
    acc1 = Account("Alice", 100)
    sa = SavingsAccount("Bob", 200)
    ca = CheckingAccount("Charlie", 300)
    bank.add_account(acc1)
    bank.add_account(sa)
    bank.add_account(ca)
    assert bank.total_balance() == 600
    with pytest.raises(ValueError):
        bank.add_account("not an account")
