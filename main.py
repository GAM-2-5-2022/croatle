import tkinter as tk
from tkinter.ttk import Label
from PIL import Image, ImageTk
 

gui = tk.Tk()
gui.geometry("1024x768")
gui.wm_title('Croatle')
title = Label(gui, text='Croatle', font=('Segoe UI', 25, 'bold'))
title.pack(ipadx=10, ipady=10)

img= Image.open("images/test.png")
resize_img = img.resize((400,300), Image.ANTIALIAS)
image_zup = ImageTk.PhotoImage(resize_img)


img_zup = tk.Label(gui, image = image_zup)
img_zup.pack()
gui.mainloop()
