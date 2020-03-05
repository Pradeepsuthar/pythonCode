class Card:
    'to represent card info and operations'

    Card = input("Enter Something for Card : ")

    def __init__(self):
        'to initialize card info'
        self.CNo = int( input("Enter C No : "))
        self.CHName = input("Enter C H Name : ")
        self.CBalance = float( input("Enter C Balance : ") )
        self.CExDate = input("Enter C Ex Date : ")
    
    def getCardInfo(self):
        'to display card info'
        print("C No : %d" %self.CNo)
        print("C Name : %s" %self.CHName)
        print("C Balance : %0.2f Rs" %self.CBalance)
        print("C Ex Date : %s" %self.CExDate)
    
    def withdraw(self, amt):
        'to withdraw from account balance'
        if self.CBalance>=amt:
            self.CBalance-=amt
            print("Cur Card Bal(Withdraw): %0.2f Rs" %self.CBalance)
        else:
            print("Low Balance")
    
    def deposit(self, amt):
        'to deposit into balance'
        self.CBalance+=amt
        print("Cur Card Bal(Deposit): %0.2f Rs" %self.CBalance)

# inheriting into Derived class
class DebitCard(Card):
    'to describe/represent Debit Card Info and Operations'

    Msg = input("Enter Message : ")

    def __init__(self, pin):
        'to initialize Debit Info'
        # calling base class __init__
        Card.__init__(self)
        self.PIN = pin

    def getDebitInfo(self):
        'to display Debit Info'
        # calling base class withdraw
        Card.withdraw(self, 5000)
        self.getCardInfo()
        print("PIN : %d" %self.PIN)

    def withdraw(self, amt):
        'to withdraw from account balance'
        pin = int(input("Enter PIN : "))
        if self.CBalance>=amt and self.PIN==pin:
            self.CBalance-=amt
            print("Debit Bal (Withdraw): %0.2f Rs" %self.CBalance)
        else:
            print("Low Balance or Wrong PIN")
# functions
print( issubclass(DebitCard, Card) )
# creating instance
dc1 = DebitCard(2345)
print( isinstance(dc1, DebitCard))
dc1.getDebitInfo()
dc1.withdraw(10000)
dc1.deposit(20000)

