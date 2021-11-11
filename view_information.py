from tkinter import font,Label,Button,Entry, Tk
import tkinter as tk
#GENERAR IMAGEN CON UN REQUEST
import requests as req
import PIL
from PIL import Image
from io import BytesIO


def show_image(url_image):
    try:
        response = req.get(url_image)
        image = Image.open(BytesIO(response.content))
        image.show()
    except PIL.UnidentifiedImageError: 
        print('Image not available')
    




def start(name, id_race, description, roles):
    root = Tk()
    root.title(name)
    root.geometry('500x500')
    #RACE
    label_titulo = Label(root,width=40,height=1,text=name,font=font.Font(size=15)).place(x=50,y=50)
    #ID
    label_search = Label(root,width=40,height=1,text=id_race,font=font.Font(size=15)).place(x=60,y=100)
    #ROLES
    label_search = Label(root,width=40,height=1,text=roles,font=font.Font(size=15)).place(x=60,y=150)
    #DESCRIPTION OF THE RACE
    label_search = Label(root,text=description,font=font.Font(size=12), wraplength=390).place(x=80,y=200)
    
    root.mainloop()