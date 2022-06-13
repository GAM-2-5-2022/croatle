import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from random import randint

def checking():
    text=entry.get()
    global x
    global guessval
    global values
    zupanije = ['Primorsko-goranska županija', 'Istarska županija', 'Grad Zagreb', 'Zagrebačka županija', 'Zadarska županija', 'Šibensko-kninska županija', 'Splitsko-dalmatinska županija', 'Dubrovačko-neretvanska županija', 'Ličko-senjska županija', 'Karlovačka županija', 'Sisačko-moslavačka županija', 'Krapinsko-zagorska županija', 'Varaždinska županija', 'Međimurska županija', 'Koprivničko-križevačka županija', 'Bjelovarsko-bilogorska županija', 'Virovitičko-podravska županija', 'Požeško-slavonska županija', 'Brodsko-posavska županija', 'Osječko-baranjska županija', 'Vukovarsko-srijemska županija']
    for i in range(0, 21):
        accept = False
        if x < 5:
            if zupanije[i].lower() == text.lower():
                guessval[x] = zupanije[i]
                accept = True
                break
    if x == 0 and accept == True:
        if text.lower() == values[1].lower():
            text_box1 = tk.Text(gui, height=1, width=50, font=('Arial', 11, 'bold'), bg='#52FF52', fg='#000000')
            text_box1.insert('end', guessval[x])
            text_box1.config(state='disabled')
            text_box1.grid(row=3, column = 0, columnspan = 2, pady=2)
            button.config(state='disabled')
            notice = tk.Label(gui, text='Pogodili ste u 1. pokušaju!', font=('Arial', 16, 'bold'))
            notice.grid(row=10, column=0, columnspan = 2, pady=20, ipadx=50)
        else:
            text_box1 = tk.Text(gui, height=1, width=50, font=('Arial', 11, 'bold'), bg='#FF6A6A', fg='#000000')
            text_box1.insert('end', guessval[x])
            text_box1.config(state='disabled')
            text_box1.grid(row=3, column = 0, columnspan = 2, pady=2)
    if x == 1 and accept == True:
        if text.lower() == values[1].lower():
            text_box2 = tk.Text(gui, height=1, width=50, font=('Arial', 11, 'bold'), bg='#52FF52', fg='#000000')
            text_box2.insert('end', guessval[x])
            text_box2.config(state='disabled')
            text_box2.grid(row=4, column = 0, columnspan = 2, pady=2)
            button.config(state='disabled')
            notice = tk.Label(gui, text='Pogodili ste u 2. pokušaju!', font=('Arial', 16, 'bold'))
            notice.grid(row=10, column=0, columnspan = 2, pady=20, ipadx=50)
        else:
            text_box2 = tk.Text(gui, height=1, width=50, font=('Arial', 11, 'bold'), bg='#FF6A6A', fg='#000000')
            text_box2.insert('end', guessval[x])
            text_box2.config(state='disabled')
            text_box2.grid(row=4, column = 0, columnspan = 2, pady=2)
    if x == 2 and accept == True:
        if text.lower() == values[1].lower():
            text_box3 = tk.Text(gui, height=1, width=50, font=('Arial', 11, 'bold'), bg='#52FF52', fg='#000000')
            text_box3.insert('end', guessval[x])
            text_box3.config(state='disabled')
            text_box3.grid(row=5, column = 0, columnspan = 2, pady=2)
            button.config(state='disabled')
            notice = tk.Label(gui, text='Pogodili ste u 3. pokušaju!', font=('Arial', 16, 'bold'))
            notice.grid(row=10, column=0, columnspan = 2, pady=20, ipadx=50)
        else:
            text_box3 = tk.Text(gui, height=1, width=50, font=('Arial', 11, 'bold'), bg='#FF6A6A', fg='#000000')
            text_box3.insert('end', guessval[x])
            text_box3.config(state='disabled')
            text_box3.grid(row=5, column = 0, columnspan = 2, pady=2)
    if x == 3 and accept == True:
        if text.lower() == values[1].lower():
            text_box4 = tk.Text(gui, height=1, width=50, font=('Arial', 11, 'bold'), bg='#52FF52', fg='#000000')
            text_box4.insert('end', guessval[x])
            text_box4.config(state='disabled')
            text_box4.grid(row=6, column = 0, columnspan = 2, pady=2)
            button.config(state='disabled')
            notice = tk.Label(gui, text='Pogodili ste u 4. pokušaju!', font=('Arial', 16, 'bold'))
            notice.grid(row=10, column=0, columnspan = 2, pady=20, ipadx=50)
        else:
            text_box4 = tk.Text(gui, height=1, width=50, font=('Arial', 11, 'bold'), bg='#FF6A6A', fg='#000000')
            text_box4.insert('end', guessval[x])
            text_box4.config(state='disabled')
            text_box4.grid(row=6, column = 0, columnspan = 2, pady=2)
    if x == 4 and accept == True:
        if text.lower() == values[1].lower():
            text_box5 = tk.Text(gui, height=1, width=50, font=('Arial', 11, 'bold'), bg='#52FF52', fg='#000000')
            text_box5.insert('end', guessval[x])
            text_box5.config(state='disabled')
            text_box5.grid(row=7, column = 0, columnspan = 2, pady=2)
            notice = tk.Label(gui, text='Pogodili ste u 5. pokušaju!', font=('Arial', 16, 'bold'))
            notice.grid(row=10, column=0, columnspan = 2, pady=20, ipadx=50)
        else:
            text_box5 = tk.Text(gui, height=1, width=50, font=('Arial', 11, 'bold'), bg='#FF6A6A', fg='#000000')
            text_box5.insert('end', guessval[x])
            text_box5.config(state='disabled')
            text_box5.grid(row=7, column = 0, columnspan = 2, pady=2)
            notice = tk.Label(gui, text='Točan odgovor je: %s'%values[1], font=('Arial', 16, 'bold'))
            notice.grid(row=10, column=0, columnspan = 2, pady=20, ipadx=50)
        button.config(state='disabled')
    if accept == True:
        x += 1
    return

# guesses left (if the value goes up to 5, the game should show the answer and not allow further input
x = 0    
# random selection
n = randint(0,20)
# choose image and solution based on random selection (please don't go checking images, thanks :) )
if n == 0:
    values = ['images/pgz.png', 'Primorsko-goranska županija']
if n == 1:
    values = ['images/iz.png', 'Istarska županija']
if n == 2:
    values = ['images/gz.png', 'Grad Zagreb']
if n == 3:
    values = ['images/zz.png', 'Zagrebačka županija']
if n == 4:
    values = ['images/zdz.png', 'Zadarska županija']
if n == 5:
    values = ['images/sz.png', 'Šibensko-kninska županija']
if n == 6:
    values = ['images/sdz.png', 'Splitsko-dalmatinska županija']
if n == 7:
    values = ['images/dnz.png', 'Dubrovačko-neretvanska županija']
if n == 8:
    values = ['images/lsz.png', 'Ličko-senjska županija']
if n == 9:
    values = ['images/kz.png', 'Karlovačka županija']
if n == 10:
    values = ['images/smz.png', 'Sisačko-moslavačka županija']
if n == 11:
    values = ['images/kzz.png', 'Krapinsko-zagorska županija']
if n == 12:
    values = ['images/vz.png', 'Varaždinska županija']
if n == 13:
    values = ['images/mz.png', 'Međimurska županija']
if n == 14:
    values = ['images/kkz.png', 'Koprivničko-križevačka županija']
if n == 15:
    values = ['images/bbz.png', 'Bjelovarsko-bilogorska županija']
if n == 16:
    values = ['images/vpz.png', 'Virovitičko-podravska županija']
if n == 17:
    values = ['images/psz.png', 'Požeško-slavonska županija']
if n == 18:
    values = ['images/bpz.png', 'Brodsko-posavska županija']
if n == 19:
    values = ['images/obz.png', 'Osječko-baranjska županija']
if n == 20:
    values = ['images/vsz.png', 'Vukovarsko-srijemska županija']
    
gui = tk.Tk()
gui.geometry("750x750")
gui.grid_columnconfigure(0, weight=1)
gui.wm_title('Croatle')
title = tk.Label(gui, text='Croatle', font=('Arial', 25, 'bold'))
title.grid(row=1, column = 0, columnspan = 2)

img= Image.open(values[0])
resize_img = img.resize((400,300))
image_zup = ImageTk.PhotoImage(resize_img)

img_zup = tk.Label(gui, image = image_zup)
img_zup.grid(row=2, column = 0, columnspan = 2)

guessval = ['', '', '', '', '']

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

entry = tk.Entry(gui, font=('Arial', 11, 'bold'))
entry.grid(row=8, column=0, columnspan = 2, pady=20, ipadx=50)
button = ttk.Button(gui, text="Enter", command=checking)
button.grid(row=9, column=0, columnspan = 2, pady=20, ipadx=50)

gui.mainloop()
