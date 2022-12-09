from PyPDF2 import PdfWriter, PdfReader

pdf_path = r"D:\tyg_tools\mini-tools\pdf-control\tmp\P17-1054.pdf"
# pdf_path = r"D:\zotero\微调\Sun et al_2020_How to Fine-Tune BERT for Text Classification.pdf"
reader = PdfReader(pdf_path)
writer = PdfWriter()

num_pages = len(reader.pages)
print("The document has %s pages." % num_pages)


for i in range(num_pages):
    page = reader.pages[i]
    # 左下是(0,0)坐标，右上是(x,y)坐标，单位是0.01英寸左右不确定
    page.mediaBox.upper_right = (page.mediabox.right -50, page.mediabox.top -50)
    page.mediaBox.lower_left = (page.mediabox.left +50, page.mediabox.bottom +50)

    writer.add_page(page)

new_path = pdf_path[:-4]+"-new"+".pdf"
with open(new_path, "wb") as fp:
    writer.write(fp)