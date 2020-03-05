x = int(input("How many you want to candy : "))

available_candy = 5

i=1
while i<=x:
    if x>available_candy:
        print("Out of stock")
        break
    
    print("Candy")
    i+=1