import json
import requests


vehicle_name = "Flight"
# if data is available on server machine
# url = 'https://gist.githubusercontent.com/tdreyno/4278655/raw/7b0762c09b519f40397e4c3e100b097d861f5588/airports.json'
# request = requests.get(url)
# data_in_text = request.text
# data = json.loads(data_in_text)

# if data is available on local machine
FILE_NAME = "data.json"
fr = open(FILE_NAME)
# reading all data from json file info python compative
data = json.load(fr)
fr.close()



print()
print("*"*160)
print("\n\t\t\t\t\t\t\t\tWelcome to our project\n")
print("\t\t\t\t\t\t\tBook Domestic And International %s Tickets"%(vehicle_name))
print()
print("*"*160)

print("Enter your route -")
boarding = input("From : ")
destination = input("Destination : ")
print("Travel Class : \n1.Economy\t2.Business\t3.First Class\t4.Premium Economy")
travel_class = input("Travel Class : ")
print()
print("*"*160)

boarding = boarding.title()
destination = destination.title()

print("\nFrom : %s \nTo : %s"%(boarding,destination))
print("Travel Class : %s"%(travel_class))
print("\nToday's avalible %ss here\n"%(vehicle_name))
    
# print(boarding)
# print(destination)

for item in  data:
    if boarding == data[item][0]["boarding"] and data[item][0]["to"]:
        print("Airport : %s"%(data[item][0]["name"]))
        print("From %s to %s"%(data[item][0]["boarding"],data[item][0]["to"]))
        print("Flight Name : %s\tFlight No.%s"%(data[item][0]["type"],data[item][0]["flights_no"]))
        print("Total Time : %s"%(data[item][0]["time"]))
        print("Price : Rs.%s"%(data[item][0]["price"]))
        break
    else:
        print("Not Found")
        break
   

# for item in  data:
# #    print(data[item][0]["name"])
#    print("From %s to %s"%(data[item][0]["boarding"],data[item][0]["to"]))
















        # if city == select_data["code"]:
        #     print("\n%s\t%s\t%s"%(item["code"],item["name"],item["city"]))
        #     break
        # else:
        #     print("Not found")
        #     break
    





# for item in  data:
#     print(item)
# 		print("\n%s\t%s\t%s"%(item["code"],item["name"],item["city"]))



# for item in  data:
#     for select_data in item:
#         if boarding == item["city"]:
#             print("\n%s\t%s\t%s"%(item["code"],item["name"],item["city"]))
#             break
#         else:
#             print("Not found")
#             break
#     else:
#         break   













