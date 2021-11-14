import requests,json

url = "https://hotels4.p.rapidapi.com/locations/v2/search"

ciudad= input("Introduzca una ciudad: ")
querystring = {"query":ciudad,"locale":"en_US","currency":"USD"}

headers = {
    'x-rapidapi-host': "hotels4.p.rapidapi.com",
    'x-rapidapi-key': "2fcaac5907msh084e2fda1908fe5p1b57c9jsn24746a0a00f6"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print('Status code:', response.status_code)
data = response.json()


for e in data['suggestions'][1]['entities']:
    print("name =>",e["name"]
    )
