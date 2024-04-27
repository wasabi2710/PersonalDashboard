import tkinter as tk
import time
from datetime import datetime
from openweather import fetch_weather_data
from news import fetch_global_news
from processing import get_system_resources

#weather
def update_weather():
    weather_data = fetch_weather_data()
    label_city.config(text=f"{weather_data['city_name']}".upper(), fg="black", bg="white")
    label_description.config(text=f"{weather_data['weather_description']}".upper(), fg="black", bg="white")
    label_wind_speed.config(text=f"{weather_data['wind_speed']} km/h", fg="black", bg="white")
    label_temp.config(text=f"{weather_data['temperature_celsius']:.2f}°C", fg="black", bg="white")
    
    #update
    app.after(60000, update_weather) 
    
#clock
def update_time():
    current_time = time.strftime("%H:%M:%S %p")
    clock_label.config(text=current_time, fg="green", bg="black")
    today = datetime.today()
    formatted_date = today.strftime('%a, %d - %B - %Y')
    date_label.config(text=f"{formatted_date}", fg="green", bg="black")
        
    #update
    app.after(1000, update_time)
    
#process
def update_process():
    process = get_system_resources()
    cpu_label.config(text=f"{process['cpu_percent']} %".upper(), fg="black", bg="white")
    ram_label.config(text=f"{process['memory_percent']} %".upper(), fg="black", bg="white")
    
    #update
    app.after(2000, update_process)

# main window config
app = tk.Tk()
app.title("MyDashboard")
app.configure(background="black", padx=10, pady=10) # Added padding to the root window
app.resizable(0,0)

# Configure rows and columns to expand
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# icon
city_icon = "\U0001F4CD" 
cloud_icon = "\U000026C8"     
wind_icon = "\U0001F4A8"  
temp_icon = "\U0001F321" 
news_icon = "\U0001F4F0" 
cpu_icon = "\U0001F5A5"
ram_icon = "\U0001F4BE"
search_icon_left = '\U0001F50D'  

# clock info
clock_label = tk.Label(app, font=("Fixedsys", 30), fg="green", bg="black", padx=20, pady=20, borderwidth=2, relief="solid")
clock_label.grid(row=1, column=0, sticky='ew')
date_label = tk.Label(app, font=("Fixedsys", 30), fg="green", bg="black", padx=20, pady=20, borderwidth=2, relief="solid")
date_label.grid(row=0, column=0, sticky='ew')

# weather info
weather_frame = tk.Frame(app, borderwidth=1, relief="solid", background="white")
weather_frame.grid(row=0, column=1, sticky='nsew')

city_label = tk.Label(weather_frame, text=city_icon, font=("Courier", 28), fg='purple', bg="white") # Changed icon color to purple and set bg to white
city_label.pack(side='left', padx=2, pady=2)
label_city = tk.Label(weather_frame, text="", font=("Fixedsys", 18), fg="black", bg="white")
label_city.pack(side='left', padx=10, pady=10)

cloud_label = tk.Label(weather_frame, text=cloud_icon, font=("System", 28), fg='blue', bg="white") # Changed icon color to blue and set bg to white
cloud_label.pack(side='left', padx=2, pady=2)
label_description = tk.Label(weather_frame, text="", font=("Fixedsys", 18), fg="black", bg="white")
label_description.pack(side='left', padx=10, pady=10)

wind_label = tk.Label(weather_frame, text=wind_icon, font=("System", 28), fg='red', bg="white") # Changed icon color to red and set bg to white
wind_label.pack(side='left', padx=2, pady=2)
label_wind_speed = tk.Label(weather_frame, text="", font=("Fixedsys", 18), fg="black", bg="white")
label_wind_speed.pack(side='left', padx=10, pady=10)

temp_label = tk.Label(weather_frame, text=temp_icon, font=("System", 28), fg='yellow', bg="white") # Changed icon color to yellow and set bg to white
temp_label.pack(side='left', padx=2, pady=2)
label_temp = tk.Label(weather_frame, text="", font=("Fixedsys", 18), fg="black", bg="white")
label_temp.pack(side='left', padx=10, pady=10)

# processing info
process_frame = tk.Frame(app, borderwidth=1, relief="solid", background="white")
process_frame.grid(row=1, column=1, sticky='nsew')

cpu = tk.Label(process_frame, text=cpu_icon, font=("Fixedsys", 28), fg='green', bg="white") # Changed icon color to green and set bg to white
cpu.pack(side='left', padx=2 ,pady=2)
cpu_label = tk.Label(process_frame, font=("Fixedsys", 18), fg="black", bg="white")
cpu_label.pack(side='left', padx=10, pady=10)

ram = tk.Label(process_frame, text=ram_icon, font=("Fixedsys", 28), fg='orange', bg="white") # Changed icon color to orange and set bg to white
ram.pack(side='left', padx=2, pady=2)
ram_label = tk.Label(process_frame, font=("Fixedsys", 18), fg="black", bg="white")
ram_label.pack(side='left', padx=10, pady=10)

#update modules
update_weather()
update_time()
update_process()

app.mainloop()
