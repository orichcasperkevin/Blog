def account(*,account_name, account_number, initial_balance=0):
    account_name = account_name
    account_number = account_number
    balance = initial_balance
    transactions = []

    
    def deposit(amount):        
        nonlocal balance
        if amount > 0:
            print(balance)
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

    def get_account_detail():
        return f"Acc. name: {account_name}\n Acc. No.: {account_number}"


    return {
        'deposit':deposit,
        'withdraw':withdraw,
        'get_transactions':get_transactions,
        'get_balance':get_balance,
        'get_account_detail':get_account_detail
    }


my_account = account(account_name="John Doe", account_number="123456", initial_balance=1000)
# Deposit and Withdrawal
my_account['deposit'](500)
my_account['withdraw'](200)


# Get Transactions and Balance
print("Account Detail:\n", my_account['get_account_detail']())
print("Transactions:", my_account['get_transactions']())
print("Current Balance:", my_account['get_balance']())