class Account:
    'to define account with infomation and operations'

    # creating static variables
    BankName = "HDFC Bank"

    def __init__(self):
        'to initialize instance variables'
        Account.AcStarter += 1
        self.AcNo = Account.AcStarter
        self.AcHName = input("Enter Ac H Name : ")
        self.AcBalance = float( input("Enter Ac Balance : ") )

    def setAcInfo(self):
        'to initialize instance variables'
        self.AcNo = int(input("Enter Ac No : "))
        self.AcHName = input("Enter Ac H Name : ")
        self.AcBalance = float( input("Enter Ac Balance : "))
    
    def getAcInfo(self):
        'to display account detail'
        print("- - Account Detail - -")
        print("Ac No : %d" %self.AcNo)
        print("Ac Name : %s" %self.AcHName)
        print("Ac Balance : %0.2f Rs" %self.AcBalance)
    
    def withdraw(self, amt):
        'to withdraw from account balance'
        if self.AcBalance>=amt:
            self.AcBalance-=amt
            print("Bal after withdraw : %0.2f Rs" %self.AcBalance)
        else:
            print("Low balance")

    @staticmethod
    def setBankInfo():
        'to initialize Bank Info'
        Account.BankName = input("Enter Bank Name : ")
        # creating new static variable
        Account.AcStarter = int( input("Enter Ac Stater : ") )
        print("Bank Name : %s" %Account.BankName)
        print("Ac Start : %d" %Account.AcStarter)

    @classmethod
    def setBankDetail(cls, bn, start):
        'to set bank detail by args'
        cls.BankName = bn
        Account.AcStarter = start
        print("Bank Name(cls) : %s" %Account.BankName)
        print("Ac Start (cls) : %d" %cls.AcStarter)

    # invokes implicitly when an instance is destroyed
    def __del__(self):
        'to destroy an object'
        print("Please Help, Expiring Ac No : %d" %self.AcNo)

# creating an object
Account.setBankInfo()
Account.setBankDetail("ICICI Bank", 6000)
ac1 = Account()
ac2 = Account()
ac3 = Account()
ac1.getAcInfo()
ac2.getAcInfo()
ac3.getAcInfo()