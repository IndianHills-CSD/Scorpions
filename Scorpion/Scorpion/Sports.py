import json
import http.client



def loadSports(requestType, sport = None, leagueId = None):
    conn = http.client.HTTPSConnection("www.thesportsdb.com")
    url = "/api/v1/json/1/"

    if(requestType == "allSports"):
        url += "all_sports.php"
    elif(requestType == "allLeagues"):
        if (sport != ""):
            url += "search_all_leagues.php?c=United%20States&s=" + sport
        else:
            url += "search_all_leagues.php?c=United%20States"
    elif(requestType == "Upcoming Events"):
        url += "eventsnextleague.php?id=" + leagueId
    elif(requestType == "Previous Events"):
        url += "eventspastleague.php?id=" + leagueId

    headers = {
        'x-api-host': "www.thesportsdb.com",
        'x-api-key': "1"
        }
    
    conn.request("GET", url)
    res = conn.getresponse()
    data = res.read()
    sportsDict = json.loads(data)
    return sportsDict

sportsDict = loadSports("allSports")

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

def getSportsLeague(sportName):
    leagueDict = loadSports("allLeagues", sport = sportName)
    return leagueDict

def getEventsbyLeagueId(recievedLeagueId):
    upcomingEvents = loadSports("Upcoming Events", leagueId = recievedLeagueId)
    previousEvents = loadSports("Previous Events", leagueId = recievedLeagueId)
    return upcomingEvents, previousEvents
