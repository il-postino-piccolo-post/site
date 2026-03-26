import urllib.request
import json
import os

def fetch_wiki_image(title, filename):
    url = f"https://it.wikipedia.org/w/api.php?action=query&prop=pageimages&titles={title}&pithumbsize=800&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            pages = data['query']['pages']
            for page_id in pages:
                if 'thumbnail' in pages[page_id]:
                    img_url = pages[page_id]['thumbnail']['source']
                    print(f"Downloading {img_url} to {filename}")
                    urllib.request.urlretrieve(img_url, filename)
                    return True
    except Exception as e:
        print(f"Failed to fetch for {title}: {e}")
    return False

images_to_fetch = [
    ("Circuito_integrato", "chip_informatica.jpg"),
    ("Libro", "libro_italiano.jpg"),
    ("Compasso", "matematica_fisica.jpg"),
    ("Dizionario", "dizionario_inglese.jpg"),
    ("Microscopio", "microscopio_scienze.jpg"),
    ("Calamo_(scrittura)", "penna_lettere.jpg"),
    ("Colosseo", "colosseo_latino.jpg")
]

for title, filename in images_to_fetch:
    fetch_wiki_image(title, filename)
