from bank_accounts import *

Shehan = BankAccount(2000, "Shehan")
John = BankAccount(1000, "John")

Shehan.getBalance()
John.getBalance()

# Shehan.deposit(500)

# John.withdraw(10000)

# Shehan.transfer(100000, John)

Paul = InterestRewards(1000, "Paul")

Paul.getBalance()
Paul.deposit(100)
Paul.transfer(100, Shehan)

Charith = SavingsAccount(1000, "Charith")

Charith.getBalance()
Charith.deposit(100)
Charith.transfer(10000, Shehan)
Charith.transfer(10, Shehan)