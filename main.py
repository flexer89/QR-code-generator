import tkinter
import segno


def save_qr(message, filename, extension):
    info.config(text="Wait a second . . .")
    qr = segno.make_qr(message, version=5)
    qr.save(f"{filename}{extension}", border=5, scale=10)
    info.after(1000, lambda: info.config(text="A QR code has been generated!"))


# Root initialise
root = tkinter.Tk()
root.resizable(False, False)
width = 400
height = 450
root.title("QR Code Generator | Jakub Olszak")
root.iconbitmap("qr.ico")
root.config(bg="#12192c")

# variable declaration
data_val = tkinter.StringVar()
name_val = tkinter.StringVar()
data_val.set("")
name_val.set("")

# Calculate Starting X and Y coordinates for Window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))

# Heading label
heading_label = tkinter.Label(root, text="QR code generator", bg="#12192c", fg="#f7fefc", font=('tahoma', 24, 'normal'))
heading_label.pack(pady=(30, 0))

# Text/Url label
data_label = tkinter.Label(root, text="Enter the text/url", bg="#12192c", fg="#f7fefc", font=('tahoma', 16, 'normal'))
data_label.pack(pady=(30, 0))

# Text/Url input
data_entry = tkinter.Entry(root, bg="#12192c", insertbackground="#f7fefc", textvariable=data_val, fg="#f7fefc",
                           font=('tahoma', 14, 'normal'))
data_entry.pack(padx=50, pady=(10, 20), fill=tkinter.X)

# File name label
name_label = tkinter.Label(root, text="Enter the filename", bg="#12192c", fg="#f7fefc", font=('tahoma', 16, 'normal'))
name_label.pack()

# File name input
name_entry = tkinter.Entry(root, insertbackground="#f7fefc", bg="#12192c", textvariable=name_val,
                           fg="#f7fefc", font=('tahoma', 14, 'normal'))
name_entry.pack(padx=50, pady=(10, 40), fill=tkinter.X)

# PDF save button
pdf_button = tkinter.Button(root, text='Save to .PDF', fg="#f7fefc", borderwidth=0, bg="#00c9a7",
                            font=('tahoma', 14, 'normal'),
                            command=(lambda: save_qr(data_val.get(), name_val.get(), ".pdf")))
pdf_button.pack(padx=50, pady=5, fill=tkinter.X)

# PNG save button
png_button = tkinter.Button(root, text='Save to .PNG', fg="#f7fefc", bg="#00c9a7", borderwidth=0,
                            font=('tahoma', 14, 'normal'),
                            command=(lambda: save_qr(data_val.get(), name_val.get(), ".png")))
png_button.pack(padx=50, fill=tkinter.X)

# generation info label
info = tkinter.Label(root, bg="#12192c", fg="#f7fefc", font=("tahoma", 10, "normal"))
info.pack(pady=20)

root.mainloop()
