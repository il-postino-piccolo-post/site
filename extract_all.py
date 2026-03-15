import zipfile
import os
import xml.etree.ElementTree as ET

def get_docx_text(path):
    """
    Extracts text from a .docx file by reading its internal XML (word/document.xml).
    """
    try:
        if not os.path.exists(path):
            return f"Error: File {path} not found."
            
        with zipfile.ZipFile(path) as z:
            xml_content = z.read('word/document.xml')
        
        tree = ET.fromstring(xml_content)
        namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        paragraphs = []
        for p in tree.findall('.//w:p', namespace):
            texts = p.findall('.//w:t', namespace)
            if texts:
                # Ensure we handle possible None in t.text (though rare for w:t)
                text_content = ''.join(t.text for t in texts if t.text is not None)
                if text_content:
                    paragraphs.append(text_content)
        
        return '\n'.join(paragraphs)
    except Exception as e:
        return f"Error extracting DOCX {path}: {str(e)}"

def get_pdf_text(path):
    """
    Extracts text from a .pdf file and cleans up fragmented text artifacts.
    """
    try:
        if not os.path.exists(path):
            return f"Error: File {path} not found."
            
        from pypdf import PdfReader
        import re
        reader = PdfReader(path)
        text_parts = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                # Heuristic to fix fragmented PDF text (word-per-line issue)
                # We join lines that don't seem to be intentional breaks (like dialogue or indents)
                lines = page_text.split('\n')
                cleaned_lines = []
                for i, line in enumerate(lines):
                    stripped = line.strip()
                    if not stripped: continue
                    
                    # If line starts with a quote or an indent, treat it as a new block
                    # We check for a leading space that isn't just a blank line
                    if line.startswith(' ') or stripped.startswith('“') or stripped.startswith('"'):
                        cleaned_lines.append('\n\n' + stripped)
                    else:
                        cleaned_lines.append(stripped)
                
                joined = " ".join(cleaned_lines)
                # Cleanup spaces
                joined = re.sub(r' +', ' ', joined)
                # Re-normalize our manual breaks
                joined = joined.replace(' \n\n ', '\n\n').replace('\n\n ', '\n\n')
                text_parts.append(joined)
        
        full_text = "\n\n".join(text_parts)
        # Final cleanup for double newlines
        full_text = re.sub(r'\n{3,}', '\n\n', full_text)
        return full_text.strip()
    except ImportError:
        return f"Error: pypdf not installed. Cannot extract PDF {path}."
    except Exception as e:
        return f"Error extracting PDF {path}: {str(e)}"

files = [
    "Articolo per giornale 2.docx",
    "Articolo per il giornale corretto.docx",
    "christian damone corretto.docx",
    "Cime Tempestose.docx",
    "INTERVISTA PROF FERRARO.docx",
    "Il Maracanazo (1) corretto.docx",
    "LA BELLAVITA Felice De Vita.docx",
    "RECENSIONE KID YUGI VINCENZO PIROZZI.docx",
    "Roberta Guarino.docx",
    "Document 3-2.pdf",
    "Documento senza titolo.pdf",
    "INTERVISTA AL PROF RUSSO.pdf",
    "INTERVISTA PROF FARINA.pdf",
    "INTERVISTA PROF FIORETTO.pdf",
    "INTERVISTA PROF LICCARDO.pdf",
    "INTERVISTA PROF PARIGIANO.pdf",
    "Presentazione senza titolo (4).pdf"
]

def main():
    print(f"Starting extraction of {len(files)} files...")
    with open("full_extracted_texts.txt", "w", encoding="utf-8") as f:
        for filename in files:
            print(f"Processing {filename}...")
            f.write(f"=== FILE: {filename} ===\n")
            if filename.lower().endswith('.docx'):
                f.write(get_docx_text(filename))
            elif filename.lower().endswith('.pdf'):
                f.write(get_pdf_text(filename))
            f.write("\n\n")

    print("Extraction complete. See full_extracted_texts.txt")

if __name__ == "__main__":
    main()
