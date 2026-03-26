import os
import re
from pypdf import PdfReader

def get_pdf_text(path):
    try:
        reader = PdfReader(path)
        text_parts = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                # Basic cleaning
                lines = page_text.split('\n')
                cleaned_lines = []
                for line in lines:
                    stripped = line.strip()
                    if stripped:
                        cleaned_lines.append(stripped)
                text_parts.append("\n".join(cleaned_lines))
        return "\n\n".join(text_parts)
    except Exception as e:
        return f"Error: {str(e)}"

# Extract from INTERVISTE (1).pdf to (8)
for i in range(1, 9):
    filename = f"INTERVISTE  ({i}).pdf"
    if os.path.exists(filename):
        print(f"=== {filename} ===")
        text = get_pdf_text(filename)
        print(text)
        print("-" * 30)
    else:
        # Try without double space just in case
        filename = f"INTERVISTE ({i}).pdf"
        if os.path.exists(filename):
            print(f"=== {filename} ===")
            text = get_pdf_text(filename)
            print(text)
            print("-" * 30)
