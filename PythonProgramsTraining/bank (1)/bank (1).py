'to define functions to perform operations on account'
ACT=[5501, "Surbhi", 10500.50, 2323]

def withdraw(pin, amt):
    'to withdraw from account balance'
    if ACT[2]>=amt and ACT[3]==pin:
        ACT[2]-=amt
        print(ACT)
    else:
        print("Low Balance or Wrong PIN")

def deposit(pin, amt):
    'to deposit into account balance'
    if ACT[3] == pin:
        ACT[2] += amt
        print( ACT )
    else:
        print("Wrong PIN")