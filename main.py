import scraper
import tkinter as tk

if __name__ == "__main__":

    #Create window for user to choose region
    main_window = tk.Tk()
    main_window.geometry("600x400")
    main_window.title("Cyclone Scraper")

    #Main title text
    title_lbl = tk.Label(main_window, text="Welcome to the Cyclone Scraper")
    title_lbl2 = tk.Label(main_window, text="Please select desired region below")
    title_lbl.pack()
    title_lbl2.pack()

    #Buttons for selection
    atlc_btn = tk.Button(main_window, text="Atlantic", command=lambda: scraper.scraper(3))
    epac_btn = tk.Button(main_window, text="Eastern Pacific", command=lambda: scraper.scraper(2))
    cpac_btn = tk.Button(main_window, text="Central Pacific", command=lambda: scraper.scraper(1))
    atlc_btn.place(x=270, y=150)
    epac_btn.place(x=255, y=200)
    cpac_btn.place(x=255, y=250)
    
    #Start main loop
    main_window.mainloop()