class BankAccountApplication:
    def __init__(self):
        self.balance = 0

    def getData(self):
        for i in range(n):
            print("\nEnter details for new user %d." % (i+1))
            ac_no = int(input("Enter Mobile Number : "))
            a_h_name = input("Enter Account Holder Name : ")
            passcode = input(
                "Set your 4 digit passcode ( Don't share your passcode with anyone ) : ")

            while True:
                if (len(passcode) != 4):
                    passcode = input(
                        "Set your 4 digit passcode ( Don't share your passcode with anyone ) : ")
                else:
                    break

            bal = float(input(
                "Enter starting balance of this account ( Minimum balance is Rs.500.00/- ) : "))
            while bal <= 450:
                print(
                    "Minimum balance is required Rs.500.00/-\nPlease enter valid amount.")
                bal = float(input(
                    "Enter starting balance of this account ( Minimum balance is Rs.500.00/- ) : "))
                current_bal = '₹ {:,.2f}'.format(bal)


            print("\n:- %s's account is created successsfully." % (a_h_name))
            print("\n%s's Bank Account details :-\nAccount No. : 91%d \nIFSC Code : %s \nAvailable for Payment %s \nThanks"%(a_h_name, ac_no, ifsc, current_bal))

            info = [ac_no, a_h_name, passcode, current_bal]
            account.append(info)

        else:
            print("\nAll accounts are created successsfully")
            print(account)

            print("\n1. Deposit Money\t2. Withdraw Money")
            user_choice = int(input("Please enter your choice : "))
            if user_choice == 1:
                valid_ac_no = int(input("Enter Your Account Number : "))
                for item in account:
                    if (item[0] == valid_ac_no):
                        # print("Account found",account)
                        
                        deposit_amt = float(input(
                            "Enter Amount for Deposit ( Maximum deposit limit is Rs. 10,000.00/- ) : "))
                        if deposit_amt <= 10000:
                            objBankClass.deposit()
                            break
                        else:
                            print("Maximum deposit limit is Rs. 10,000.00/-")
                            break
                    else:
                        print("Account not found", type(item))
                        break
                
            elif user_choice == 2:
                valid_ac_no = int(input("Enter Your Account Number : "))
                for item in account:
                    if (item[0] == valid_ac_no):
                        # print("Account found",account)

                        deposit_amt = float(input("Enter Amount for withdraw ( Maximum deposit limit is Rs. 10,000.00/- ) : "))
                        if deposit_amt <= 10000:
                            objBankClass.withdraw()
                            break
                        else:
                            print("Maximum deposit limit is Rs. 10,000.00/-")
                            break
                    else:
                        print("Account not found", type(item))
                        break

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 


print("----------My Indian Payments Bank----------\n")
account = []
ifsc = "MYINDIANBANK081"
n = int(input("How many open accounts : "))

print("Enter bank details for creating account : ")

objBankClass = BankAccountApplication()

# Calling functions with that class object

objBankClass.getData()
