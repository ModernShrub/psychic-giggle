from tkinter import *
import requests as r
import json as j

root = Tk()
root.title("Country-capital")
root.geometry("350x400")

head = Label(root, text="Country Capitals",font=("Arial", 20, "bold"))
head.place(relx=0.4,rely=0.2,anchor=CENTER)

capinp = Entry(root)
capinp.place(relx=0.27,rely=0.3,anchor=CENTER)

contry = Label(root,text="Country- ",font=("Arial", 10, "bold"))
contry.place(relx=0.17,rely=0.5,anchor=CENTER)

contin = Label(root,text="Continent- ",font=("Arial", 10, "bold"))
contin.place(relx=0.18,rely=0.6,anchor=CENTER)

pop = Label(root,text="Population- ",font=("Arial", 10, "bold"))
pop.place(relx=0.19,rely=0.7,anchor=CENTER)

lang = Label(root,text="Language- ",font=("Arial", 10, "bold"))
lang.place(relx=0.19,rely=0.8,anchor=CENTER)

area = Label(root,text="Area- ",font=("Arial", 10, "bold"))
area.place(relx=0.14,rely=0.9,anchor=CENTER)

def getcity():
    global capinp
    
    citname = capinp.get()
    details = r.get("https://restcountries.com/v2/capital/" + str(citname))
    print("data got")
    apiout = j.loads(details.content)
    contry['text'] = "Country- " + str(apiout[0]['name'])
    contin['text'] = "Cotinent- " + str(apiout[0]['region'])
    pop['text'] = "Population- " + str(apiout[0]['population'])
    lang['text'] = "Language- " + str(apiout[0]['languages'][0]['name'])
    area['text'] = "Area- " + str(apiout[0]['area'])

btn = Button(root,text="Get details",command=getcity)
btn.place(relx=0.2,rely=0.4,anchor=CENTER)
root.mainloop()