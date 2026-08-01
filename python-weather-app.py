#IMPORTING MODULE
import tkinter as tk
import requests

#API KEY (OPEN WEATHER MAP RECOMMANDED)
api_key = "API_KEY"  #ENTER YOUR API KEY HERE

#SERACH WEATHER DATA FUNCTION
def on_search():
    city = city_input.get()
#URL OF OPEN WEATHER MAP 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url , timeout=5)
#TO CONVERT JSON INTO PYTHON OBJECT
    data = response.json()
#TEMPERATION DATA
    temp = data["main"]["temp"]
#HUMIDITY DATA
    humidity = data["main"]["humidity"]
#DESCRIPTION DATA
    description = data["weather"][0]["description"].capitalize()

#TO SHOW DATA AT THE LABEL
    temp_label.config(text=f"Temperature: {temp}°C")
    humidity_label.config(text=f"Humidity: {humidity}%")
    desc_label.config(text=f"Condition: {description}")

#CREATING A GUI
root = tk.Tk()
root.title("PYTHON WEATHER")
root.geometry("400x300")

#HEADING
heading = tk.Label(
    root ,
    font=("areil" , 10 , "bold") ,
    text="ENTER A CITY NAME"
)
heading.pack(pady=10)

#CITY NAME INPUT
city_input = tk.Entry(
    root ,
    font=("areil" , 10 , "bold") ,
)
city_input.pack(pady=10)

#WEATHER SEARCH BUTTON 
enter_btn = tk.Button(
    root , 
    font=("areil" , 10 , "bold") ,
    text="ENTER" ,
    command=on_search
)
enter_btn.pack(pady=10)

#TEMPERATION DATA LABEL
temp_label = tk.Label(
     root ,
     font=("areil" , 10 , "bold") ,
     text="TEMPERATION:"
)
temp_label.pack(pady=10)

#HUMIDITY DATA LABEL
humidity_label = tk.Label(
     root ,
     font=("areil" , 10 , "bold") ,
     text="HUMIDITY:"
)
humidity_label.pack(pady=10)

#DESCRIPTION DATA LABEL
desc_label = tk.Label(
     root ,
     font=("areil" , 10 , "bold") ,
     text="DESCRIPTION;"
)
desc_label.pack(pady=10)

#CLOSING BUTTON
close_btn = tk.Button(
    root ,
    text="CLOSE" ,
    font=("areil" , 10 , "bold") ,
    command=root.destroy
)
close_btn.pack(
    pady=10 ,
    side="bottom"
)

root.mainloop()
