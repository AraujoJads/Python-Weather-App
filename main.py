import requests as rq
import tkinter as tk
from tkinter import ttk


api_key = "4c33132535109438d25b8fc62f47c1bf"

def getInput():
    url = "http://api.openweathermap.org/geo/1.0/direct?q={}&limit=5&appid={}".format(entrada.get(),api_key)

    response = rq.get(url)

    if response.status_code == 200:
        dados = response.json()
        print(dados)

        latitude = dados[0]['lat']
        longitude = dados[0]['lon']

        url_weather = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(latitude,
                                                                                                      longitude,
                                                                                                      api_key)

        response = rq.get(url_weather)

        if response.status_code == 200:
            dados = response.json()
            print(dados)
            result = f"{(dados['main']['temp'] - 273.15):.2f}"
            ttk.Label(root, text=result).grid(column=0,row=2)
            tk.mainloop()



    else:
        print(response.status_code)

root = tk.Tk()
root.geometry('500x500')
root.title('Weather_App')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
ttk.Style().theme_use('clam')
ttk.Label(root, text='Weather App').grid(column=0, row=0)

resultado = ttk.Label(root, text='Insira a Cidade').grid(column=0, row=1)

entrada = ttk.Entry(root)
entrada.grid(column=0, row=3)

button = ttk.Button(root, text='Send',command=getInput).grid(column=0, row=4)


tk.mainloop()



