
# #GENERAR IMAGEN CON UN REQUEST
# import requests as req
# from PIL import Image
# from io import BytesIO
# #CODIGO
# response = req.get('https://s.ankama.com/www/static.ankama.com/dofus/renderer/look/7b317c31312c323032307c313d31363130333737352c323d363833333138342c333d31333636313139302c343d31333636313139302c353d363936333436327c3132357d/full/1/250_250-10_100.png')
# image = Image.open(BytesIO(response.content))
# image.show()

import tkinter as tk
marco = tk.Tk()
marco.geometry("450x200")

for i in range(10):
    et = tk.Label(marco, text=f"Hola {i}")
    et.pack()
    et.bind("<Button-1>", lambda event, num=i, label=et: prueba(event, num, label))

def prueba(event, num, label):
    print(event)
    print(num)
    print(label["text"])

marco.mainloop()