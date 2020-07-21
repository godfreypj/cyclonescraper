import pip._vendor.requests as requests
from bs4 import BeautifulSoup

#The class to retrieve data from the NOAA website.  Depending on the users selection,
#  this will either retrieve data from Central, Eastern Pacific or Atlantic.  The args
#  for the class are default "self" and the "selection", which is an int (for now)

    
def atlc():
    page = requests.get("https://www.nhc.noaa.gov/?atlc")
    soup = BeautifulSoup(page.content, 'html.parser')
    imagePage = requests.get("https://www.nhc.noaa.gov/gtwo.php?basin=atlc&fdays=2")
    imageSoup = BeautifulSoup(page.content, 'html.parser')
    for text in soup.select('a[href="/cyclones/"]'):
        title = text.get_text()
    areaTitle = soup.select("th span")[0].get_text()
    activeStorms = soup.find_all(class_='hdr')[0].get_text()
    stormImage = imageSoup.find("img", {"id": "twofig0d"})
    image = "https://www.nhc.noaa.gov" + stormImage["src"][:-7]
    data = [title, "No Long/Lat Available", areaTitle, activeStorms, image]
    return data

def epac():
    page = requests.get("https://www.nhc.noaa.gov/?epac")
    soup = BeautifulSoup(page.content, 'html.parser')
    imagePage = requests.get("https://www.nhc.noaa.gov/gtwo.php?basin=epac&fdays=2")
    imageSoup = BeautifulSoup(page.content, 'html.parser')
    for text in soup.select('a[href="/cyclones/?epac"]'):
        title = text.get_text()
    areaTitle = soup.select("th span")[1].get_text()
    areaLongLat = soup.select("th span")[2].get_text()
    activeStorms = soup.find_all(class_='hdr')[1].get_text()
    stormImage = imageSoup.find("img", {"id": "twofig0d"})
    image = "https://www.nhc.noaa.gov" + stormImage["src"][:-7]
    data = [title, areaTitle, areaLongLat, activeStorms, image]
    return data

def cpac():
    page = requests.get("https://www.nhc.noaa.gov/?cpac")
    soup = BeautifulSoup(page.content, 'html.parser')
    imagePage = requests.get("https://www.nhc.noaa.gov/gtwo.php?basin=cpac&fdays=2")
    imageSoup = BeautifulSoup(page.content, 'html.parser')
    for text in soup.select('a[href="/cyclones/?cpac"]'):
        title = text.get_text()
    areaTitle = soup.select("th span")[3].get_text()
    areaLongLat =  soup.select("th span")[4].get_text()
    activeStorms = soup.find_all(class_='hdr')[2].get_text()
    stormImage = imageSoup.find("img", {"id": "twofig0d"})
    image = "https://www.nhc.noaa.gov" + stormImage["src"][:-7]
    data = [title, areaTitle, areaLongLat, activeStorms, image]
    return data




            