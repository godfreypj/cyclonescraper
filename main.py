import scraper
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import PhotoImage, Canvas
import io
import urllib
import base64

def main():
#Create window for user to choose region
    main_window = tk.Tk()
    main_window.geometry("600x400")
    main_window.title("Cyclone Scraper")

    #Main title text
    title_lbl = tk.Label(main_window, text="Welcome to the Cyclone Scraper")
    title_lbl2 = tk.Label(main_window, text="Please select desired region below")
    title_lbl.pack()
    title_lbl2.pack()

    #function to call the appropriate method in scaper module
    def callScraper(selection):
        if selection == 1:
            data = scraper.atlc()
            popup(data)
        if selection == 2:
            data = scraper.epac()
            popup(data)
        if selection == 3:
            data = scraper.cpac()
            popup(data)
    
    #function to call popupwindow to display info to user
    def popup(data):
        #Method to restart program and close existing windows
        def restart():
            main_window.destroy()
            popup_window.destroy()
            main()
            
        #Popup window to display info to user
        popup_window = tk.Tk()
        popup_window.geometry("500x300")
        popup_window.title("Active Cyclones")
        title_lbl = tk.Label(popup_window, text=data[0])
        longlat_lbl = tk.Label(popup_window, text=data[1])
        area_lbl = tk.Label(popup_window, text=data[2])
        active_label = tk.Label(popup_window, text=data[3])
        
        #Button to restart program
        end_btn = tk.Button(popup_window, text="Main Menu", command=lambda: restart())
        end_btn.place(x=170, y=250)

        #Grab image URL and display on popup window
        raw_data = urllib.request.urlopen(data[4]).read()
        image = base64.encodebytes(raw_data)
        im = tk.PhotoImage(data=image)
        cv = tk.Canvas(bg="white")
        cv.pack(side='top', fill='both', expand='yes')
        cv.create_image(10,10,image=im, anchor="nw")
        title_lbl.pack()
        longlat_lbl.pack()
        area_lbl.pack()
        active_label.pack()
        popup_window.mainloop()

    #Buttons for selection
    atlc_btn = tk.Button(main_window, text="Atlantic", command=lambda: callScraper(1))
    epac_btn = tk.Button(main_window, text="Eastern Pacific", command=lambda: callScraper(2))
    cpac_btn = tk.Button(main_window, text="Central Pacific", command=lambda: callScraper(3))
    atlc_btn.place(x=270, y=150)
    epac_btn.place(x=255, y=200)
    cpac_btn.place(x=255, y=250)

    #Start main loop
    main_window.mainloop()


if __name__ == "__main__":
    main()