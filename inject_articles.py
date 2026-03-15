import json
import re
import os

def load_extracted_data(file_path):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = content.split("=== FILE: ")
    data = {}
    for part in parts:
        if not part.strip():
            continue
        # Split into filename and text
        lines = part.split("\n", 1)
        if len(lines) > 1:
            header = lines[0].strip()
            filename = header.replace(" ===", "").strip()
            text = lines[1].strip()
            if not text.startswith("Error"):
                data[filename] = text
            else:
                print(f"Warning: Extraction failed for {filename}: {text[:100]}...")
    return data

def main():
    print("Loading extracted data...")
    data = load_extracted_data('full_extracted_texts.txt')
    if not data:
        print("No extracted data found. Run extract_all.py first.")
        return

    # Define full database articles with mapping to files
    # These match the titles in the original script.js
    articles_data = [
        {
            "title": "Hansi Flick: La Rinascita del Barcellona",
            "category": "Sport", "tag": "Analisi",
            "excerpt": "Hansi Flick sta trasformando il Barcellona con un gioco verticale e aggressivo. Scopriamo come.",
            "img": "49d833e4-f356-48d2-a531-60976e4364ba.jfif",
            "file": "Articolo per giornale 2.docx"
        },
        {
            "title": "Il Parma e la presidenza Manenti",
            "category": "Sport", "tag": "Serie A",
            "excerpt": "Il ricordo della presidenza Manenti e il fallimento del Parma nel 2015.",
            "img": "manenti_profile.jpg",
            "file": "Articolo per il giornale corretto.docx"
        },
        {
            "title": "Il Maracanazo: Una Ferita Aperta",
            "category": "Sport", "tag": "Storia",
            "excerpt": "Il 16 luglio 1950 il Brasile perse il Mondiale in casa contro l'Uruguay.",
            "img": "maracanazo_history.jpg",
            "file": "Il Maracanazo (1) corretto.docx"
        },
        {
            "title": "Cime Tempestose: Una Recensione",
            "category": "Cinema", "tag": "Recensione",
            "excerpt": "Il nuovo film diretto da Emerald Fennell che riprende il romanzo di Emily Bronte.",
            "img": "b6b5b384-4888-446b-a84e-fdd7069d6ac3.jfif",
            "file": "Cime Tempestose.docx"
        },
        {
            "title": "Scuola e videogiochi, opposti o coincidenti?",
            "category": "Videogiochi", "tag": "Riflessione",
            "excerpt": "Una riflessione su come i videogiochi come Uncharted possano essere educativi.",
            "img": "87e20958-928b-4d25-9252-120d9f99c40e.jfif",
            "file": "christian damone corretto.docx"
        },
        {
            "title": "La Bellavita di Artie 5ive",
            "category": "Musica", "tag": "Recensione Album",
            "excerpt": "Recensione dell'album 'La Bellavita' pubblicato nel 2025.",
            "img": "5e7b36fc-95b0-4cb1-afcc-89e43938d108.jfif",
            "file": "LA BELLAVITA Felice De Vita.docx"
        },
        {
            "title": "Anche gli eroi muoiono - Kid Yugi",
            "category": "Musica", "tag": "Recensione Album",
            "excerpt": "Il ritorno di Kid Yugi con un album crudo e introspettivo.",
            "img": "8d8e509c-61fc-4221-9be2-bab2057a5e86.jfif",
            "file": "RECENSIONE KID YUGI VINCENZO PIROZZI.docx"
        },
        {
            "title": "Dolce Vita - Shiva",
            "category": "Musica", "tag": "Recensione Album",
            "excerpt": "L'album della rivincita di Shiva pubblicato nel 2021.",
            "img": "0ee88205-fa7f-40d1-afd2-0966d7a6f364.jfif",
            "file": "Roberta Guarino.docx"
        },
        {
            "title": "Heroes & Villains - Metro Boomin",
            "category": "Musica", "tag": "Recensione Album",
            "excerpt": "Un viaggio cinematografico tra eroi e cattivi.",
            "img": "8d0b2472-63a9-4251-92ea-2f468cb2595e.jfif",
            "file": "Document 3-2.pdf"
        },
        {
            "title": "TREDICI PIETRO",
            "category": "Musica", "tag": "Recensione Album",
            "excerpt": "Il nuovo album di Tredici Pietro, un viaggio crudo e introspettivo.",
            "img": "tredici_pietro.jfif",
            "file": "TREDICI PIETRO.txt"
        },
        {
            "title": "Aftersun - Il ricordo di un'estate",
            "category": "Cinema", "tag": "Recensione",
            "excerpt": "Un film delicato sul rapporto padre-figlia e la salute mentale.",
            "img": "aftersun_movie_poster_1773352108336.png",
            "file": "Documento senza titolo.pdf"
        },
        {
            "title": "Uncharted: Il Film",
            "category": "Cinema", "tag": "Recensione",
            "excerpt": "L'avventura di Nathan Drake arriva sul grande schermo.",
            "img": "uncharted_new.jfif",
            "file": "Presentazione senza titolo (4).pdf"
        },
        {
            "title": "Intervista: Prof.ssa Ferraro",
            "category": "Attualità Segrè", "tag": "Intervista",
            "excerpt": "Quattro chiacchiere con Rossella Ferraro sulla passione per l'informatica.",
            "img": "chip_informatica.jpg",
            "file": "INTERVISTA PROF FERRARO.docx"
        },
        {
            "title": "Intervista: Prof. Russo",
            "category": "Attualità Segrè", "tag": "Intervista",
            "excerpt": "Il ruolo di docente e vicepreside tra responsabilità e sfide.",
            "img": "ufficio_vicepreside.jpg",
            "file": "INTERVISTA AL PROF RUSSO.pdf"
        },
        {
            "title": "Intervista: Prof. Farina",
            "category": "Attualità Segrè", "tag": "Intervista",
            "excerpt": "Matematica, fisica e il futuro dell'Intelligenza Artificiale.",
            "img": "matematica_fisica.jpg",
            "file": "INTERVISTA PROF FARINA.pdf"
        },
        {
            "title": "Intervista: Prof.ssa Fioretto",
            "category": "Attualità Segrè", "tag": "Intervista",
            "excerpt": "L'importanza dell'inglese e i nuovi metodi di insegnamento coinvolgenti.",
            "img": "dizionario_inglese.jpg",
            "file": "INTERVISTA PROF FIORETTO.pdf"
        },
        {
            "title": "Intervista: Prof. Liccardo",
            "category": "Attualità Segrè", "tag": "Intervista",
            "excerpt": "Sviluppare lo spirito critico attraverso lo studio delle scienze naturali.",
            "img": "microscopio_scienze.jpg",
            "file": "INTERVISTA PROF LICCARDO.pdf"
        },
        {
            "title": "Intervista: Prof.ssa Parigiano",
            "category": "Attualità Segrè", "tag": "Intervista",
            "excerpt": "L'amore per le Lettere e l'incontro con i grandi classici.",
            "img": "penna_lettere.jpg",
            "file": "INTERVISTA PROF PARIGIANO.pdf"
        }
    ]

    # Build final articles list
    final_articles = []
    for a in articles_data:
        filename = a.pop("file")
        content = data.get(filename)
        if content:
            # Fix typo specifically for Kid Yugi article
            if filename == "RECENSIONE KID YUGI VINCENZO PIROZZI.docx":
                content = content.replace("Deianira", "De André")
            a["fullText"] = content
        else:
            print(f"Notice: Using placeholder for {a['title']} (no content in {filename})")
            a["fullText"] = f"Contenuto per {a['title']} non ancora disponibile integralmente."
        final_articles.append(a)

    # Update script.js
    print("Reading script.js...")
    with open('script.js', 'r', encoding='utf-8') as f:
        js_content = f.read()

    # Construct the JS array string
    articles_js = "const articlesDatabaseRaw = [\n"
    for a in final_articles:
        articles_js += "    " + json.dumps(a, ensure_ascii=False) + ",\n"
    articles_js += "];"

    # Replace the array
    print("Injecting new articles database...")
    new_js_content = re.sub(
        r'const articlesDatabaseRaw = \[.*?\];', 
        articles_js.replace('\\', '\\\\'),
        js_content, 
        flags=re.DOTALL
    )
    new_js_content = new_js_content.replace("\\\\", "\\")

    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(new_js_content)
    
    print("script.js successfully updated with all 18 articles!")

if __name__ == "__main__":
    main()
