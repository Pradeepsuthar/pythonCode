# 1. List are change after creating

bill = ["07860123432","Pradeep Suthar",5,100]
print("Before change :",bill)

bill[2] = 20
bill[3] = 500

print("After change :",bill)
bill_no = bill[0]
name = bill[1]
total_items = bill[2]
total_price = bill[3] 

print()
print("Bill Number : %s "%bill_no)
print("Customer Name : %s "%name)
print("Total Items : %d "%total_items)
print("Total Price : %.2f "%total_price)