import re

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Update images with local files
content = content.replace('"img": "https://images.unsplash.com/photo-1518605368461-1e1252220a4c?auto=format&fit=crop&w=800&q=80"', '"img": "49d833e4-f356-48d2-a531-60976e4364ba.jfif"') # Flick
content = content.replace('"img": "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?auto=format&fit=crop&w=800&q=80"', '"img": "49d833e4-f356-48d2-a531-60976e4364ba.jfif"') # Parma
content = content.replace('"img": "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?auto=format&fit=crop&w=800&q=80"', '"img": "49d833e4-f356-48d2-a531-60976e4364ba.jfif"') # Maracanazo
content = content.replace('"img": "https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&w=800&q=80"', '"img": "b6b5b384-4888-446b-a84e-fdd7069d6ac3.jfif"') # Cime Tempestose
content = content.replace('"img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=800&q=80"', '"img": "87e20958-928b-4d25-9252-120d9f99c40e.jfif"') # Videogiochi
content = content.replace('"img": "https://images.unsplash.com/photo-1493225457124-a1a2a5956093?auto=format&fit=crop&w=800&q=80"', '"img": "5e7b36fc-95b0-4cb1-afcc-89e43938d108.jfif"') # La Bellavita
content = content.replace('"img": "https://images.unsplash.com/photo-1541689592655-f5f52825a3b8?auto=format&fit=crop&w=800&q=80"', '"img": "8d8e509c-61fc-4221-9be2-bab2057a5e86.jfif"') # Kid Yugi
# Shiva image was already updated to unsplash in previous turn? 
# Wait, I used: content = content.replace('"img": "41b2017d-a2c0-4a28-9b0c-04f4a0a1c038.jfif"', '"img": "https://images.unsplash.com/photo-1493225457124-a1a2a5956093?auto=format&fit=crop&w=800&q=80"')
# Let's just fix Shiva to its cover
content = content.replace('"img": "https://images.unsplash.com/photo-1493225457124-a1a2a5956093?auto=format&fit=crop&w=800&q=80"', '"img": "0ee88205-fa7f-40d1-afd2-0966d7a6f364.jfif"')
# Prof Ferraro
content = content.replace('"img": "https://images.unsplash.com/photo-1580894732444-8ecded7900cd?auto=format&fit=crop&w=800&q=80"', '"img": "df2fb62d-cca2-43c7-83e4-da13ad21a418.jfif"')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("script.js images mapped successfully")
