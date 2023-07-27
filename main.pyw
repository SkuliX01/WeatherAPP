import customtkinter
import requests

def get_weather(city):
    api_key = ""
    url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric".format(city=city, api_key=api_key)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def mainProgram():
    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme('green')
    def LookUP():
        city = postalCode.get()
        weather = get_weather(city)
        if weather is not None:
            pressure = int(weather["main"]["pressure"])
            cityName.pack(padx=10)
            cityName.configure(text="City :  {}".format(city))
            cityTemp.pack(padx=10)
            cityTemp.configure(text="Temprature : {}".format(weather["main"]["temp"]))
            cityPressure.pack(padx=10)
            cityPressure.configure(text="Pressure : {}".format(pressure) + " hPa")
            cityHumidity.pack(padx=10)
            cityHumidity.configure(text="Humidity : {}".format(weather["main"]["humidity"]) + " %")
        else:
            cityError.configure(text="City not found : {}.".format(city))
            cityError.pack(pady=155)
            cityError.after(3500,cityError.destroy)
    def clearweather():
        cityName.destroy()
        cityHumidity.destroy()
        cityPressure.destroy()
        cityTemp.destroy()
    root = customtkinter.CTk()
    root.title("Weather App")
    root.geometry("315x450")
    root.resizable(False,False)
    root.iconbitmap("cloud.ico")
    info = customtkinter.CTkLabel(master=root,text="Weather App.",font=('Helvetica',22))
    info.pack()
    postalCode = customtkinter.CTkEntry(master=root,placeholder_text="City Name.",width=155,height=35,corner_radius=12,font=('Helvetica',16))
    postalCode.pack(pady=5,padx=5)
    lookUP = customtkinter.CTkButton(master=root,text="Look UP",width=135,height=25,corner_radius=10,font=('Helvetica',14),command=LookUP)
    lookUP.pack(pady=5,padx=5)
    clearbutton = customtkinter.CTkButton(master=root,text="Clear",width=135,height=25,corner_radius=10,font=('Helvetica',14),command=clearweather)
    clearbutton.pack(pady=10,padx=75)
    global cityTemp
    global cityName
    global cityPressure
    global cityHumidity
    cityName = customtkinter.CTkLabel(master=root,font=('Helvetica',16))
    cityTemp = customtkinter.CTkLabel(master=root,font=('Helvetica',16))
    cityPressure = customtkinter.CTkLabel(master=root,font=('Helvetica',16))
    cityHumidity = customtkinter.CTkLabel(master=root,font=('Helvetica',16))
    cityError = customtkinter.CTkLabel(master=root,font=('Helvetica',16))
    root.mainloop()
mainProgram()
