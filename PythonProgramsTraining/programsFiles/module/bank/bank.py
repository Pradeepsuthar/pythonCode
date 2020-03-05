'to define functions to perform bank operations'

ACT={"ANo":121001, "AcHName":"Jaiprakash", 
        "AcBal":35500.50,"PIN":4545}

print("Hello guys, we are using bank module")

def withdraw(pin, amt):
    'to withdraw from account balance'
    if ACT["PIN"] == pin and ACT["AcBal"]>=amt:
        ACT["AcBal"] -= amt
        print(ACT)
    else:
        print("Either wrong PIN or Low Balance")

def deposit(pin, amt):
    'to deposit into account balance'
    if ACT["PIN"] == pin:
        ACT["AcBal"] += amt
        print(ACT)
    else:
        print("Wrong PIN")


