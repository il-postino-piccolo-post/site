import re

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove authors
content = re.sub(r'Articolo a cura di [a-zA-Z\s]+', '', content, flags=re.IGNORECASE)

# Specifically remove "Articolo Giornale PostinoSede Marano (NA 80016)POSTINO" from the Videogame article just in case
content = content.replace("Articolo Giornale PostinoSede Marano (NA 80016)POSTINO", "")
content = content.replace("Articolo Giornale Postino", "")

# Fix the images that are wrong/white
# Videogame image
content = content.replace('"img": "016bed86-0176-4a17-9bae-2f630b53e4da.jfif"', '"img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=800&q=80"')

# Kid Yugi image (was maybe a videogame one)
content = content.replace('"img": "b1405765-4434-440f-913e-c77729c822d6.jfif"', '"img": "https://images.unsplash.com/photo-1541689592655-f5f52825a3b8?auto=format&fit=crop&w=800&q=80"')

# Shiva image (was maybe white)
content = content.replace('"img": "41b2017d-a2c0-4a28-9b0c-04f4a0a1c038.jfif"', '"img": "https://images.unsplash.com/photo-1493225457124-a1a2a5956093?auto=format&fit=crop&w=800&q=80"')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("script.js fixed successfully")
