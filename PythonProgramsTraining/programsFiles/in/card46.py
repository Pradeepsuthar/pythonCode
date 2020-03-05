class Card:
    'to describe Card Details'

    Card = input("Enter Card Msg : ")

    def __init__(self):
        'to initialize card info'
        self.CNo = int(input("Enter Card No : "))
        self.CHName = input("Enter Card H Name : ")
        self.CBalance = float( input("Enter Card Balance : "))
        self.CExDate = input("Enter Card Ex Date : ")
    
    def getCardInfo(self):
        'to display card detail'
        print("C No : %d" %self.CNo)
        print("C H Name : %s" %self.CHName)
        print("C Balance : %0.2f Rs" %self.CBalance)
        print("C Ex Date : %s" %self.CExDate)
    
    def withdraw(self, amt):
        'to withdraw from account balance'
        if self.CBalance >= amt:
            self.CBalance -= amt
            print("Cur Card Bal : %0.2f Rs" %self.CBalance)
        else:
            print("Low Balance")

# inheriting into Derived Class
class CreditCard(Card):
    'to describe/represent credit card'

    Credit = input("Enter Credit msg : ")

    def __init__(self, cvv):
        'to initialize cvv'
        # calling base class init
        Card.__init__(self)
        self.CVV = cvv

    def getCreditInfo(self):
        'to display credit info'
        Card.withdraw(self, 5000)
        self.getCardInfo()
        print("CVV : %d" %self.CVV)

    def withdraw(self, amt):
        'to withdraw from Credit limit by CVV'
        cvv = int(input("Enter CVV : "))
        if self.CBalance >= amt and self.CVV == cvv:
            self.CBalance-=amt
            print("Cur Credit Balance : %0.2f Rs" %self.CBalance)
        else:
            print("Low Balance or Wrong CVV")
# functions
print( issubclass(CreditCard, Card) )
# creating an instance
cd1 = CreditCard(3035)
print( isinstance(cd1, CreditCard) )
# cd1.getCreditInfo()
# cd1.withdraw(10000)


