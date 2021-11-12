from tkinter import font,Label, Tk
#GENERAR IMAGEN CON UN REQUEST
import requests as req
import PIL
from PIL import Image
from io import BytesIO

#Show the image of the race
def show_image(url_image) -> None:
    try:
        print('Cargando imagen...')
        #get response
        response : any = req.get(url_image)
        #convert bytes to image
        image : Image  = Image.open(BytesIO(response.content))
        #show image
        image.show()
    except PIL.UnidentifiedImageError: 
        print('Image not available')




#Show information
def start(name, id_race, description, roles) -> None:
    
    print('Trabajando hilo...')
    root = Tk()
    root.title(name)
    root.geometry('500x500')
    #RACE
    label_titulo : Label = Label(
        root,
        width=40,
        height=1,
        text=name,
        font=font.Font(size=15)
    ).place(x=50,y=50)
    #ID
    label_search : Label = Label(
        root,
        width=40,
        height=1,
        text=id_race,
        font=font.Font(size=15)
    ).place(x=60,y=100)
    #ROLES
    label_search : Label = Label(
        root,width=40,
        height=1,
        text=roles,
        font=font.Font(size=15)
    ).place(x=60,y=150)
    #DESCRIPTION OF THE RACE
    label_search : Label = Label(
        root,
        text=description,
        font=font.Font(size=12),
        wraplength=390 #This put a maxlenght to the label so the text doesn't overflow
    ).place(x=80,y=200)
    
    root.mainloop()