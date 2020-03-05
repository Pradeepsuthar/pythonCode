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