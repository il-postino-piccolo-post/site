import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

urls = {
    'chip_informatica.jpg': 'https://upload.wikimedia.org/wikipedia/commons/8/80/Three_IC_circuit_chips.JPG',
    'libro_italiano.jpg': 'https://upload.wikimedia.org/wikipedia/commons/8/87/Old_book_bindings.jpg',
    'dizionario_inglese.jpg': 'https://upload.wikimedia.org/wikipedia/commons/6/6e/Latin_dictionary.jpg',
    'microscopio_scienze.jpg': 'https://upload.wikimedia.org/wikipedia/commons/6/6c/Microscope-letters.svg',
    'penna_lettere.jpg': 'https://upload.wikimedia.org/wikipedia/commons/b/b3/Quill_pen.jpg',
    'colosseo_latino.jpg': 'https://upload.wikimedia.org/wikipedia/commons/d/de/Colosseo_2020.jpg',
    'matematica_fisica.jpg': 'https://upload.wikimedia.org/wikipedia/commons/1/15/Compasso_in_ottone.jpg',
    'ufficio_vicepreside.jpg': 'https://upload.wikimedia.org/wikipedia/commons/1/1d/Classroom_in_a_School.jpg'
}

for fname, url in urls.items():
    print(f'Downloading {fname} da {url}...')
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req) as response:
            with open(fname, 'wb') as f:
                f.write(response.read())
        print(f"Salvato: {fname}")
    except Exception as e:
        print(f"Errore {fname}: {e}")
