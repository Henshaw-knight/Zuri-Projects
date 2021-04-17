import random
import sys
from datetime import datetime
from datetime import datetime
now = datetime.now()
date = now.strftime("%d-%B-%Y")
time = now.strftime("%X")

database = {9836068260: ["Henshaw", "Joseph", "josephhensh2000@gmail.com","1111", 5000]}
balance = 1000 #initial awarded cash for registering with the bank 

def init():
        
    print("Welcome to Hensh bank")

    have_account = int(input("Do you have an account with us: 1(yes) 2(no)\n"))
        
    if have_account == 1:                  
        login()
    elif have_account == 2:
        register()
    else:
        print("You have selected an invalid option")
        init()

def login():
    print("\n****** Login ******\n")
    account_number_from_user = input("What is your account number? \n")
    is_valid_account_number = account_number_validation(account_number_from_user)
    if is_valid_account_number:
        
        password = input("What is your password \n")

        for account_number, user_details in database.items():
            if(account_number == int(account_number_from_user)):
                 if(user_details[3] == password):
                     bank_operation(user_details)
                        

        print("Invalid account or password")
        login()
    else:
        init()

def register():
    print("\n***** Register ******\n")

    email = input("What is your email address? \n")
    if "@" and ".com" not in email:
        print("Enter a valid email address")
        register()
    else:
        pass
    
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself: \n")
    balance = 1000

    try:
        account_number = generate_account_number()
    except ValueError:
        print("Account generation failed due to internet connection failure")
        init()
            
    database[account_number] = [first_name, last_name, email, password, balance]
    
    
    
    print("\n== ==== ====== ==== ===")
    print(f"Your account number is: {account_number}")
    print("Make sure you keep it safe")
    print("== ==== ====== ==== ===\n")
    login()        

def account_number_validation(account_number):
    
    if account_number:
        if len(str(account_number)) == 10:
            try:
                int(account_number)
                return True 
            except ValueError:
                print("Invalid Account Number, Account Number should only be integer\n")
                return False
            except TypeError:
                return False
        else:
            print("Account Number cannot be more or less than 10.\n")
            return False           

    else:
        print("Account number is a required feature")
        return False 

def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))
    print("Entry time: ", date, time)   
    selected_option = int(input("\nWhat would you like to do? (1) deposit (2) withdrawal (3)Logout (4) Exit\n"))

    if selected_option == 1:
        deposit_operation(user)
    elif selected_option == 2:
        withdrawal_operation(user)
    elif selected_option == 3:
        logout()
    elif selected_option == 4:
        sys.exit()
    else:
        print("Invalid option selected")
        bank_operation(user)
    

def withdrawal_operation(user):
    print("Withdrawal")
    amount_to_withdraw = int(input('Enter the amount you want to withdraw: '))
    previous_balance = user[4]
    if previous_balance > amount_to_withdraw:
        recent_balance = previous_balance - amount_to_withdraw
        print(f"You have successfully withdrawn {amount_to_withdraw}")
        print(f"Your balance is now {recent_balance}")
    else:
        print("Insufficient balance, enter a lesser withdrawal amount")
           
    logout()
    

def deposit_operation(user):
    print("Deposit")
    deposited_cash = int(input("How much will you like to deposit: "))
    print(f"You just successfully deposited {deposited_cash}")
    previous_balance = get_current_balance(user)
    new_balance = previous_balance + deposited_cash
    print(f"Your balance is now {new_balance}")
    logout()
    
def generate_account_number():
    print("\nYour account has been created successfully")
    print("Thanks for registering with us\nHere are your account details: ")
    return random.randrange(1111111111, 9999999999)

def get_current_balance(user_details):
    return user_details[4]
 
 
def logout():
    logout_question = int(input("\nWould you like to continue?\n1.Yes\n2.No\n"))
    if logout_question == 1:
        login()   #would love to go back to bank_operations() after withdrawing or depositing but it's kinda difficult to implement
    else:
        print("Thanks for banking with us")
        sys.exit()    

init()    

