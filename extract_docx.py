import os
import zipfile
import xml.etree.ElementTree as ET

def extract_docx(doc_path):
    text = []
    try:
        with zipfile.ZipFile(doc_path) as docx:
            xml_content = docx.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            for node in tree.iter():
                if node.tag.endswith('}t'):
                    if node.text:
                        text.append(node.text)
        return "".join(text)
    except Exception as e:
        return str(e)

files = [f for f in os.listdir('.') if f.endswith('.docx')]
with open('extracted_docx.txt', 'w', encoding='utf-8') as out:
    for f in files:
        out.write(f"=== {f} ===\n")
        out.write(extract_docx(f) + "\n\n")
