import requests

url = "https://api.publicapis.org/entries"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload).json()

temp = []

for i in response['entries']:
    if i['Auth'] == "" and len(temp) <= 10:
        temp.append({'API': i['API'], 'Link': i['Link'], 'Category': i['Category']})

    if len(temp) == 10:
        print('API || Link || Category')
        for j in temp:
            print(f"{j['API']} || {j['Link']} || {j['Category']}")
        input() # just press enter to get next 10 response
        temp.clear()