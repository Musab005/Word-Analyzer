import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = []
    with open(pdf_file, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return [" ".join(text)]
