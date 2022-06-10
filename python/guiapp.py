# This is a Python program to do a graphics window
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

ButtonNotPressed = True

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# Instructions
instructions = tk.Label(root, text="Select a PDF file to see text")
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    global ButtonNotPressed # only needed if variable is modified in function
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("Pdf file","*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        if ButtonNotPressed:
            ButtonNotPressed = False
            canvas = tk.Canvas(root, width=600, height=250)
            canvas.grid(columnspan=3)

        # Text box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("left", justify="left")
        text_box.tag_add("left", 1.0, "end")
        text_box.grid(column=1, row=3)
        
        browse_text.set("Browse")
# Logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

root.mainloop()
