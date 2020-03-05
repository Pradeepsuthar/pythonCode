import random
upper = 0
lower =0
for i in range(1000):
    code = random.randint(48,122)
    print(chr(code),end=" ")
    if (chr(code).islower()):
     lower=lower+1
    if (chr(code).isupper()):
     upper=upper+1
print("\nLower char :",lower)
print("Upper char :",upper)