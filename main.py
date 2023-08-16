from io import BytesIO
from tkinter import *
from random import randint
from tkinter import messagebox
from captcha.image import ImageCaptcha

image = ImageCaptcha(fonts=["./fonts/ChelseaMarketsr.ttf", "./fonts/DejaVuSanssr.ttf"])


# define generator image
def generate_image():
    global random, photo
    random = str(randint(100000, 999999))
    data = image.generate(random)
    assert isinstance(data, BytesIO)
    image.write(random, "./captcha_image/output.png")
    photo = PhotoImage(file="./captcha_image/output.png")
    l1.config(image=photo, height=100, width=200)


# define verify
def verify():
    """
    Mengambil input teks dari elemen GUI t1
    dan menghapus spasi di awal dan akhir input.
    Input ini akan disimpan dalam variabel x
    """
    x = t1.get("0.0", END).strip()
    if int(x) == int(random):
        messagebox.showinfo("Success", "verified")
        generate_image()
    else:
        messagebox.showinfo("Alert", "Not verified")
        generate_image()


root = Tk()
photo = None  # To avoid UnboundLocalError

l1 = Label(root, height=100, width=200)
t1 = Text(root, height=5, width=50)
b1 = Button(root, text="Submit", command=verify)
b2 = Button(root, text="Refresh", command=generate_image)

l1.pack()
t1.pack()
b1.pack()
b2.pack()

# To display image on application startup
generate_image()

root.mainloop()
