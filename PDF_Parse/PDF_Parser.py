import pypdf


# Open the PDF file
with open("PDF_TXT1.pdf", "rb") as file:
    reader = pypdf.PdfReader(file)
    text = ""

    # Extract text from each page
    for page in reader.pages:
        text += page.extract_text()

print(text)