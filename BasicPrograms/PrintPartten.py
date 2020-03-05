# # # # #
# # # # #
# # # # #
# # # # #
for i in range(4): # for column
    for j in range(4): # for Row
        print("# ",end="")
    print("")
    

print("\n")
# 
# # 
# # # 
# # # # 
for i in range(4): # for column
    for j in range(i+1): # for Row
        print("# ",end="")
    print("")

print("\n")
# #  # #
# # #
# # 
# 
for i in range(4): # for column
    for j in range(4-i): # for Row
        print("# ",end="")
    print("")
