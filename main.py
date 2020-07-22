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
    main_window.geometry("950x800")
    main_window.title("Cyclone Scraper")
    main_window.configure(bg="azure")

    #Main title text
    title_lbl = tk.Label(
        main_window, padx=30, pady=30, 
        bg="azure", borderwidth=3, relief="ridge",
        text="Welcome to the Cyclone Scraper")
    title_lbl2 = tk.Label(
        main_window, 
        bg="azure", text="Please select desired region")
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
        popup_window.geometry("550x300")
        popup_window.title("Active Cyclones")
        popup_window.configure(bg="azure")
        title_lbl = tk.Label(
            popup_window, bg="azure", borderwidth=5, 
            relief="ridge", pady=5,
            text=data[0])
        area_lbl = tk.Label(
            popup_window, bg="azure",
            text=data[1])
        longlat_lbl = tk.Label(
            popup_window, bg="azure",
            text=data[2])
        active_label = tk.Label(
            popup_window, bg="azure",
            text=data[3])
        
        #Button to restart program
        end_btn = tk.Button(popup_window, text="Main Menu", command=lambda: restart())
        end_btn.place(x=450, y=170)

        #Grab image URL and display on popup window
        raw_data = urllib.request.urlopen(data[4]).read()
        image = base64.encodebytes(raw_data)
        im = tk.PhotoImage(data=image)
        cv = tk.Canvas(bg="azure")
        cv.pack(side='top', fill='both', expand=1)
        cv.create_image(10,10,image=im, anchor="nw")

        #Place labels and run popup window loop
        title_lbl.place(x=20,y=20,width=500)
        area_lbl.place(x=20,y=60)
        longlat_lbl.place(x=20,y=100)
        active_label.place(x=20,y=140)
        popup_window.mainloop()

    #Buttons for selection
    atlc_btn = tk.Button(
        main_window, bg="dodgerblue2", padx=30, pady=30,
        borderwidth=10, relief="raised",
        text="Atlantic", command=lambda: callScraper(1))
    epac_btn = tk.Button(
        main_window, bg="dodgerblue2", padx=30, pady=30,
        borderwidth=10, relief="raised",
        text="Eastern Pacific", command=lambda: callScraper(2))
    cpac_btn = tk.Button(
        main_window, bg="dodgerblue2", padx=30, pady=30,
        borderwidth=10, relief="raised",
        text="Central Pacific", command=lambda: callScraper(3))
    atlc_btn.place(x=410, y=250)
    epac_btn.place(x=395, y=370)
    cpac_btn.place(x=395, y=490)

    #Start main loop
    main_window.mainloop()


if __name__ == "__main__":
    main()