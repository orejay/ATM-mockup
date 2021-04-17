from datetime import date
today = date.today()
D1 = today.strftime("%B %d, %Y")
print(D1)
import random
database = {}
newdatabase = {}
def welcome():
    accountoptions = [1,2]
    print('welcome to Power Bank')
    accountstatus = int(input('Do you have an account with us? \n 1) Yes 2) No \n'))
    while (accountstatus not in accountoptions):
        print('Invalid option, Please try again')
        accountstatus = int(input('Do you have an account with us? \n 1) Yes 2) No \n'))
    if (accountstatus == 1):
        olddatabase()
        Transactionold()
    elif (accountstatus == 2):
        wantanaccount = int(input('would you like to create a Power Bank account? \n 1) Yes 2) No \n'))
        while (wantanaccount not in accountoptions):
            print('Invalid option, Please try again')
            wantanaccount = int(input('would you like to create a Power Bank account? \n 1) Yes 2) No \n'))
        if (wantanaccount == 1):
            register()
        elif (wantanaccount == 2):
            Transaction()
def register():
    print('*******SIGN UP HERE********')
    first_name = input('what is your first name? \n')
    last_name = input('what is your last name? \n')
    email = input('Enter your email address\n')
    password1 = input('create a secure password \n')
    password2 = input('confirm password \n')
    balance = 0
    if (password1 == password2):
        print('generating account number...' )
        accountnumber = accountnumbergenerator()
        print('Your account was created successfully...')
        print('YOUR ACCOUNT NUMBER IS : %d'% accountnumber)
        password = password2
        userdetails = [first_name, last_name, email, password, balance]
        database[accountnumber] = userdetails
        Transactionnew()
    else:
        print("passwords don't match, please try again")
        register()
def accountnumbergenerator():
    return random.randrange(0000000000,9999999999)
    print('your account number is:', accountnumbergenerator())
def olddatabase():
    #userdetails = [
    #database[accountnumber] = userdetails
    database[1023456789] = ['ore', 'jay', 'orejay@yahoo.com', 'funny', 25000000]
    database[1234567890] = ['metoy', 'ojo', 'metoy@yahoo.com', 'goat', 19000000]
def Transactionold():
    print('********LOGIN HERE********')
    olddatabase()
    Loginsuccessful = False
    while (Loginsuccessful == False):
        enteredaccountnumber = int(input('What is your account number? \n'))
        Password = input('What is your password \n')
        for accountnumber,userdetails in database.items():
            if (accountnumber == enteredaccountnumber):
                if (userdetails[3] == Password):
                    Loginsuccessful = True
    for accountnumber,userdetails in database.items():
        if (accountnumber == enteredaccountnumber):
            print('Welcome %s %s'% (userdetails[0],userdetails[1]))
    transactiontype1 = int(input('Please select an option below \n 1) Withdrawal  2)Deposit \n 3)Check balance  4)Complaint \n 5)Exit \n'))
    if (transactiontype1 == 1):
        Withdrawalold()
    elif (transactiontype1 == 2):
        Depositold()
    elif (transactiontype1 == 3):
        for accountnumber,userdetails in database.items():
            if (accountnumber == enteredaccountnumber):
                print('Your account balance is %d'% (userdetails[4]))
    elif (transactiontype1 == 4):
        input('What issue will you like to report? \n')
        print('Thank you for contacting us, your feedback helps us improve. We will work on your complaint.')
def Transactionnew():
    print('Login')
    Loginsuccessful = False
    while (Loginsuccessful == False):
        enteredaccountnumber = int(input('What is your account number? \n'))
        Password = input('What is your password \n')
        for accountnumber,userdetails in database.items():
            if (accountnumber == enteredaccountnumber):
                if (userdetails[3] == Password):
                    Loginsuccessful = True
    for accountnumber,userdetails in database.items():
        print('Welcome %s %s'% (userdetails[0],userdetails[1]))
    transactiontype = int(input('Please select an option below \n 1) Withdrawal  2)Deposit \n 3)Check balance  4)Complaint \n 5)Exit'))
    if (transactiontype == 1):
        Withdrawalnew()
    elif (transactiontype == 2):
        Depositnew()
    elif (transactiontype == 3):
        for accountnumber,userdetails in database.items():
            print('Your account balance is %d'% (userdetails[4]))
    elif (transactiontype == 4):
        input('What issue will you like to report? \n')
        print('Thank you for contacting us, your feedback helps us improve. We will work on your complaint.')
def Withdrawalold():
    totaloptionsW = [1,2,3,4,5,6]
    amountW = int(input('How much would you like to withdraw? \n 1)1000  2)2000 \n 3)5000  4)10000 \n 5)20000  6)others  \n'))
    while (amountW not in totaloptionsW):
        print('Invalid option, Please try again')
        amountW = int(input('How much would you like to withdraw? \n 1)1000  2)2000 \n 3)5000  4)10000 \n 5)20000  6)others  \n'))
    selectableamountswithdrawal = [1,2,3,4,5]
    if (amountW in selectableamountswithdrawal):
        olddatabase()
        for accountnumber,userdetails in database.items():
            if (accountnumber == enteredaccountnumber):
                Balance = userdetails[4]
        withdrawaloptions = [0, 1000, 2000, 5000, 10000, 20000]
        if (withdrawaloptions[amountW] < Balance):
            print('Please take your cash')
        elif (withdrawaloptions[amountW] > Balance):
            print('insufficient balance')
    elif (amountW == 6):
        otheramountW = int(input('input amount in multiples of 1000 not more than 80000 \n'))
        while (otheramountW > 80000):
            olddatabase()
            for accountnumber,userdetails in database.items():
                #if (accountnumber == enteredaccountnumber):
                Balance = userdetails[4]
                if (otheramountW > Balance):
                    print('insufficient balance')
                Withdrawalold()
            print('Please select an amount between 20000 and 80000')
            otheramountW = int(input('input amount in multiples of 1000 not more than 80000 \n'))
        if (otheramountW < 80000):
            print('Please take your cash')
    transactionoptions = [1,2]
    anothertransactionW = int(input('Would you like to perform another transaction? \n 1) Yes 2) No \n'))
    while (anothertransactionW not in transactionoptions):
        print('Invalid option, Please try again')
        anothertransactionW = int(input('Would you like to perform another transaction? \n 1) Yes 2) No \n'))
    if (anothertransactionW == 1):
            Transactionold()
    elif (anothertransactionW == 2):
            print('Please take your card')
            exit()
def Withdrawalnew():
    totaloptionsW = [1,2,3,4,5,6]
    amountW = int(input('How much would you like to withdraw? \n 1)1000  2)2000 \n 3)5000  4)10000 \n 5)20000  6)others  \n'))
    while (amountW not in totaloptionsW):
        print('Invalid option, Please try again')
        amountW = int(input('How much would you like to withdraw? \n 1)1000  2)2000 \n 3)5000  4)10000 \n 5)20000  6)others  \n'))
    selectableamountswithdrawal = [1,2,3,4,5]
    if (amountW in selectableamountswithdrawal):
        print('Please take your cash')
    elif (amountW == 6):
        otheramountW = int(input('input amount in multiples of 1000 not more than 80000 \n'))
        while (otheramountW > 80000):
            print('Please select an amount between 20000 and 80000')
            otheramountW = int(input('input amount in multiples of 1000 not more than 80000 \n'))
        if (otheramountW < 80000):
            print('Please take your cash')
    transactionoptions = [1,2]
    anothertransactionW = int(input('Would you like to perform another transaction? \n 1) Yes 2) No \n'))
    while (anothertransactionW not in transactionoptions):
        print('Invalid option, Please try again')
        anothertransactionW = int(input('Would you like to perform another transaction? \n 1) Yes 2) No \n'))
    if (anothertransactionW == 1):
            Transactionoldnew()
    elif (anothertransactionW == 2):
            print('Please take your card')
            exit()
def Depositold():
    totaloptionsD = [1,2,3,4,5,6]
    optionsD = [1,2]
    amountD = int(input('How much would you like to deposit? \n 1)1000  2)2000 \n 3)5000  4)10000 \n 5)20000  6)others  \n'))
    while (amountD not in totaloptionsD):
        print('Invalid option, Please try again')
        amountD = int(input('How much would you like to deposit? \n 1)1000  2)2000 \n 3)5000  4)10000 \n 5)20000  6)others  \n'))
    selectableamountsD = [1,2,3,4,5]
    if (amountD in selectableamountsD):
        print('Please submit your cash')
    elif (amountD == 6):
        otheramountD = int(input('input amount in multiples of 1000 not more than 80000 \n'))
        while (otheramountD not in range(80000)):
            print('Please select an amount between 20000 and 80000')
            otheramountD = int(input('input amount in multiples of 1000 not more than 80000 \n'))
        if (otheramountD in range(80000)):
            print('Please submit your cash')
    anothertransactionD = int(input('Would you like to perform another transaction? \n 1) Yes 2) No \n'))
    while (anothertransactionD not in optionsD):
        print('Please select a valid option')
        anothertransactionD = int(input('Would you like to perform another transaction? \n 1) Yes 2) No \n'))
    if (anothertransactionD == 1):
        Transactionold()
    elif (anothertransactionD == 2):
        print('Please take your card')
        exit()
def Depositnew():
    totaloptionsD = [1,2,3,4,5,6]
    optionsD = [1,2]
    amountD = int(input('How much would you like to deposit? \n 1)1000  2)2000 \n 3)5000  4)10000 \n 5)20000  6)others  \n'))
    while (amountD not in totaloptionsD):
        print('Invalid option, Please try again')
        amountD = int(input('How much would you like to deposit? \n 1)1000  2)2000 \n 3)5000  4)10000 \n 5)20000  6)others  \n'))
    selectableamountsD = [1,2,3,4,5]
    if (amountD in selectableamountsD):
        print('Please submit your cash')
    elif (amountD == 6):
        otheramountD = int(input('input amount in multiples of 1000 not more than 80000 \n'))
        while (otheramountD not in range(80000)):
            print('Please select an amount between 20000 and 80000')
            otheramountD = int(input('input amount in multiples of 1000 not more than 80000 \n'))
        if (otheramountD in range(80000)):
            print('Please submit your cash')
    anothertransactionD = int(input('Would you like to perform another transaction? \n 1) Yes 2) No \n'))
    while (anothertransactionD not in optionsD):
        print('Please select a valid option')
        anothertransactionD = int(input('Would you like to perform another transaction? \n 1) Yes 2) No \n'))
    if (anothertransactionD == 1):
        Transactionnew()
    elif (anothertransactionD == 2):
        print('Please take your card')
        exit()
def Transaction():
    allowedpins = [1991,1992,1993,1994,1995,1996,1997,1998,1999]
    PIN = int(input("Please type your pin \n"))
    pinowner = allowedpins.index(PIN)
    while(PIN not in allowedpins):
        print("incorrect pin, please try again")
        PIN = int(input("Please insert your card and input your pin \n"))
    balance = [100000,250004000,300000,20000,30000000,400000000,1000,590000000,25000]
    if (PIN in allowedpins):
        print("Please select an option below")
        serviceoption = int(input("1. WITHDRAWAL \n 2. DEPOSIT \n \n"))
    availableoptions = [1,2,3]
    while(serviceoption not in availableoptions):
        print("invalid option, please try again")
        serviceoption = int(input("1. WITHDRAWAL \n 2. DEPOSIT \n \n"))
    if (serviceoption == 1):
        withdrawalamount = int(input("How much would you like to withdraw? \n"))
        if (withdrawalamount > balance[pinowner]):
            print("insufficient balance")
            Transaction()
        print("take your cash")
    elif ( serviceoption == 2):
        pinowner = allowedpins.index(PIN)
        depositamount = int(input("How much would you like to deposit? \n"))
        Accountbalance = depositamount + balance[pinowner]
        print("********DEPOSIT SUCCESSFUL********")
        print("current balance is", Accountbalance)
welcome()
    
