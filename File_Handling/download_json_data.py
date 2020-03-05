import json
import requests

url = input("Enter url : ")

request = requests.get(url)

data_in_text = request.text

data = json.loads(data_in_text)
print("All data is fetch successfully.")

file_name = input("Enter file name : ")

json_file = file_name+".json"

json.dump(data , open(json_file,"w"))

print("File is downloaded successfully.\nFile Name : %s"%(json_file ))