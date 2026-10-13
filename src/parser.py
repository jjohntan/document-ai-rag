import argparse
import pymupdf


def  parse_arg() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='Document Ai', 
        description='Extract text from PDF')
    parser.add_argument('pdf_path', type=str, help='Path to PDF file')
    # parser.add_argument('prompt', type=str, help='Prompt to ask the model')
    return parser.parse_args()


def  extract_text_from_pdf(pdf_path: str):
    doc = pymupdf.open(pdf_path) # open a document
    pages = []

    for page in doc: # iterate the document pages
        page_text = page.get_text()# all text of the page
        pages.append(page_text)

    doc.close()
    full_page = "\f".join(pages) # page delimiter form feed 0x0C
    
    return full_page