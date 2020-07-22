# cyclonescraper
Python program that retrieves active tropical cyclones from NOAA webpage

scraper module -
    This module uses requests library to grab the needed NOAA URL's and return the information for
    beautifulsoup to parse into maniputable objects.  The needed information is then scraped from the website and returned into a list as strings, and sent to the main module

main module - 
    This module is for the GUI.  tkinter is used to present the user with a selection of three areas:
    Atlantic Ocean, Eastern Pacific & Central Pacific Ocean.  Once the user has made the choice, the scaper module is called, and the data is returned.  A popup window is presented as well as an image of the selected area.
