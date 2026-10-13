import argparse
import pymupdf


def  parse_arg() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='Document Ai', 
        description='Extract text from PDF')
    parser.add_argument('pdf_path', type=str, help='Path to PDF file')
    # parser.add_argument('prompt', type=str, help='Prompt to ask the model')
    return parser.parse_args()


def  extract_text_from_pdf(filename):
    # If it's a file-like object (e.g. Streamlit UploadedFile)
    if hasattr(filename, "read"):
        doc = pymupdf.open(stream=filename.read(), filetype="pdf")
    # If raw bytes were passed
    elif isinstance(filename, bytes):
        doc = pymupdf.open(stream=filename, filetype="pdf")
    # Otherwise treat as a file path string
    else:
        doc = pymupdf.open(filename) # open a document
    pages = []

    for page in doc: # iterate the document pages
        page_text = page.get_text()# all text of the page
        pages.append(page_text)

    doc.close()
    full_page = "\f".join(pages) # page delimiter form feed 0x0C
    
    return full_page