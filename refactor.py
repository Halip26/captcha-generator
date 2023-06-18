from io import BytesIO
from random import randint
from tkinter import *
from tkinter import messagebox

from captcha.image import ImageCaptcha


def generate_captcha(image: ImageCaptcha, random: str,
                     output_path: str = 'captcha_image/output.png') -> None:
    data = image.generate(random)
    if not isinstance(data, BytesIO):
        raise TypeError(
            f"data is of type {type(data)} and not {BytesIO} as expected")
    image.write(random, output_path)


def verify(random: str, entry) -> None:
    x = entry.get("0.0", END)
    if int(x) == int(random):
        messagebox.showinfo("Success", "Verified")
    else:
        messagebox.showinfo("Alert", "Not verified")
        refresh()


def refresh(random: str = str(randint(100000, 999999)), image: ImageCaptcha = ImageCaptcha(
            fonts=['./fonts/ChelseaMarketsr.ttf', './fonts/DejaVuSanssr.ttf']),
            img_output_path: str = 'captcha_image/output.png') -> None:
    generate_captcha(image, random, img_output_path)
    photo = PhotoImage(file=img_output_path)
    l1.config(image=photo, height=100, width=200)
    l1.update()


image = ImageCaptcha(
    fonts=['./fonts/ChelseaMarketsr.ttf', './fonts//DejaVuSanssr.ttf'])

random = str(randint(100000, 999999))
generate_captcha(image, random)

root = Tk()
l1 = Label(root, image=PhotoImage(
    file='captcha_image/output.png'), height=100, width=200)
entry = Text(root, height=5, width=50)
submit = Button(root, text="Submit", command=lambda: verify(random, entry))
refresh_btn = Button(root, text="Refresh",
                     command=lambda: refresh(random, image))
l1.pack()
entry.pack()
submit.pack()
refresh_btn.pack()
root.mainloop()
