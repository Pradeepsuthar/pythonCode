import sys

USER = "admin"
PIN = 1212
print("Hello, Are you admin?")

def validate():
    'to validate user'
    user = input("Enter User Name : ")
    pin = int( input("Enter PIN : ") )
    if USER == user and PIN == pin:
        print("Wel Come, admin you cal use basic package")
    else:
        print("invalid user")
        sys.exit(0)

# calling
validate()