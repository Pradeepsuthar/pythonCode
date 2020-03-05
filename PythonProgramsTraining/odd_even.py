n = int(input("Enter n : "))
for i in range(1,11):
    if i%3==0:
        continue # skip this statement   
    print(i*n)
 
print("\n")

for i in range(1,11):
    if i%2!=0:
        print("Even %d"%i)
    else:
        pass #print("Odd %d"%i) #Ignore this block using pass    

     