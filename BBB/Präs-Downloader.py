import cairosvg
import io
from PyPDF2 import PdfFileMerger
import urllib
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

i = 1
merger = PdfFileMerger()
split = input("URL: ").split("/")
split.pop()
url = "/".join(split) + "/{}"
name = filedialog.asksaveasfile(
    filetypes=[("PDF", "*.pdf")], defaultextension="*.pdf").name
print()
if(name == ""):
    exit()
while(True):
    try:
        pdf = cairosvg.svg2pdf(url=url.format(i), scale=20)
        merger.append(io.BytesIO(pdf))
        print("\rDownloading page {}".format(i), end='')
    except urllib.error.HTTPError:
        print("\rDownloaded {} pages".format(i-1), end='')
        break
    i += 1
merger.write(name)
