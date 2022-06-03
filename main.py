import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def get_value():
    text=entry.get()
    a = tk.Label(gui, text=text).grid(row=10)
   
gui = tk.Tk()
gui.geometry("1024x768")
gui.grid_columnconfigure(0, weight=1)
gui.wm_title('Croatle')
title = tk.Label(gui, text='Croatle', font=('Segoe UI', 25, 'bold'))
title.grid(row=1, column = 0, columnspan = 2)

# image import
img= Image.open("images/pgz.png")
resize_img = img.resize((400,300), Image.ANTIALIAS)
image_zup = ImageTk.PhotoImage(resize_img)

# image
img_zup = tk.Label(gui, image = image_zup)
img_zup.grid(row=2, column = 0, columnspan = 2)

# guess values
guessval = ['', '', '', '', '']

# guesses already done (should change upon a guess)
text_box1 = tk.Text(gui, height=1, width=50)
text_box1.insert('end', guessval[0])
text_box1.config(state='disabled')
text_box1.grid(row=3, column = 0, columnspan = 2, pady=2)

text_box2 = tk.Text(gui, height=1, width=50)
text_box2.insert('end', guessval[1])
text_box2.config(state='disabled')
text_box2.grid(row=4, column = 0, columnspan = 2, pady=2)

text_box3 = tk.Text(gui, height=1, width=50)
text_box3.insert('end', guessval[2])
text_box3.config(state='disabled')
text_box3.grid(row=5, column = 0, columnspan = 2, pady=2)

text_box4 = tk.Text(gui, height=1, width=50)
text_box4.insert('end', guessval[3])
text_box4.config(state='disabled')
text_box4.grid(row=6, column = 0, columnspan = 2, pady=2)

text_box5 = tk.Text(gui, height=1, width=50)
text_box5.insert('end', guessval[4])
text_box5.config(state='disabled')
text_box5.grid(row=7, column = 0, columnspan = 2, pady=2)

entry = tk.Entry(gui)
entry.grid(row=8, column=0, columnspan = 2, pady=20, ipadx=50)
button= ttk.Button(gui, text="Enter", command=get_value)
button.grid(row=9, column=0, columnspan = 2, pady=20, ipadx=50)

gui.mainloop()
