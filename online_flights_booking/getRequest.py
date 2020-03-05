import json
import requests

# url = "https://developers.zomato.com/api/v2.1/geocode?lat=24.624058599999998&lon=73.8536568"

# headers = {
#     'x-rapidapi-host': "aerodatabox.p.rapidapi.com",
#     'x-rapidapi-key': "7041e0211f830d08bb8d03dd413b9e35"
#     }

# response = requests.request("GET", url, headers=headers)

# data = response.json
# print(data)



# if data is available on server machine
url = 'https://developers.zomato.com/api/v2.1/geocode?lat=24.624058599999998&lon=73.8536568'
request = requests.get(url)
data_in_text = request.text
data = json.loads(data_in_text)

print(data)

# url = 'curl -X GET --header "Accept: application/json" --header "user-key: 7041e0211f830d08bb8d03dd413b9e35" "https://developers.zomato.com/api/v2.1/geocode?lat=24.624058599999998&lon=73.8536568"'


# api_key = '7041e0211f830d08bb8d03dd413b9e35'

# lat = '24.624058599999998'
# lon = '73.8536568'

# requests_url = 'https://developers.zomato.com/api/v2.1/geocode?lat=24.624058599999998&lon=73.8536568'

