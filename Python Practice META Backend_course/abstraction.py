from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def calculate_interest(self):
        # TODO: Implement interest calculation for savings account
        pass

class CheckingAccount(BankAccount):
    def __init__(self, balance, overdraft_limit):
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def calculate_interest(self):
        # TODO: Implement interest calculation for checking account
        pass

# Create instances
savings = SavingsAccount(10000, 0.05)  # Example interest rate: 5%
checking = CheckingAccount(5000, 1000) # Example overdraft limit: 1000

# Print interest
print(f"Savings Account Interest: {savings.calculate_interest()}")
print(f"Checking Account Interest: {checking.calculate_interest()}")
