import json

# ანგარიშის ინფორმაციის შენახად ცარიელი სივრცე
accounts = {}

def create_account():
    account_number = input("enter account number: ")
    name = input("enter account holder name: ")
    balance = float(input("enter initial balance: "))
    accounts[account_number] = {
        'name': name,
        'balance': balance
    }
    print("account created successfully!\n")

def perform_transaction():
    account_number = input("enter account number: ")
    
    if account_number in accounts:
        print("account holder name:", accounts[account_number]['name'])
        print("current balance:", accounts[account_number]['balance'])
        
        choice = input("Enter 'd' for deposit, 'w' for withdrawal: ")
        
        if choice == 'd':
            amount = float(input("Enter deposit amount: "))
            accounts[account_number]['balance'] += amount
            print("deposit successful. updated balance:", accounts[account_number]['balance'])
        elif choice == 'w':
            amount = float(input("enter withdrawal amount: "))
            if amount <= accounts[account_number]['balance']:
                accounts[account_number]['balance'] -= amount
                print("withdrawal successful. updated balance:", accounts[account_number]['balance'])
            else:
                print("insufficient funds!")
        else:
            print("invalid choice. please enter 'd' for deposit or 'w' for withdrawal.")
    else:
        print("account not found!")

# Simple menu system
while True:
    print("\nMenu:")
    print("1. create account")
    print("2. perform transaction")
    print("3. exit")
    
    choice = input("enter your choice: ")
    
    if choice == '1':
        create_account()
    elif choice == '2':
        perform_transaction()
    elif choice == '3':
        print("exiting program. Thank you!")
        break
    else:
        print("invalid choice. please enter a valid option.")