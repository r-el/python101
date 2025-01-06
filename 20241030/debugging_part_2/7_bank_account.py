def deposit(account, amount):
    account['balance'] += amount

def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds")
    else:
        account['balance'] -= amount

def get_balance(account):
    return account['balance']

def print_statement(account):
    print("Account balance:", get_balance(account)
    print("Transactions:")
    for transaction in account['transactions']:
        print(transaction)

account = {'balance': 100}
deposit(account, 50)
withdraw(account, 30)
withdraw(account, 200)
print_statement(account)