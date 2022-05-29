import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
 

gui = tk.Tk()
gui.geometry("1024x768")
gui.grid_columnconfigure(0, weight=1)
gui.wm_title('Croatle')
title = tk.Label(gui, text='Croatle', font=('Segoe UI', 25, 'bold'))
title.grid(row=1, column = 0, columnspan = 2)

# image import
img= Image.open("images/test.png")
resize_img = img.resize((400,300), Image.ANTIALIAS)
image_zup = ImageTk.PhotoImage(resize_img)

# image
img_zup = tk.Label(gui, image = image_zup)
img_zup.grid(row=2, column = 0, columnspan = 2)

# guess values
guess1 = 'test1'
guess2 = ''
guess3 = ''
guess4 = ''
guess5 = ''

# guesses already done (should change upon a guess)
text_box1 = tk.Text(gui, height=1, width=50)
text_box1.insert('end', guess1)
text_box1.config(state='disabled')
text_box1.grid(row=3, column = 0, columnspan = 2)

text_box2 = tk.Text(gui, height=1, width=50)
text_box2.insert('end', guess2)
text_box2.config(state='disabled')
text_box2.grid(row=4, column = 0, columnspan = 2)

text_box3 = tk.Text(gui, height=1, width=50)
text_box3.insert('end', guess3)
text_box3.config(state='disabled')
text_box3.grid(row=5, column = 0, columnspan = 2)

text_box4 = tk.Text(gui, height=1, width=50)
text_box4.insert('end', guess4)
text_box4.config(state='disabled')
text_box4.grid(row=6, column = 0, columnspan = 2)

text_box5 = tk.Text(gui, height=1, width=50)
text_box5.insert('end', guess5)
text_box5.config(state='disabled')
text_box5.grid(row=7, column = 0, columnspan = 2)

gui.grid_rowconfigure(8, weight=1)
# guess input
guess = tk.Entry(gui)
guess.grid(row=8, column = 0, columnspan = 1)

guessbtn = tk.Button(gui, text='Pretpostavi')
guessbtn.grid(row=8, column = 1, columnspan = 1)

gui.mainloop()
