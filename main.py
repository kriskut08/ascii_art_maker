from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image,ImageOps



"""
Képből ascii art generátor
nemtudom miért hasznos, de egy jó projekt
 ¯\_(ツ)_/¯


2021.12.19
qkristof.hu
"""



win = Tk()

#fájlok bekérése
def openImage():
    global inp
    global open_btn
    inp = filedialog.askopenfilename(title="Fájlok kiválasztása",
                                          filetypes=(("Kép ",
                                                      "*.jpg*"),("Kép","*.png*"),
                                                     ("all files",
                                                      "*.*")))
    name = inp.split("/")
    open_btn.configure(text=name[-1])

def openoutput():
    global output
    global output_btn
    output =filedialog.asksaveasfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))
    name = output.split("/")
    output_btn.configure(text=name[-1])

#a kép konvertálása
def convertImage(img, out):
    width = 100
    height = 100

    # a karakterek
    shades = "$@%#*/\|()1{}[]?o<>i!lI-_+~;:,"

    # a kép megnyitása, átméterezése, forgatása
    im = Image.open(img)
    im = im.convert("P", palette=Image.ADAPTIVE, colors=64)
    im = im.resize((width, height))
    im = ImageOps.grayscale(im)
    im = im.rotate(90)
    im = ImageOps.flip(im)

    text = ""
    for i in range(width):
        for j in range(height):
            text += shades[int(im.getpixel((i, j)) / 8.6)]
            text += shades[int(im.getpixel((i, j)) / 8.6)]
        text += "\n"

    # a "kép" fájlba írása
    out = open(out, "w+")
    out.write(text)
    out.close()
    showinfo("Kész!","A konvertálás sikeres volt!")


win.geometry("400x268")
win.title("Kép-ascii konverter")
win.resizable(False, False)
output=""
inp=""

open_btn = Button(win, text="Kép kiválasztása", command = lambda: openImage())
open_btn.pack()
output_btn = Button(win,text="Kimeneti fájl megnyitása",command = lambda: openoutput())
output_btn.pack()
convert =Button(win,text="Konvertálás",command = lambda: convertImage(inp,output)).pack()




win.mainloop()
