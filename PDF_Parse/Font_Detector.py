
import fitz  # PyMuPDF

doc = fitz.open("PDF_TXT1.pdf")

for page_num, page in enumerate(doc):
    fonts = page.get_fonts(full=True)
    print(f"Fonts used on Page {page_num + 1}:")
    for font in fonts:
        print(font)

