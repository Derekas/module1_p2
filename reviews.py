import requests,json

url = "https://hotels4.p.rapidapi.com/reviews/v2/list"

querystring = {"hotelId":"1053457920","reviewOrder":"date_newest_first","tripTypeFilter":"all"}

headers = {
    'x-rapidapi-host': "hotels4.p.rapidapi.com",
    'x-rapidapi-key': "2fcaac5907msh084e2fda1908fe5p1b57c9jsn24746a0a00f6"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print('Status code:', response.status_code)

#print(response.text)

data = response.json()
#print(data)
for e in data['data']['reviews']['body']['reviewContent']['reviews']['hermes']['groups']:
    for i in e['items']:
        print("Description=>",i["description"])