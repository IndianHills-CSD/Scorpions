import http.client
import re
import requests
import json

def eLeagueFunctions():
    #conn = http.client.HTTPSConnection("api-pandascore.p.rapidapi.com")
    #
    #headers = {
    #'x-rapidapi-host': "api-pandascore.p.rapidapi.com",
    #'x-rapidapi-key': "UDRax380JpWU7t5aGXaEyVAyTjOnf8oaI3YEBBYfw_8Dntxr7lE"
    #}
    #
    #conn.request("GET", "/players.json", headers=headers)
    url = "https://api.pandascore.co/lol/champions?&token=UDRax380JpWU7t5aGXaEyVAyTjOnf8oaI3YEBBYfw_8Dntxr7lE"

    conn = requests.get(url)

    #res = conn.getresponse()
    #data = res.read()
    data = conn.json()
    info = json.dumps(data,sort_keys = True, indent = 4)

    #print(info)
    #
    #print(data.decode("utf-8"))
    #
    #dataDecoded = json.loads(data)
    
    #theResponse = addDetails(info)
    #
    #return theResponse

def addDetails(baseDict):
    length = len(baseDict['Search'])
    for index in range(length):
        baseDict['Search'][index]['details'] = idSearch(baseDict['Search'][index]['imdbID'])
    return baseDict


