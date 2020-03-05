# creating dict to store account detail
ACT = {}
for i in range(5):
    an = int(input("Enter Ac No : "))
    ahn = input("Enter Ac H Name : ")
    ab = float( input("Enter Ac Balance : ") )
    pin = int(input("Enter Ac PIN : "))
    # adding account info into dict
    ACT[an] = [ahn, ab, pin]
else:
    print( ACT )
# defining fun
def withdraw(an, amt):
    'to withdraw from account'
    if an in ACT:
        pn = int(input("Enter PIN : "))
        if ACT[an][1]>=amt and ACT[an][2]==pn:
            ACT[an][1] -= amt
            print("Bal : %0.2f Rs" %ACT[an][1])
        else:
            print("Wrong PIN or low balance")
    else:
        print("Ac No is not available")

def deposit(an, amt):
    'to deposit into account'
    if an in ACT:
        pn = int(input("Enter PIN : "))
        if ACT[an][2] == pn:
            ACT[an][1] += amt
            print("Bal : %0.2f Rs" %ACT[an][1])
        else:
            print("Wrong PIN")
    else:
        print("Given Ac No is not valid")
# calling
withdraw(1203, 2000)
withdraw(1206, 1000)
deposit(1202, 3000)
deposit(1207, 1000)
