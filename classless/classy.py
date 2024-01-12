class Account:
    def __init__(self,account_name, account_number, initial_balance=0):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(amount)
            return True
        else:
            print("Invalid deposit amount. Please enter a positive value.")
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(-abs(amount))
            return True
        else:
            print("Invalid withdrawal amount. Please enter a valid amount.")
            return False

    def get_transactions(self):
        return self.transactions

    def get_balance(self):
        return self.balance


class SavingsGoalAccount(Account):
    def __init__(self, account_name, account_number, goal_amount):
        super().__init__(account_name, account_number)
        self.goal_amount = goal_amount

    def withdrawal(self, amount):
        if amount > 0 and amount <= self.balance and self.balance - amount >= self.goal_amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            return True
        else:
            print("Invalid withdrawal amount or goal not reached.")
            return False


# Example Usage:
# Create an instance of the Account class
my_account = Account(account_name="John Doe", account_number="123456", initial_balance=1000)

# Deposit and Withdrawal
my_account.deposit(500)
my_account.withdraw(200)


# Get Transactions and Balance
print("Account Name:", my_account.account_name)
print("Account Number:", my_account.account_number)
print("Transactions:", my_account.get_transactions())
print("Current Balance:", my_account.get_balance())

savings_account = SavingsGoalAccount(account_name="Savings", account_number="789012", goal_amount=5000)

# Deposit and Withdrawal (only allowed when the goal is reached)
savings_account.deposit(2000)
savings_account.deposit(3000)
savings_account.withdrawal(1000)  # This withdrawal is allowed
savings_account.withdrawal(2000)  # This withdrawal is not allowed

# Get Transactions and Balance
print("Account Name:", savings_account.account_name)
print("Account Number:", savings_account.account_number)
print("Transactions:", savings_account.get_transactions())
print("Current Balance:", savings_account.get_balance())
