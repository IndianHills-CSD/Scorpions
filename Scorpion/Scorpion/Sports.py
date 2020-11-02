import requests
import json
import http.client



def loadSports():
    conn = http.client.HTTPSConnection("www.thesportsdb.com")
    url = "/api/v1/json/1/all_sports.php"

    headers = {
        'x-api-host': "www.thesportsdb.com",
        'x-api-key': "1"
        }

    conn.request("GET", url)
    res = conn.getresponse()
    data = res.read()
    sportsDict = json.loads(data)
    return sportsDict

sportsDict = loadSports()

def printAllSports():
    print(sportsDict['sports'])

def getSport(sportName):
    length = len(sportsDict['sports'])
    for index in range(length):
        if (sportsDict['sports'][index]['strSport'] == sportName):
            return retrieveSportDesc(index)

def retrieveSportDesc(index):
    sportDesc = sportsDict['sports'][index]['strSportDescription']

    return sportDesc
