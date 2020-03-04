import requests
import json

open_db_api_path = 'http://www.omdbapi.com/?apikey=918c131e'


class MovieReview():
    title = None
    year = None

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def getMovie(self):
        path = open_db_api_path
        if self.title is not None:
            path = path + '&t=' + self.title
        if self.year is not None:
            path = path + '&y=' + self.year

        response = requests.get(path)
        jsonResponse = response.json()
        # print(jsonResponse)
        if 'Title' in jsonResponse:

            print("Title: "+jsonResponse['Title'])
            print("Year: "+jsonResponse['Year'])
            print("Genre: "+jsonResponse['Genre'])
            print("Actors: "+jsonResponse['Actors'])
            print("Plot: "+jsonResponse['Plot'])
            print("Type: "+jsonResponse['Type'])
            try:
                print("Production: " + jsonResponse['Production'])
                print("POSTER: "+jsonResponse['Poster'])
                print("BoxOffice: " + jsonResponse['BoxOffice'])
            except:
                print("")

            for rating in jsonResponse['Ratings']:
                print(rating)
        else:
            print("Movie or series not found")