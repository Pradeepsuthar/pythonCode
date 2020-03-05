class card:
    'to describe card details'
    def __init__(self):
        self.cno = int(input("Enter card number:- "))
        self.chname = input("Enter card holder name:- ")
        self.cbalance = int(input("Enter card balance:- "))
        self.cexdate = input("Enter card expiry date:- ")

    def getCardInfo(self):
        print("c no:- %d"%self.cno)
        print("c h name:- %s"%self.chname)
        print("c bal:- %0.2f"%self.cbalance)
        print("c ex date:- %s"%self.cexdate)

    def withdraw(self):
        amt = float(input("Enter amount:- "))
        if self.cbalance >= amt:
            self.cbalance -= amt
            print("cur card bal:- %0.2f Rs." %self.cbalance)
        else:
            print("Low balance")

#inheriting into derived class
class CreditCard(card):
    def __init__(self):
        card.__init__(self)
        self.CVV=int(input("Enter cvv:- "))
    def withdraw(self):
        cvv=int(input("Enter CVV:- "))
        if self.CVV==cvv:
            card.withdraw(self)
        else:
            print("Incorrect cvv")
    def getCreditInfo(self):
        self.getCardInfo()
        print("CVV:- %d"%self.CVV)

#creating an instance
cd1 = CreditCard()
cd1.getCreditInfo()
cd1.withdraw()
