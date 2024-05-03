import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser
import asyncio
import urllib.request
import io
import time
from PIL import Image, ImageTk
from datetime import datetime
from openweather import fetch_weather_data
from nasa import fetch_nasa, fetch_rover
from news import fetch_news
from processing import get_system_resources

# debugger
import hupper
def start_reloader():
    reloader = hupper.start_reloader('MyDashboard.main')

# Functions for updating weather, time, process, and news
def update_weather():
    weather_data = fetch_weather_data()
    label_city.config(text=f"{weather_data['city_name']}".upper(), fg="black", font=("Terminal", 16))
    label_description.config(text=f"{weather_data['weather_description']}".upper(), fg="black", font=("Terminal", 16))
    label_wind_speed.config(text=f"{weather_data['wind_speed']} km/h", fg="black", font=("Terminal", 16))
    label_temp.config(text=f"{weather_data['temperature_celsius']:.2f}°C", fg="black", font=("Terminal", 16))
    app.after(60000, update_weather)

def update_time():
    current_time = time.strftime("%H:%M:%S %p")
    clock_label.config(text=current_time, fg="black", font=("Terminal", 16))
    today = datetime.today()
    formatted_date = today.strftime('%a, %d %B %Y')
    date_label.config(text=f"{formatted_date}", fg="black", font=("Terminal", 16))
    app.after(1000, update_time)

def update_process():
    process = get_system_resources()
    cpu_label.config(text=f"{process['cpu_percent']} %".upper(), fg="black", font=("Terminal", 16))
    ram_label.config(text=f"{process['memory_percent']} %".upper(), fg="black", font=("Terminal", 16))
    app.after(2000, update_process)
    
def update_news(type_of_news='global', sec=None):
    for widget in news_frame.winfo_children():
        widget.destroy()

    # Get news articles
    articles = fetch_news(type_of_news, sec)
    counter = 0

    # Add news titles, descriptions, and "Read More" links to the frame
    for article in articles:
        news_source = tk.Frame(news_frame, background="black", borderwidth=2, relief="solid")
        news_source.pack(fill="both", expand=True)
        
        # news_source.grid_rowconfigure(0, weight=1)
        # news_source.grid_rowconfigure(1, weight=1)
        # news_source.grid_columnconfigure(0, weight=1)
        # news_source.grid_columnconfigure(1, weight=1)

        title_label = tk.Label(news_source, text=article['title'], font=("Arial", 10), borderwidth=1, relief="solid")
        # title_label.grid(row=0, column=0, sticky="w")
        title_label.pack(side="left", fill="both", expand=True)

        description_label = tk.Label(news_source, text=article['description'], font=("Arial", 8), borderwidth=1, relief="solid", wraplength=200)
        # description_label.grid(row=1, column=0, sticky="w")
        description_label.pack(side="left", fill="both")

        def open_url(url):
            webbrowser.open(url)

        read_more_label = tk.Label(news_source, text="Read More", fg="blue", cursor="hand2", borderwidth=1, relief="solid", padx=20, pady=20)
        read_more_label.bind("<Button-1>", lambda e, url=article['url']: open_url(url))
        # read_more_label.grid(row=0, column=1, sticky="w")
        read_more_label.pack(side="right", fill="both")
        
        def update_title_width(event):
            wraplength = event.width - 12
            event.widget.configure(wraplength=wraplength)        

        title_label.bind("<Configure>", update_title_width)

        counter += 1

def search_exploit_news():
    news_entry_text = news_entry.get()
    update_news('exploit', news_entry_text)

def get_top_news():
    update_news('global') 

# Initialize the Tkinter application
app = tk.Tk()
app.title("Space Explorer Dashboard")
app.configure(background="blue", padx=10, pady=10)
app.minsize(300, 400)
app.geometry("1000x600")

path = "mountain.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(app, image = img)

#The Pack geometry manager packs widgets in rows or columns.
# panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.grid(rowspan=15, columnspan=15, sticky="snew")

# responsive root
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(3, weight=1)

# Load and set up icons
city_img = Image.open('images/map.png').resize((60,60))
city_icon = ImageTk.PhotoImage(city_img)
cloud_img = Image.open('images/cloudy.png').resize((60,60))
cloud_icon = ImageTk.PhotoImage(cloud_img)
wind_img = Image.open('images/wind-turbine.png').resize((60,60))
wind_icon = ImageTk.PhotoImage(wind_img)
temp_img = Image.open('images/thermometer.png').resize((60,60))
temp_icon = ImageTk.PhotoImage(temp_img)
news_img = Image.open('images/world-news.png').resize((60,60))
news_icon = ImageTk.PhotoImage(news_img)
cpu_img = Image.open('images/cpu.png').resize((60,60))
cpu_icon = ImageTk.PhotoImage(cpu_img)
ram_icon = Image.open('images/ram-memory.png').resize((60,60))
ram_icon = ImageTk.PhotoImage(ram_icon)

# Set up clock and date labels
clock_label = tk.Label(app, font=("Terminal", 16), fg="black", borderwidth=3, relief="solid", padx=2, pady=2)
clock_label.grid(row=0, column=0, sticky='w')
date_label = tk.Label(app, font=("Terminal", 16), fg="black", borderwidth=3, relief="solid", padx=2, pady=2)
date_label.grid(row=1, column=0, sticky='w', pady=(0, 30))

# Set up weather frame
weather_frame = tk.Frame(app, borderwidth=3, relief="solid", padx=2, pady=2)
weather_frame.grid(row=2, column=0, sticky='w')
weather_frame.grid_rowconfigure(0, weight=1)
weather_frame.grid_rowconfigure(1, weight=1)
weather_frame.grid_columnconfigure(0, weight=1)
weather_frame.grid_columnconfigure(1, weight=1)

# Add weather labels and icons
city_label = tk.Label(weather_frame, image=city_icon, bg="black")
city_label.grid(row=0, column=0, padx=2, pady=2, sticky="w")
label_city = tk.Label(weather_frame, text="", font=("Terminal", 16), fg="black")
label_city.grid(row=0, column=1, padx=2, pady=2, sticky="w")

cloud_label = tk.Label(weather_frame, image=cloud_icon, bg="black")
cloud_label.grid(row=1, column=0, padx=2, pady=2, sticky="w")
label_description = tk.Label(weather_frame, text="", font=("Terminal", 16), fg="black")
label_description.grid(row=1, column=1, padx=2, pady=2, sticky="w")

wind_label = tk.Label(weather_frame, image=wind_icon, bg="black")
wind_label.grid(row=2, column=0, padx=2, pady=2, sticky="w")
label_wind_speed = tk.Label(weather_frame, text="", font=("Terminal", 16), fg="black")
label_wind_speed.grid(row=2, column=1, padx=2, pady=2, sticky="w")

temp_label = tk.Label(weather_frame, image=temp_icon, bg="black")
temp_label.grid(row=3, column=0, padx=2, pady=2, sticky="w")
label_temp = tk.Label(weather_frame, text="", font=("Terminal", 16), fg="black")
label_temp.grid(row=3, column=1, padx=2, pady=2, sticky="w")

cpu = tk.Label(weather_frame, image=cpu_icon, bg="black")
cpu.grid(row=4, column=0, padx=2, pady=2, sticky="w")
cpu_label = tk.Label(weather_frame, font=("Terminal", 16), fg="black")
cpu_label.grid(row=4, column=1, padx=2, pady=2, sticky="w")

ram = tk.Label(weather_frame, image=ram_icon, bg="black")
ram.grid(row=5, column=0, padx=2, pady=2, sticky="w")
ram_label = tk.Label(weather_frame, font=("Terminal", 16), fg="black")
ram_label.grid(row=5, column=1, padx=2, pady=2, sticky="w")

# vertical separator
separator = ttk.Separator(app, orient='vertical')
separator.grid(row=2, column=1, rowspan=12, sticky='ns', padx=(30))

# news info
# news entry container
news_container = tk.Frame(app, background="white")
news_container.grid(row=1, column=3, sticky="w")

news_entry = tk.Entry(news_container, borderwidth=3, relief="solid", background="white")
news_entry.pack(side="left", fill="both", expand=1)

news_search = tk.Button(news_container, text="Search", command=search_exploit_news, padx=10, pady=10, borderwidth=3, relief="solid", background="blue", fg="white")
news_search.pack(side="left", fill="x", padx=1)

clear_search = tk.Button(news_container, text="Get Top News", command=get_top_news, padx=10, pady=10, borderwidth=3, relief="solid", background="blue", fg="white")
clear_search.pack(side="left", fill="x")

# main container
container = tk.Frame(app, background="blue")
container.grid(row=2, column=3, sticky="snew")

# Create a news_canvas widget and scrollbar widget
news_canvas = tk.Canvas(container, background="orange")
news_scroll = tk.Scrollbar(container, orient="vertical", command=news_canvas.yview)
news_canvas.pack(side="left", fill="both", expand=True) 
news_scroll.pack(side="right", fill="y")

# news frame
news_frame = tk.Frame(news_canvas, background="green")

# Use the create_window method to add the button to the news_canvas, filling the entire news_canvas
frame_id = news_canvas.create_window(0, 0, window=news_frame, anchor='nw')

# Bind the <Configure> event to the news_canvas
def on_canvas_configure(event):
    # Update the scroll region to encompass all the widgets in the news_frame
    news_canvas.configure(scrollregion=news_canvas.bbox("all"))
    news_canvas.itemconfig(frame_id, width=event.width)

news_canvas.bind('<Configure>', on_canvas_configure)

# Configure the yscrollcommand for the news_canvas
news_canvas.configure(yscrollcommand=news_scroll.set)

# Bind the mouse wheel event to the canvas for scrolling
def on_mousewheel(event):
    news_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Bind the mouse wheel event to the entire application window
app.bind_all("<MouseWheel>", on_mousewheel)

# vertical separator
separator = ttk.Separator(app, orient='vertical')
separator.grid(row=2, column=4, rowspan=12, sticky='ns', padx=(30))

# space container
space_container = tk.Frame(app, borderwidth=1, relief="solid")
space_container.grid(row=2, column=5, sticky="snew")

space_label = tk.Label(space_container, text="Astronomy Picture of the Day", font=('Terminal', 10))
space_label.pack(side="top", fill="x")
    
apod_frame = tk.Frame(space_container, background="black", borderwidth=2, relief="solid")
apod_frame.pack(fill="both", expand=True, padx=2, pady=2)

apod_title = tk.Label(apod_frame, font=('Terminal', 10))
apod_title.pack(side="top", fill="x")

async def update_nasa():
    apod = await fetch_nasa()
    apod_title.config(text=f"{apod['title']}")
    response = urllib.request.urlopen(apod['url'])
    img_data = response.read()
    img = Image.open(io.BytesIO(img_data))
    
    def update_apod_size(event):
        width = event.width - 12
        height = event.height - 12
        update_apod_size.apod_img = img
        apod_img = update_apod_size.apod_img.resize((width, height))
        apod_icon = ImageTk.PhotoImage(apod_img)
        apod_label.config(image=apod_icon)
        apod_label.image = apod_icon
        
    apod_label = tk.Label(apod_frame)
    apod_label.pack(side="top", fill="both", expand=True)

    apod_label.bind("<Configure>", update_apod_size)
    
    app.after(30000, update_nasa)

async def update_rover():
    rover_image_url = await fetch_rover()
    response = urllib.request.urlopen(rover_image_url)
    img_data = response.read()
    img = Image.open(io.BytesIO(img_data))
    
    def update_rover_size(event):
        width = event.width - 12
        height = event.height - 12
        update_rover_size.rover_img = img
        rover_img = update_rover_size.rover_img.resize((width, height))
        rover_icon = ImageTk.PhotoImage(rover_img)
        rover_label.config(image=rover_icon)
        rover_label.image = rover_icon
        
    rover_label = tk.Label(rover_frame)
    rover_label.pack(side="top", fill="both", expand=True)

    rover_label.bind("<Configure>", update_rover_size)
    
    app.after(60000, update_rover)  # Update every 60 seconds

# Create a frame for the rover image
rover_frame = tk.Frame(space_container, borderwidth=2, relief="solid")
rover_frame.pack(fill="both", expand=True, padx=2, pady=2)

rover_label = tk.Label(rover_frame, text="Mars Rover Images", font=('Terminal', 10))
rover_label.pack(side="top", fill="x")

# Update modules
update_weather()
update_time()
update_process()
update_news()
asyncio.run(update_nasa())
asyncio.run(update_rover())

start_reloader()
app.mainloop()

