class Card:
    card = input("Enter card massage 1 : ")

    def __init__(self):
        self.CNo = int(input("Enter Card no. : "))
        self.CHName = input("Enter Card Holder Name : ")
        self.CBal = float(input("Enter Card Balance : "))
        self.ex_date = input("Enter Ex-Date : ")

    def getCardInfo(self):
        print("C No. : %d"%self.CNo)
        print("C H Name : %s"%self.CHName)
        print("C Bal : %0.2f"%self.CBal)
        print("C Ex-Date :  %s"%self.ex_date)

    def withdraw(self,amt):
        pin = int(input("Enter Pin : "))
        if self.CBal >= amt and self.PIN==pin:
            self.CBal-=amt
            print("Current Bal after withdraw : %0.2f Rs."%self.CBal)
        else:
            print("Low Bal (Krpiya Okaat me rhe Dhanywaad!)")

    def deposit(self,amt):
        self.CBal += amt
        print("Current Bal after Deposit : %0.2f Rs."%self.CBal)


class DebitCard(Card):
    msg = input("Enter messs 2")

    def __init__(self,pin):
        Card.__init__(self)
        self.PIN = pin

    def getDebitCardInfo(self):
        print("Your PIN is : %d"%self.PIN)

dc1 = DebitCard(1234)
dc1.getDebitCardInfo()
dc1.withdraw(10000)
dc1.deposit(500000)
