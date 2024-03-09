# BytesIO an in-memory buffer for binary data
from io import BytesIO
from tkinter import *
from random import randint
from tkinter import messagebox

# pip install captcha
from captcha.image import ImageCaptcha

image = ImageCaptcha(fonts=["./fonts/ChelseaMarketsr.ttf", "./fonts/DejaVuSanssr.ttf"])

GUI_tkinter = Tk()
photo = None  # to avoid Unbounding LocalError

l1 = Label(GUI_tkinter, height=100, width=200)
t1 = Text(GUI_tkinter, height=5, width=50)


# define generator image
def generate_image():
    # set the vars to global
    global random, photo

    random = str(randint(100000, 999999))
    data = image.generate(random)
    assert isinstance(data, BytesIO)
    image.write(random, "./captcha-image/output-captcha.png")
    photo = PhotoImage(file="./captcha-image/output-captcha.png")
    l1.config(image=photo, height=100, width=200)


def verify():
    x = t1.get("0.0", END).strip()

    if int(x) == int(random):
        messagebox.showinfo("Success", "Verified")
        generate_image()

    else:
        messagebox.showinfo("Alert", "Not Verified")
        generate_image()


b1 = Button(GUI_tkinter, text="Submit", command=verify)
b2 = Button(GUI_tkinter, text="Refresh", command=generate_image)

l1.pack()
t1.pack()
b1.pack()
b2.pack()

# to display image on app startup new window
generate_image()

GUI_tkinter.mainloop()
