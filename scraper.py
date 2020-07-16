import pip._vendor.requests as requests
from bs4 import BeautifulSoup

#The class to retrieve data from the NOAA website.  Depending on the users selection,
#  this will either retrieve data from Central, Eastern Pacific or Atlantic.  The args
#  for the class are default "self" and the "selection", which is an int (for now)
class scraper:
    def __init__(self, selection):
        self.selection = int(selection)
        if selection == 1:
            page = requests.get("https://www.nhc.noaa.gov/?cpac")
            soup = BeautifulSoup(page.content, 'html.parser')
            for text in soup.select('a[href="/cyclones/?cpac"]'):
                activeStatus = text.get_text()
            activeTitle = soup.select("th span")[3].get_text()
            activeLongLat =  soup.select("th span")[4].get_text()
            print("Status: ", activeStatus)
            print("Area: ", activeTitle)
            print("Long/Lat: ", activeLongLat)
        if selection == 2:
            page = requests.get("https://www.nhc.noaa.gov/?epac")
            soup = BeautifulSoup(page.content, 'html.parser')