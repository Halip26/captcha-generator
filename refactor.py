from io import BytesIO
from tkinter import *
from random import randint
from tkinter import messagebox
from captcha.image import ImageCaptcha

image = ImageCaptcha(
    fonts=['./fonts/ChelseaMarketsr.ttf', './fonts/DejaVuSanssr.ttf'])


def generate_image():
    global random, photo
    random = str(randint(100000, 999999))
    data = image.generate(random)
    assert isinstance(data, BytesIO)
    image.write(random, './captcha_image/output.png')
    photo = PhotoImage(file='./captcha_image/output.png')
    l1.config(image=photo, height=100, width=200)


def verify():
    x = t1.get("0.0", END).strip()
    if (int(x) == int(random)):
        messagebox.showinfo("sucsess", "verified")
        generate_image()
    else:
        messagebox.showinfo("Alert", "Not verified")
        generate_image()


root = Tk()
photo = None  # To avoid UnboundLocalError

l1 = Label(root, height=100, width=200)
t1 = Text(root, height=5, width=50)
b1 = Button(root, text="submit", command=verify)
b2 = Button(root, text="refresh", command=generate_image)

l1.pack()
t1.pack()
b1.pack()
b2.pack()

generate_image()  # To display image on application startup

root.mainloop()
