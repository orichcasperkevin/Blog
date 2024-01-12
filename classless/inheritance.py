from types import SimpleNamespace

def account(*,account_name, account_number, initial_balance=0):
    account_name = account_name
    account_number = account_number
    balance = initial_balance
    transactions = []

    def deposit(amount):        
        nonlocal balance
        if amount > 0:            
            balance += amount
            transactions.append(amount)
            return True
        else:
            print("Invalid deposit amount. Please enter a positive value.")
            return False

    def withdraw(amount):
        nonlocal balance
        if amount > 0 and amount <= balance:
            balance -= amount
            transactions.append(-abs(amount))
            return True
        else:
            print("Invalid withdrawal amount. Please enter a valid amount.")
            return False

    def get_transactions():
        return transactions

    def get_balance():
        return balance
    
    def set_balance(amount):        
        nonlocal balance 
        balance = amount

    def get_account_detail():
        return f"Acc. name: {account_name}\n Acc. No.: {account_number}"


    return SimpleNamespace(
        transactions=transactions,
        deposit=deposit,
        withdraw=withdraw,
        get_transactions=get_transactions,
        get_balance=get_balance,
        set_balance=set_balance,
        get_account_detail=get_account_detail
    )

def savings_goal_acount(*,account_name, account_number, goal_amount):
    parent = account
    child = parent(account_name=account_name,account_number=account_number)   
    goal_amount = goal_amount

    def withdraw(amount):        
        if child.get_balance() >= goal_amount:            
            child.set_balance(child.get_balance() - amount )            
            child.transactions.append(-abs(amount))            
            return True
        else:
            print("Invalid withdrawal amount or goal not reached.")
            return False

    child.withdraw = withdraw
    return child

# my_account = account(account_name="John Doe", account_number="123456", initial_balance=1000)
# # Deposit and Withdrawal
# my_account.deposit(500)
# my_account.withdraw(200)


# # Get Transactions and Balance
# print("Account Detail:\n", my_account.get_account_detail())
# print("Transactions:", my_account.get_transactions())
# print("Current Balance:", my_account.get_balance())

savings_account = savings_goal_acount(account_name="Savings", account_number="789012", goal_amount=5000)

# Deposit and Withdrawal (only allowed when the goal is reached)
savings_account.deposit(2000)
savings_account.deposit(3000)
print(savings_account.get_balance())
savings_account.withdraw(1000)  # This withdrawal is allowed
savings_account.withdraw(2000)  # This withdrawal is not allowed

# # Get Transactions and Balance
print("Account Detail:\n", savings_account.get_account_detail())
print("Transactions:", savings_account.get_transactions())
print("Current Balance:", savings_account.get_balance())