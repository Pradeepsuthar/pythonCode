class Account:
    'to define account class with account info and operations'

    # creating static/class variables
    BankName = "HDFC Bank"

    def __init__(self):
        'to initialize instance variables'
        Account.AcStarter += 1
        self.AcNo = Account.AcStarter
        self.AcHName = input("Enter Ac H Name : ")
        self.AcBalance = float( input("Enter Ac Balance : ") )

    def setAcInfo(self):
        'to initialize account info'
        # declaring/creating instance variables
        self.AcNo = int( input("Enter Ac No : ") )
        self.AcHName = input("Enter Ac H Name : ")
        self.AcBalance = float( input("Enter Ac Balance : ") )
    
    def getAcInfo(self):
        'to display account detail'
        print("- - Account Detail - -")
        print("Ac No : %d" %self.AcNo)
        print("Ac H Name : %s" %self.AcHName)
        print("Ac Balance : %0.2f Rs" %self.AcBalance)
        print("Bank Name : %s" %Account.BankName )

    def withdraw(self, amt):
        'to withdraw from account balance'
        if self.AcBalance >= amt:
            self.AcBalance -= amt
            print("Balance after withdraw : %0.2f Rs" %self.AcBalance)
        else:
            print("Low Balance")

    @staticmethod
    def setBankInfo():
        'to set bank detail'
        Account.BankName = input("Enter Bank Name : ")
        # creating new static variable
        Account.AcStarter = int( input("Account Start No : ") )
        print("Bank Name : %s" %Account.BankName)
        print("Ac Starter : %d" %Account.AcStarter)

    @classmethod
    def setBankDetail(cls, bn, start):
        'to initialize variables by args'
        cls.BankName = bn
        Account.AcStarter = start
        print("Bank Name CLS : %s" %Account.BankName)
        print("Starter : %d" %cls.AcStarter)

    # invokes implicitly when instance is destroyed
    def __del__(self):
        'to destroy'
        print("Bachao, Ac No : %d delete ho raha hai" %self.AcNo)

# creating an object
Account.setBankInfo()
Account.setBankDetail("ICICI Bank", 7000)
ac1 = Account()
ac2 = Account()
ac1.getAcInfo()
ac2.getAcInfo()

