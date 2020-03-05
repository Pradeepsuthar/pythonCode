row = int(input("Enter row : "))

for r in range(1,row+1):
 c=1
 sum=0
 while c <=r:
  print(c, end="")
  sum+=c
  c+=1
 else:
  print("\tsum :",sum)