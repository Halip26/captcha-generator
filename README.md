# Captcha Generator

This Python code generates a captcha image and allows users to verify their input.

The code imports BytesIO from the io library, tkinter, randint function from the random library, messagebox from tkinter to display messages, and the ImageCaptcha function from the captcha.image library.

The code uses the ImageCaptcha function to generate captcha image using a random number and saves it as a PNG file in the captcha_image directory.

The GUI components are created using the Tk function from tkinter. The GUI contains a label, text box for user input, and two buttons, one to submit the input and the other to refresh the captcha image.

When the user submits an input, the code verifies if the input is the same as the one shown in the captcha image. If the input is verified, the code shows a success message; otherwise, it shows a message alerting the user that the input is incorrect.

To run the code, open it in an IDE or text editor and run it. The captcha image will be displayed along with the user input box and buttons. Enter the captcha shown in the image into the input box and click submit to verify. Below is the code:

```python
from io import BytesIO
from tkinter import *
from random import randint
from tkinter import messagebox
from captcha.image import ImageCaptcha

image = ImageCaptcha(fonts=["./fonts/ChelseaMarketsr.ttf", "./fonts/DejaVuSanssr.ttf"])

```

```python
# define generator image
def generate_image():
    global random, photo
    random = str(randint(100000, 999999))
    data = image.generate(random)
    assert isinstance(data, BytesIO)
    image.write(random, "./captcha_image/output.png")
    photo = PhotoImage(file="./captcha_image/output.png")
    l1.config(image=photo, height=100, width=200)

```

## Explanations of generate image

Kode di atas adalah fungsi generate_image() yang digunakan untuk menghasilkan gambar captcha. Berikut adalah penjelasan dari setiap baris kode:

def generate_image(): - Mendefinisikan fungsi generate_image().
global random, photo - Mendeklarasikan variabel random dan photo sebagai variabel global.
random = str(randint(100000, 999999)) - Menghasilkan angka acak antara 100000 hingga 999999 dan mengkonversinya menjadi string. Angka acak ini akan digunakan sebagai identitas unik untuk gambar captcha.
data = image.generate(random) - Menghasilkan data gambar captcha menggunakan identitas unik yang dihasilkan sebelumnya dan menyimpannya di variabel data.
assert isinstance(data, BytesIO) - Memastikan bahwa data adalah objek BytesIO.
image.write(random, "./captcha_image/output.png") - Menyimpan gambar captcha dengan nama file output.png di direktori /captcha_image/.
photo = PhotoImage(file="./captcha_image/output.png") - Membaca gambar captcha yang baru saja disimpan ke dalam objek PhotoImage dan menyimpannya di variabel photo.
l1.config(image=photo, height=100, width=200) - Mengatur atribut image, height, dan width dari objek l1 (sebuah elemen GUI) dengan nilai yang sesuai dari gambar captcha yang telah dibaca.

Kode di atas akan menghasilkan sebuah gambar captcha dan mengatur tampilan gambar tersebut di elemen GUI l1 dengan tinggi 100 dan lebar 200.

```python
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

```

## Explanations of function verify()

Kode di atas adalah fungsi verify() yang digunakan untuk memverifikasi input dari pengguna terhadap angka acak yang dihasilkan sebelumnya.

Berikut adalah penjelasan dari setiap baris kode:

def verify(): - Mendefinisikan fungsi verify(). x = t1.get("0.0", END).strip() - Mengambil input teks dari elemen GUI t1 dan menghapus spasi di awal dan akhir input. Input ini akan disimpan dalam variabel x. if int(x) == int(random): - Memeriksa apakah nilai x yang diinputkan oleh pengguna sama dengan nilai random yang dihasilkan sebelumnya. Kedua nilai ini dikonversi menjadi tipe data integer sebelum dibandingkan. messagebox.showinfo("Success", "Verified") - Jika kedua nilai tersebut sama, maka akan muncul pesan dialog dengan judul "Success" dan pesan "Verified" yang menandakan bahwa verifikasi berhasil. generate_image() - Memanggil fungsi generate_image() untuk menghasilkan gambar captcha baru setelah proses verifikasi selesai. else: - Jika kedua nilai tersebut tidak sama, maka akan dilakukan hal berikutnya. messagebox.showinfo("Alert", "Not verified") - Akan muncul pesan dialog dengan judul "Alert" dan pesan "Not verified" yang menandakan bahwa verifikasi tidak berhasil. generate_image() - Memanggil fungsi generate_image() untuk menghasilkan gambar captcha baru setelah proses verifikasi selesai.

Kode di atas akan mengambil input dari pengguna, membandingkannya dengan angka acak yang dihasilkan sebelumnya, dan menampilkan pesan yang sesuai tergantung pada hasil verifikasi.

```python
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


```

## Explanations of the rest codes

Kode ini adalah implementasi dasar dari GUI (Graphical User Interface) menggunakan library Tkinter di Python. GUI ini memiliki beberapa elemen utama seperti label (l1), teks (t1), tombol (b1 dan b2), dan gambar (photo).

Baris pertama membuat objek Tk() yang akan menjadi jendela utama GUI.
Kemudian, variabel photo dideklarasikan dan diinisialisasi dengan None untuk menghindari UnboundLocalError.
Selanjutnya, dibuat label (l1) dengan tinggi 100 piksel dan lebar 200 piksel menggunakan Label(root, height=100, width=200).
Setelah itu, dibuat teks (t1) dengan tinggi 5 baris dan lebar 50 karakter menggunakan Text(root, height=5, width=50).
Berikutnya, dibuat tombol (b1 dan b2) dengan teks "submit" dan "refresh" serta masing-masing memiliki aksi yang akan dieksekusi saat tombol ditekan menggunakan command=verify dan command=generate_image.
Label, teks, dan tombol tersebut kemudian ditampilkan menggunakan l1.pack(), t1.pack(), b1.pack(), dan b2.pack().
Setelah itu, fungsi generate_image() dipanggil untuk menampilkan gambar captcha pada saat aplikasi berjalan.
Terakhir, root.mainloop() digunakan untuk menjalankan GUI dan menjaga jendela GUI tetap terbuka sampai ditutup oleh pengguna.
Kode di atas menunjukkan bagaimana membuat GUI sederhana dengan beberapa elemen dan menghubungkannya dengan fungsi-fungsi tertentu untuk melakukan tugas-tugas seperti verifikasi input dan menghasilkan gambar captcha.

## Libraries Used

- tkinter: for creating GUI components
- captcha.image: for generating captcha images
- messagebox from tkinter: for displaying message boxes

### Functions

- generate_image(): generates a new captcha image with a new random number, saves it to a file named output.png, and displays it in the GUI using the Label widget.
- verify(): gets the input from the text box, compares it with the random number generated previously, and shows a message box with either a success message or an alert message, depending on whether the input is correct or not.

### GUI Components

- Label: to display the captcha image
- Text: to get the input from the user
- Button: to submit the input and refresh the captcha image

### How to Run

- To run the code, open it in an IDE or text editor and run it. The captcha image will be displayed along with the user input box and buttons.

```console
  $python.exe .\main.py
```

- Enter the six-digit number shown in the captcha image into the input box and click submit to verify.
- Click the refresh button to generate a new captcha image if the current one is difficult to read.

### Changes Made

- Redefined __random__ as a global variable, so that it can be accessed by other functions.
- Created the __generate_image()__ function to encapsulate complex logic related to generating captcha image, which also updates __random__ global variable and makes __photo__ available globally. It's called on button click, and also on application startup to (re)display captcha image.
- Removed redundant checks of __isinstance(data, BytesIO)__ on each __generate()__ call.
