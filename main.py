from PyPDF2 import PdfMerger
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Store newly created image
images = []

# Global fill color for canvas
fill = ()

# Label bg color
label_color = "#FCFAFA"

pdf_list = []

button_font = ("Helvetica", 10)

TARGET_PATH = ""


def create_rectangle(x, y, a, b, **options):
    """Create transparent rectangle with title inside it and exports fill parameter as a tuple (RGBA)"""
    global fill
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 20)
    if 'alpha' in options:
        # Calculate the alpha transparency for every color(RGB)
        alpha = int(options.pop('alpha') * 255)
        # Use the fill variable to fill the shape with transparent color
        fill = options.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        # Create image with pillow
        image = Image.new('RGBA', (a - x, b - y), fill)
        img = ImageDraw.Draw(image)
        # Add title
        img.text(((a - x) / 2 - 125, 10), "Choose PDFs to Merge", fill=(41, 41, 41), font=fnt, align="center")
        images.append(ImageTk.PhotoImage(image))
        canva.create_image(x, y, image=images[-1], anchor='nw')


def pdf_browse():
    """Opens filedialog to choose pdf files. Verifies if extension is .pdf and checks if maximum number of files
     wasn't exceeded """
    global pdf_list
    path = filedialog.askopenfilename(title="Add PDF")
    if path.endswith(".pdf"):
        if len(pdf_list) < 6:
            pdf_list.append(path)
            root.title("PDF Merger")
        else:
            root.title("You have reached maximum number of files!")
        list_label.config(text="")
        for i in range(len(pdf_list)):
            pdf = pdf_list[i]
            if i != 0:
                list_label["text"] += "\n"
            pdf_name = os.path.basename(pdf)
            list_label["text"] += f"{i + 1}) {pdf_name}"
    else:
        root.title("Select .pdf file")


def merge():
    """Merge function"""
    global TARGET_PATH
    if len(pdf_list) == 0:
        root.title("Add PDF files")
    else:
        merger = PdfMerger()
        for pdf in pdf_list:
            merger.append(pdf)
        merger.write(f"{TARGET_PATH}/merged.pdf")
        merger.close()
        root.title("Files merged")


def clear_list():
    """Clears list of pdfs"""
    global pdf_list
    pdf_list = []
    list_label.config(text="")


def target_found():
    """Opens filedialog to pick target directory"""
    global TARGET_PATH
    path = filedialog.askdirectory(title="Target Directory")
    path_label.config(text=path)
    TARGET_PATH = path


if __name__ == "__main__":
    root = tk.Tk()
    root.title("PDF Merger")
    width = 500
    height = 333
    root.geometry(f"{width}x{height}")

    bg = ImageTk.PhotoImage(file="./images/small.png")
    canva = tk.Canvas(root, height=height, width=width)
    canva.place(x=0, y=0)

    # create a background image

    canva.create_image(width / 2, height / 2, image=bg)

    # Create transparent rectangle with title

    create_rectangle(25, 25, width - 25, height - 25, fill="white", alpha=0.98)

    # Create widgets

    pdf_list_label = tk.Label(text="PDF List:", bg=label_color)
    pdf_list_label.place(x=45, y=75)

    list_label = tk.Label(text="", bg=label_color, justify="left")
    list_label.place(x=45, y=100)

    target_label = tk.Label(text="Target directory:", bg=label_color)
    target_label.place(x=45, y=220)

    path_label = tk.Label(text="", bg=label_color, wraplength=200, justify="left")
    path_label.place(x=45, y=245)

    browse_button = tk.Button(text="Add PDF", width=15, font=button_font, command=pdf_browse)
    browse_button.place(x=300, y=100)

    clear_button = tk.Button(text="Clear List", width=15, font=button_font, command=clear_list)
    clear_button.place(x=300, y=140)

    target_button = tk.Button(text="Target directory", width=15, font=button_font, command=target_found)
    target_button.place(x=300, y=220)

    merge_button = tk.Button(text="Merge", width=15, font=button_font, command=merge)
    merge_button.place(x=300, y=260)

    root.mainloop()
