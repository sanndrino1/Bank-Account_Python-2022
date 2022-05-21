cpunt=0
user=[]
user_All_Holders=[]
Search_List=[]
withdrawl=0
deposit=0
balance=0
card_Holder=''
name=''
Pin=0
user_Account = [
    ['id',
 	'name',
    'deposit',
    'balance',
 	'withdrawl',
     'Customer_Card',
     'pin']
]
def entry_user_and_validation():
    id=input('Enter ID:')

    if  id.isdigit():
        print("ID!: Wellcome:!")
    else:
        print("ID is  not a digit!")

def user_validation():
    if len(id) == 10:
        print(" Your ID !:",id) 
    else:
        print("False Pin: Enter a Valid ID Cod Please !:") 

def name_user():
   
    name=(input('Enter Name:'))

def name_validation():
    for char in name:
        if((char>='a' and char<= 'z') or (char>='A' and char<='Z')):
            print(char, "is an Alphabet")
        else:
            print(char, "is not an Alphabet")
        
            print('Yuor Name:',name)
       
def Balance_user():
    balance=2000
def Deposit_User():
    balance=2000
    withdrawl=0
    deposit=float(input("Enter the amount to be deposit: "))
    balance = balance + deposit
    print ("The deposit is successful and the balance in the account is ",balance)
def Witdrawl_and_Validation_user(withdrawl):
    balance=2000
    withdrawl=float(input("Enter the amount to withdraw: "))
    if (balance >= withdrawl):
        balance = balance - withdrawl
        print ("The withdraw is successful and the balance is " ,balance)
    else:
        print ('Insuficient Balance')
def card_Holder_and_validation_user():
    card_Holder=input('Enter Card:')
    for char in card_Holder:
        if len(str(card_Holder)) > 4 or len(int(card_Holder)) >12:
            if  not (("A" <= char and char <= "Z")  or (char == " ")):
                print("INVALID CARD !:")
            break
        else:
                print("VALID CARD ")
def Pin_and_validation_user():
    Pin=input('Enter Pin:')

    if  Pin.isdigit():
        print("Pin!: Wellcome:!")
    else:
        print("Pin is  not a digit!")

    if len(Pin) == 4:
        print(" Your Pin !:",Pin) 
    else:
        print("False Pin: Enter a Valid Pin Cod Please !:") 
def User_Account_append():
    user_Account.append([id,name,balance,deposit,withdrawl,card_Holder,Pin])
    
    print(user_Account)
    if user_Account  and id and name and balance and deposit and withdrawl and card_Holder  and Pin in user_Account:
   # print ("That user already exsist",user_Account)
    #user.append(user_Account)
        print(user)
entry_user_and_validation() 
name_user()
Balance_user()
Deposit_User()
Witdrawl_and_Validation_user(0)
card_Holder_and_validation_user()
Pin_and_validation_user()
User_Account_append()

def Option_user():
    i=0                        
    option=int(input('enter Option:'))    
    for  i in range(0,2):
                  
        if option==1:
            print('Holders Account:',user_Account)
        break
    if option==2:
        print('Create New Account:')
                                              
Option_user()                                 
def Create_New_User_Account():
          
    while True:
        word=0
        if word==" ":
            break
        word=input('Enter Q for Create New Account: ' )
        id=input('Enter ID:')
        if  id.isdigit():
            print("Pin!: Wellcome:!")
        else:
            print("Pin is  not a digit!")

        if len(id) == 10:
            print(" Your Pin !:",id) 
        else:
            print("False Pin: Enter a Valid Pin Cod Please !:") 
            name=input('Enter Name:')
        for char in name:
            if((char>='a' and char<= 'z') or (char>='A' and char<='Z')):
                print(char, "is an Alphabet")
        else:
            print(char, "is not an Alphabet")
        
            print('Yuor Name:',name)

            balance=2000
            deposit=float(input("Enter the amount to be deposit: "))
            balance = balance + deposit
            print ("The deposit is successful and the balance in the account is ",balance)

            withdrawl=float(input("Enter the amount to withdraw: "))
        if (balance >= withdrawl):
            balance = balance - withdrawl
            print ("The withdraw is successful and the balance is " ,balance)
        else:
            print ('Insuficient Balance')

        card_Holder=input('Enter Card:')
        for char in card_Holder:
            if len(str(card_Holder)) > 4 or len(int(card_Holder)) >12:
                if  not (("A" <= char and char <= "Z")  or (char == " ")):
                    print("INVALID CARD !:")
                    break
                else:
                    print("VALID CARD ")

                    Pin=input('Enter Pin:')
                if  Pin.isdigit():
                        print("Pin!: Wellcome:!")
                else:
                        print("Pin is  not a digit!")

                if len(Pin) == 4:
                    print(" Your Pin !:",Pin) 
                else:
                    print("False Pin: Enter a Valid Pin Cod Please !:")
                    user.append([word,id,name, deposit,balance,withdrawl,card_Holder,Pin])
                    print(user)
                    
                    user_All_Holders.append(user)
                    print(user_All_Holders)
                    continue
        


def Option_User_Validation():
    n = int(input('Please enter the Holders of iterations:\n'))

    
    print('Enter 1 for choice 1 for Users: \n Enter 2 for choice 2 for Holder Withdrawl: \n,Enter 3 for choice Holder Balance:\n')
    
def Option_Choise():
    choice = int(input('Enter your choice:'))
    if (choice==0):
        print('Account Number:',user)
        choice = int(input('Enter your choice:'))
    if (choice == 1):
        deposit=0
        print('Holder Deposit:',deposit)
        print( ' Holders Deposit:\n If  Holders wont more Deposit Please pres 2')
        balance=0
        deposit=float(input("Enter the amount to be deposit: "))
        balance = balance + deposit
        print ("The deposit is successful and the balance in the account is ",balance)
    if (choice == 2):
        withdrawl=0
        print('Holder Withdrawl:',withdrawl)  
        withdrawl=float(input("Enter the amount to withdraw: "))
        withdrawl=0
        print(withdrawl)
        balance=0
        if (int(balance) >= float(withdrawl)):
            balance = int(balance) - float(withdrawl)
            print('Enter Withdrawl',withdrawl)
            print ("The withdraw is successful and the balance is " ,balance)
        else:
            print ('Insuficient Balance')  
            if (choice == 3):
                print('Holder Balance:',balance)
                if (choice == 4):
                    print(' All Bank Holders:', name)                      
                else:
                    print('Invalid choice:')
                    print(user_All_Holders)
Option_User_Validation()                  
Option_Choise()  
Create_New_User_Account()

