import pytesseract
from PIL import Image
import fitz  # PyMuPDF

doc = fitz.open("PDF_TXT1.pdf")

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    pix = page.get_pixmap()  # Convert page to image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # OCR with Kurdish language model
    text = pytesseract.image_to_string(img, lang="ckbLayer")
    print(text)
