# creating dict to account detail
ACINFO = {}
def add_act_info():
    'to add new account info'
    an = int(input("Enter Ac No : "))
    ahn = input("Enter Ac Name : ")
    ab = float( input("Enter Ac Balance : ") )
    pin = int( input("Enter PIN : ") )
    # adding into dict
    ACINFO[an] = [ahn, ab, pin]

def read_act_info():
    'to read all account info'
    for info in ACINFO:
        print("%d\t%s\t%0.2f\t%d" \
        %(info, ACINFO[info][0], ACINFO[info][1],ACINFO[info][2]))

def withdraw(an, amt):
    'to withdraw from account'
    if an in ACINFO:
        pn = int(input("Enter PIN : "))
        if ACINFO[an][1]>=amt and ACINFO[an][2]==pn:
            ACINFO[an][1] -= amt
            print("Cur Bala : %0.2f Rs"%ACINFO[an][1])
        else:
            print("Wrong PIN or low Balance")
    else:
        print("Given Ac No is not valid")
        
def deposit(an, amt):
    'to deposit into account'
    if an in ACINFO:
        ACINFO[an][1]+=amt
        print("Cur Bal : %0.2f Rs" %ACINFO[an][1])
    else:
        print("Given Ac No is not valid")
# calling fun
for i in range(4):
    add_act_info()
else:
    read_act_info()
withdraw(5502, 3000)
deposit(5503, 2000)





