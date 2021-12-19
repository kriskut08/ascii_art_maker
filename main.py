from PIL import Image, ImageOps

"""
Képből ascii art generátor
nemtudom miért hasznos, de egy jó projekt
 ¯\_(ツ)_/¯


2021.12.19
qkristof.hu
"""



width = 100
height = 100

#a karakterek
shades = "$@%#*/\|()1{}[]?o<>i!lI-_+~;:,"

#a kép megnyitása, átméterezése, forgatása
im = Image.open("test.jpg")
im = im.convert("P", palette=Image.ADAPTIVE, colors=64)
im = im.resize((width,height))
im = ImageOps.grayscale(im)
im = im.rotate(90)
im = ImageOps.flip(im)



#a kép konvertálása
text = ""
for i in range(width):
    for j in range(height):
        text += shades[int(im.getpixel((i, j)) / 8.6)]
        text += shades[int(im.getpixel((i, j)) / 8.6)]
    text += "\n"


# a "kép" fájlba írása
out = open("output.txt","w+")
out.write(text)
out.close()


