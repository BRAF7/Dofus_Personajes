from tkinter import font,Label,Button,Entry, Tk
import tkinter as tk

from race_information import run

# search : str
names : str

def connect_back(search):
    #Tkinter automatically convert everything you put in str
    assert search != str, "search must be a string"
    search_lower = search.lower()
    print(search)
    run(search_lower)




def start(names):
    root = Tk()
    root.title('Buscar razas')
    root.geometry('1250x500')

    label_titulo = Label(root,width=40,height=1,text='Razas',font=font.Font(size=15)).place(x=350,y=180)
    for i in names:
        et = tk.Label(root, text=i, font=font.Font(size=12))
        et.pack(side='left',ipadx=5, ipady=20 )
        et.bind("<Button-1>", lambda event, label=et: prueba(event, label))

    label_search = Label(root,width=40,height=1,text='Buscar raza',font=font.Font(size=15)).place(x=360,y=50)
    entry_search = Entry(root,width=20)
    entry_search['font'] = font.Font(size=12)
    entry_search.place(x=480,y=90)
    btn_search = Button(root,width=16,height=1,text='Buscar',font=font.Font(size=12),command=lambda: connect_back(entry_search.get())).place(x=500,y=120)

    root.mainloop()
    




def prueba(event,label):
    print(event)
    print(label["text"])