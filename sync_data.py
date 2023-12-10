import os
import http.client
import asyncio
import requests
import json

print("Example of endpoint: 178.79.181.117:80")
# source_endpoint = input("enter source endpoint: ")
# your_node_endpoint = input("enter your node endpoint: ")

# conn = http.client.HTTPConnection(source_endpoint)
# nconn = http.client.HTTPConnection(your_node_endpoint)


async def load_data_from_node():
    url = "https://fir-task-menanger-default-rtdb.europe-west1.firebasedatabase.app/dBase0//.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        for item in data.values():
            await add_data_to_database(item)
    else:
        print(f"Request failed with status code {response.status_code}")


async def add_data_to_database(item):

    # parse item
    date = item['Datum_i_vrijeme']
    fiels = item['field']
    blocName = item['Ime']
    ownerName = item['Ime_osobe_koja_unosi_podatke']
    requestType = item['vsrta_unosa']

    # upload data to database
    payload = f'''
   {{
     "Datum_i_vrijeme": "{date}",
     "Ime": "{ownerName}",
     "field": {{"key": "{fiels}"}},
     "Ime_osobe_koja_unosi_podatke": "{ownerName}",
     "vsrta_unosa": "{requestType}"
   }}
   '''
    headers = {
        'Content-Type': "application/json",
    }

    conn.request("POST", "/api/collections/bloc/records", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


asyncio.run(load_data_from_node())  # load_data_from_node()
