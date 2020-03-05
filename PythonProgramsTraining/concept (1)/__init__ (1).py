import sys

USER = "admin"
PIN = 451451

def validate():
    'to validate user info'
    user = input("Enter user name : ")
    pin = int(input("Enter PIN : "))
    if USER==user and PIN == pin:
        print("Wel come, admin you can use bank package")
    else:
        print("Invalid user")
        sys.exit(0)
# calling fun
validate()