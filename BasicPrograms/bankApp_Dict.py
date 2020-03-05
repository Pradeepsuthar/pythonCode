ACINFO = {}

def add_ac():
    an = int(input("Enter account number : "))
    ahn = input("Enter account holder name : ")
    ab = float(input("Enter balance : "))
    pin = int(input("Enter Pin : "))
    # add into dict
    ACINFO[an] = [ahn, ab, pin]
    
def read_ac():
    print("\nA/C No.\t\tName\t\t\tCurrent Balance\t\tPin Code")
    for info in ACINFO:
        print("%d\t%s\t\t%0.2f\t\t\t%d"%(info,ACINFO[info][0],ACINFO[info][1],ACINFO[info][2]))
        
def withdraw(an, amt):
    if an in ACINFO:
        pn = int(input("Enter Pin : "))
        if ACINFO[an][1] >= amt and ACINFO[an][2] == pn:
            ACINFO[an][1] -= amt
            print("Current balance : %0.2f Rs."%ACINFO[an][1])
        else:
            print("Wrong pin or low balance...")
    else:
        print("Given ac no. is not valid..Try agian!!!")

# functions calling

for i in range(2):
    add_ac()
else:
    read_ac()


ac_no = int(input("Enter account no. : "))
w_bal = int(input("Enter withdraw amount : "))

withdraw(ac_no,w_bal)