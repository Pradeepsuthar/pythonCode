print("----------Mobile Recharge----------")

print("1. Prepaid\t 2. Postpaid")
payment_mode = int(input("Please select payment mode : "))

if payment_mode == 1:
	mobile_no = input("Enter Mobile Number : ")
	if len(mobile_no) == 10:
	    mobile_operator = input("Enter Operator : ")
	    print("Prepaid,",mobile_operator," Rajasthan")
	    Recharge_amt = float(input("Amount : "))
	    print("Recharge of Rs.",Recharge_amt,"is successful for your",mobile_operator,"number",mobile_no)
	else:
	    print("Please check your valid mobile number.")
	
	
elif payment_mode == 2:
	mobile_no = input("Enter Mobile Number : ")
	if len(mobile_no) == 10:
	    mobile_operator = input("Enter Operator : ")
	    print("Postpaid,",mobile_operator," Rajasthan")
	    Recharge_amt = float(input("Amount : "))
	    print("Recharge of Rs.",Recharge_amt,"is successful for your",mobile_operator,"number",mobile_no)
	else:
	    print("Please check your valid mobile number.")
else : 
	print("RECHARGE FAILED. Please try again")