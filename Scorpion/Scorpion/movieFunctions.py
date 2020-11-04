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

def getJsonDetails(baseDict):
    length = len(baseDict['movie_results'])
    returnArray = []
    for index in range(length):
        returnArray.append(json.loads(idSearch(baseDict['movie_results'][index]['imdb_id'])))
    return returnArray


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


#
def leagueGameSearch(searchString):
    conn = http.client.HTTPSConnection("api-pandascore.p.rapidapi.com")

    headers = {
    'x-rapidapi-host': "api-pandascore.p.rapidapi.com",
    'x-rapidapi-key': "0a56ecd8a4msh557dc3387a3c8b2p18a8a5jsnda85dc032912"
    }

    conn.request("GET", "/tournaments/%7Bid%7D.json", headers=headers)
    res = conn.getresponse()
    data = res.read()

    dataDecoded = json.loads(data)

    theResponse = addDetails(dataDecoded)

    return theResponse

def formatSearch(searchS):
    import re
    searchS = re.sub('[^0-9a-zA-Z]+', ' ', searchS)
    searchS.replace(" ", "%20", -1)
    return searchS

def storeMovies(conn):
    upcomingMovies = apiUpcomingMovies()
    trendingMovies = apiTrendingMovies()

    upcomingMovies = getJsonDetails(upcomingMovies)
    trendingMovies = getJsonDetails(trendingMovies)

    #apiDeleteStoredMovies(conn)

    apiSetUpcomingMovies(conn, upcomingMovies)
    apiSetTrendingMovies(conn, trendingMovies)





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

def apiDeleteStoredMovies(conn):
    sql = """\
    DECLARE	@return_value Int
    EXEC	@return_value = [dbo].[DeleteHeldMovies]
    SELECT	@return_value as 'Return Value'
    """
    conn.execute(sql)


def apiSetUpcomingMovies(conn, upcomingMovies):
    outfile = open("StoredUpcomingMovies.txt", "w") 
    json.dump(upcomingMovies, outfile)
    outfile.close()
    '''
        sql = """\
        DECLARE	@return_value Int
        EXEC	@return_value = [dbo].[AddUpcomingMovie]
		        @param1 = ?
        SELECT	@return_value as 'Return Value'
        """
        params = ('{"Title":"Way Down","Year":"2020","Rated":"N/A","Released":"27 Nov 2020","Runtime":"N/A","Genre":"Action, Thriller","Director":"Jaume BalaguerÃ³","Writer":"Rowan Athale, Michel Gaztambide, Borja Glez. Santaolalla, AndrÃ©s M. Koppel, Rafa MartÃ­nez (Writer)","Actors":"Famke Janssen, Freddie Highmore, Astrid BergÃ¨s-Frisbey, Sam Riley","Plot":"The movie stars Highmore as Thom, a genius engineering graduate whose interest is piqued by the Bank of Spain whose safe, built over 100 years ago, has no blueprints and whose security ...","Language":"English","Country":"Spain","Awards":"N/A","Poster":"https://m.media-amazon.com/images/M/MV5BYTE2Y2E4ZDctODQxOC00NjgwLWEwYmEtZmVhYzUyMjM5MWZlXkEyXkFqcGdeQXVyODc0OTEyNDU@._V1_SX300.jpg","Ratings":[],"Metascore":"N/A","imdbRating":"N/A","imdbVotes":"N/A","imdbID":"tt9742794","Type":"movie","DVD":"N/A","BoxOffice":"N/A","Production":"N/A","Website":"N/A","Response":"True"}',)
        conn.execute(sql, params)
    '''
    
def apiSetTrendingMovies(conn, trendingMovies):
    outfile = open("StoredTrendingMovies.txt", "w")
    json.dump(trendingMovies, outfile)
    outfile.close()
    '''
        sql = """\
        DECLARE	@return_value Int
        EXEC	@return_value = [dbo].[AddTrendingMovie]
		        @param1 = ?
        SELECT	@return_value as 'Return Value'
        """
        params = (i,)
        conn.execute(sql, params)
    '''


def getUpcomingMovies():
    json_file = open("StoredUpcomingMovies.txt")
    data = json.load(json_file)
    return data
    '''
        moviesList = []
        sql = """\
        DECLARE	@return_value Int
        EXEC	@return_value = [dbo].[GetUpcomingMovies]
        SELECT	@return_value as 'Return Value'
        """
        conn.execute(sql)
        rows = conn.fetchall()
        while rows:
            print(rows)
            if conn.nextset():
                rows = conn.fetchall()
            else:
                rows = None
    '''

def getTrendingMovies():
    json_file = open("StoredTrendingMovies.txt")
    data = json.load(json_file)
    return data
    '''
        moviesList = []
        sql = """\
        DECLARE	@return_value Int
        EXEC	@return_value = [dbo].[GetTrendingMovies]
        SELECT	@return_value as 'Return Value'
        """
        conn.execute(sql)
        rows = conn.fetchall()
        while rows:
            print(rows)
            if conn.nextset():
                rows = conn.fetchall()
            else:
                rows = None
    '''


def getConnection():
    conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}',
                      server='(localdb)\MSSQLLocalDB',
                      database='Scorpions',
                      trusted_connection='yes')
    return conn
