class Budget:
    def __init__(self, category):
        """"Initialize attributes"""
        self.category = category
        self.fund = 10000  #a default fund is set

          
    def deposit(self):
        """amount to deposit into the category is requested"""
        amount_to_deposit = int(input("Enter the amount (in figures) you want to deposit: "))
        print(f"{amount_to_deposit} Naira has just been deposited into {self.category} category!")
        return amount_to_deposit  #the input entered is returned
    
    def withdraw(self):
        """amount to be withdrawn from the category is requested"""
        amount_to_withdraw = int(input("Enter the amount (in figures) you want to withdraw: "))
        print(f"{amount_to_withdraw} has just been withdrawn from {self.category} category!")
        return amount_to_withdraw  #the input entered is returned
    
    def deposit_balance(self):               
        print(f"Your fund is now {self.fund + deposit_statement} Naira") #this displays the balance after deposit is done 
    def withdrawal_balance(self):
        print(f"Your fund is now {self.fund - withdrawal_statement} Naira") #this displays the balance after withdrawal is done
        #if - sign shows, it indicates a deficit that is the user is owing.
        
    
    def transfer(self):
        """the receiving category is requested"""
        category2 = input("Which category do you want to transfer to?\n")
        try:
            balance_amount = int(input("How much would you like to transfer: "))
        except ValueError:
            print("Please, enter a valid amount.")
        else:    
            print(f"You successfully transferred {balance_amount} Naira to {category2} category!")           
     
      
    def first_question(self):
        try:
            question = int(input(f"\nHello! Welcome to {category.title()} category\nWhich of the following actions will you like to perform?\n1. Deposit and check balance\n2. Withdraw and check balance\n3. Make Transfer\n\n"))
        except ValueError:
            print("Enter a valid option 1 - 3")
        else:    
            return question
    
category = input("Hi, which category will you go for? (Enter in words): \n* Food\n* Clothing\n* Entertainment\n\n")
if category.title() == "Food":
    food = Budget("Food")  #first instance created
    firstQuestion = food.first_question()  #the method is called and the returned value is stored in a variable
    if firstQuestion == 1:
        deposit_statement = food.deposit() #the method is called and the returned value is stored in a variable
        food.deposit_balance() 
    elif firstQuestion == 2:
        withdrawal_statement = food.withdraw()
        food.withdrawal_balance()    
    elif firstQuestion == 3:
        food.transfer()
    else:
        print("invalid option inputted")
elif category.title() == "Clothing":    
    clothing = Budget("Clothing")   #second instance created
    firstQuestion = clothing.first_question()
    if firstQuestion == 1:
        deposit_statement = clothing.deposit()
        clothing.deposit_balance()
    elif firstQuestion == 2:
        withdrawal_statement = clothing.withdraw()
        clothing.withdrawal_balance()
    elif firstQuestion == 3:
        clothing.transfer()
    else:
        print("Invalid option inputted")
elif category.title() == "Entertainment":    
    entertainment = Budget("Entertainment")  #last instance created
    firstQuestion = entertainment.first_question()
    if firstQuestion == 1:
        deposit_statement = entertainment.deposit()
        entertainment.deposit_balance()
    elif firstQuestion == 2:
        withdrawal_statement = entertainment.withdraw()
        entertainment.withdrawal_balance()
    elif firstQuestion == 3:
        entertainment.transfer()
    else:
        print("Invalid option inputted")
         
else:
    print("Category not found")



                                             
       
