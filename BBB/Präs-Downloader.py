import cairosvg
import io
from PyPDF2 import PdfFileMerger
import urllib
i = 1
merger = PdfFileMerger()
url = "url/svg/{}"
while(True):
    try:
        pdf = cairosvg.svg2pdf(url=url.format(i),scale=20)
        merger.append(io.BytesIO(pdf))
        print("{}".format(i))
    except urllib.error.HTTPError:
        print("{} pages".format(i-1))
        break
    i+=1
merger.write("all.pdf")
