import json
import requests

readData = json.load(open("zomato.json"))

name = readData["name"]
address = readData["location"]["address"]
locality = readData["location"]["locality"]
city =  readData["location"]["city"]
zip_code = readData["location"]["zipcode"]
print("Name of  Hotel : %s"%(name))
print("Address : %s, %s (%s)"%(locality,city,zip_code))

# # request = requests.get("https://www.quandl.com/api/v3/datasets/BUNDESBANK/BBK01_JJB934.json?api_key=mTK-T4RzZ5rdyzLSoL3F")
# request = requests.get("https://gist.githubusercontent.com/yoobi55/5d36f13e902a75225a39a8caa5556551/raw/cbd57cfdddbdfc009fd9ccdadf5fb7129af71c73/restaurant-data.json")


# # print(type(request))

# data_in_text = request.text

# data = json.loads(data_in_text)

# # print(type(data))
# # print(data)

# for item in data:
#     index = 0    
#     print("Restaurants Name : %s"%(data[item][9]["name"]))
#     print("Address : %s"%(data[item][9]["address"]))
#     print("Cuisine Type : %s"%(data[item][9]["cuisine_type"]))
    

  

