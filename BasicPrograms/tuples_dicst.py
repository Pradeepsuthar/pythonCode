# 1. List are change after creating

# bill = ["07860123432","Pradeep Suthar",5,100]
# print("Before change :",bill)

# bill[2] = 20
# bill[3] = 500

# print("After change :",bill)
# bill_no = bill[0]
# name = bill[1]
# total_items = bill[2]
# total_price = bill[3] 

# print()
# print("Bill Number : %s "%bill_no)
# print("Customer Name : %s "%name)
# print("Total Items : %d "%total_items)
# print("Total Price : %.2f "%total_price)

#**********************************************************************************#

# 2. Tuples are can't change after creating

# bill = ("07860123432","Pradeep Suthar",5,100)
                 # OR
# bill = "07860123432","Pradeep Suthar",5,100

# bill_no = bill[0]
# name = bill[1]
# total_items = bill[2]
# total_price = bill[3] 

# print(bill)
# print()
# print("Bill Number : %s "%bill_no)
# print("Customer Name : %s "%name)
# print("Total Items : %d "%total_items)
# print("Total Price : %.2f "%total_price)

#---------------------------------------------------------------------------------#

# Single element in Tuple
# a = 10
# print(a)
# print(type(a))
# print()
# a = 10,
# print(a)
# print(type(a))

#---------------------------------------------------------------------------------#

#index:-9 -8 -7 -6 -5 -4 -3 -2 -1
# b = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#index:0  1  2  3  4  5  6  7  8      

# print(b[2:7])
# print(b[2:-3])
# print(b[2:-5])
# print(b[4:-2])

# print(b)
# print()
# maxValue = max(b)
# minValue = min(b)
# length = len(b)
# sumOfTuple = sum(b)
# Tuple = tuple(b)

# print("Max is :",maxValue)
# print("Min is :",minValue)
# print("Length is :",length)
# print("Sum Of Tuple Elements:",sumOfTuple)
# print("Tuple is :",Tuple)

#**********************************************************************************#

# 3. Dictionary

students = {}

while True:

    print("If you want to add a new student in Dictionary press Y/N : ",end="")
    choice = input()

    if choice == 'Y' or choice == 'y':
        new_roll_no = int(input("Enter Roll Number : "))
        std_name = input("Enter Student Name : ")
        students[new_roll_no] = std_name
        print("New Student added successfuly.")
    elif choice == 'N' or choice == 'n':
        print("\nSearch for using roll no.\n")
        while True:
            roll_no = int(input("Enter Roll No. : "))
            if roll_no != "":
                print("Hello,",students[roll_no])
            else:
                break













