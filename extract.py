import os

def extract_docx(doc_path):
    import docx
    doc = docx.Document(doc_path)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_pdf(pdf_path):
    from pypdf import PdfReader
    reader = PdfReader(pdf_path)
    return "\n".join([page.extract_text() for page in reader.pages])

files = [f for f in os.listdir('.') if f.endswith('.docx') or f.endswith('.pdf')]
with open('extracted_texts.txt', 'w', encoding='utf-8') as out:
    for f in files:
        out.write(f"=== FILE: {f} ===\n")
        try:
            if f.endswith('.docx'):
                out.write(extract_docx(f))
            else:
                out.write(extract_pdf(f))
        except Exception as e:
            out.write(f"ERROR: {e}")
        out.write("\n\n")
print("Done writing to extracted_texts.txt")
