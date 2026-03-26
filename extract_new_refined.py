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
                # Fix fragmented text (one word per line)
                lines = page_text.split('\n')
                # Join lines that end with a hyphen or are just single words
                cleaned_text = " ".join(line.strip() for line in lines if line.strip())
                # Normalize spaces
                cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
                text_parts.append(cleaned_text)
        return "\n\n".join(text_parts)
    except Exception as e:
        return f"Error: {str(e)}"

# Extract from INTERVISTE (1).pdf to (8)
output = ""
for i in range(1, 9):
    filename = f"INTERVISTE  ({i}).pdf"
    if not os.path.exists(filename):
        filename = f"INTERVISTE ({i}).pdf"
    
    if os.path.exists(filename):
        output += f"=== {filename} ===\n"
        output += get_pdf_text(filename) + "\n"
        output += "-" * 30 + "\n"

with open("new_interviews_extracted.txt", "w", encoding="utf-8") as f:
    f.write(output)

print("Extraction complete. See new_interviews_extracted.txt")
