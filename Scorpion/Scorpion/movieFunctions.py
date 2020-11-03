import http.client
import re
import json
import urllib.parse
import pyodbc

def movieSearch(searchString):
    conn = http.client.HTTPSConnection("movie-database-imdb-alternative.p.rapidapi.com")

    #searchString = urllib.parse.quote(searchString)

    headers = {
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
        'x-rapidapi-key': "aacba34385msh2de2878b096e1a1p13e391jsn86c2163e469d"
        }

    conn.request("GET", "/?page=1&r=json&s="+searchString, headers=headers)

    res = conn.getresponse()
    data = res.read()
    dataDecoded = json.loads(data)
    
    theResponse = addDetails(dataDecoded)

    return theResponse

def addDetails(baseDict):
    length = len(baseDict['Search'])
    for index in range(length):
        baseDict['Search'][index]['details'] = json.loads(idSearch(baseDict['Search'][index]['imdbID']))
    return baseDict


def idSearch(id):
    conn = http.client.HTTPSConnection("movie-database-imdb-alternative.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
        'x-rapidapi-key': "aacba34385msh2de2878b096e1a1p13e391jsn86c2163e469d"
        }

    conn.request("GET", "/?i="+id+"&r=json", headers=headers)

    res = conn.getresponse()
    dataToReturn = res.read()

    #dataToReturn = json.loads(data);
    return dataToReturn;

def formatSearch(searchS):
    import re
    searchS = re.sub('[^0-9a-zA-Z]+', ' ', searchS)
    searchS.replace(" ", "%20", -1)
    return searchS

def storeMovies(conn):
    upcomingMovies = apiUpcomingMovies()
    trendingMovies = apiTrendingMovies()




def apiUpcomingMovies():
    import http.client

    conn = http.client.HTTPSConnection("rapidapi.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "aacba34385msh2de2878b096e1a1p13e391jsn86c2163e469d",
        'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
        }

    conn.request("GET", "/?page=1&type=get-upcoming-movies", headers=headers)

    res = conn.getresponse()
    data = res.read()

    dataToReturn = json.loads(data);
    return dataToReturn;

def apiTrendingMovies():
    import http.client

    conn = http.client.HTTPSConnection("rapidapi.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "aacba34385msh2de2878b096e1a1p13e391jsn86c2163e469d",
        'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
        }

    conn.request("GET", "/?page=1&type=get-trending-movies", headers=headers)

    res = conn.getresponse()
    data = res.read()
                    
    dataToReturn = json.loads(data);
    return dataToReturn;



def getUpcomingMovies():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM UpcomingMovies.table')

def getConnection():
    conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}',
                      server='(localdb)\MSSQLLocalDB',
                      database='Scorpions',
                      trusted_connection='yes')
    return conn