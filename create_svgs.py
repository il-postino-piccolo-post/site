import os

svgs = {
    "chip_informatica.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="#3b82f6">
  <rect x="25" y="25" width="50" height="50" rx="5" />
  <path d="M20 30h-10 M20 40h-10 M20 50h-10 M20 60h-10 M20 70h-10" stroke="#3b82f6" stroke-width="4"/>
  <path d="M80 30h10 M80 40h10 M80 50h10 M80 60h10 M80 70h10" stroke="#3b82f6" stroke-width="4"/>
  <path d="M30 20v-10 M40 20v-10 M50 20v-10 M60 20v-10 M70 20v-10" stroke="#3b82f6" stroke-width="4"/>
  <path d="M30 80v10 M40 80v10 M50 80v10 M60 80v10 M70 80v10" stroke="#3b82f6" stroke-width="4"/>
</svg>""",
    "libro_italiano.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="#10b981">
  <path d="M20 20 Q50 10 80 20 L80 80 Q50 70 20 80 Z" stroke="#10b981" stroke-width="4" fill="none"/>
  <path d="M50 15 V75" stroke="#10b981" stroke-width="4"/>
  <line x1="25" y1="30" x2="45" y2="30" stroke="#10b981" stroke-width="2"/>
  <line x1="25" y1="40" x2="45" y2="40" stroke="#10b981" stroke-width="2"/>
  <line x1="55" y1="30" x2="75" y2="30" stroke="#10b981" stroke-width="2"/>
  <line x1="55" y1="40" x2="75" y2="40" stroke="#10b981" stroke-width="2"/>
</svg>""",
    "dizionario_inglese.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="#ef4444">
  <rect x="25" y="15" width="50" height="70" rx="3" fill="#ef4444" />
  <text x="35" y="55" fill="white" font-family="Arial" font-size="20" font-weight="bold">EN</text>
  <line x1="35" y1="25" x2="65" y2="25" stroke="white" stroke-width="2"/>
</svg>""",
    "microscopio_scienze.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none" stroke="#22c55e" stroke-width="5" stroke-linecap="round">
  <path d="M30 80 h40 M50 80 v-20 M50 60 l-15 -35 l10 -5 l15 35 M40 50 a15 15 0 0 0 30 0" />
</svg>""",
    "penna_lettere.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none" stroke="#8b5cf6" stroke-width="4" stroke-linecap="round">
  <path d="M80 20 C60 20 50 40 40 60 L30 80 L40 75 C60 60 70 40 80 20 Z" />
  <line x1="40" y1="60" x2="80" y2="20" />
  <path d="M20 90 h20" stroke-width="8" />
</svg>""",
    "colosseo_latino.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none" stroke="#f59e0b" stroke-width="4">
  <path d="M10 80 L10 50 C30 40 70 40 90 50 L90 80 Z" />
  <path d="M10 80 h80" />
  <circle cx="25" cy="65" r="5" />
  <circle cx="50" cy="65" r="5" />
  <circle cx="75" cy="65" r="5" />
</svg>""",
    "matematica_fisica.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none" stroke="#ec4899" stroke-width="4" stroke-linecap="round">
  <path d="M50 20 L20 80 M50 20 L80 80" />
  <line x1="35" y1="50" x2="65" y2="50" />
  <circle cx="50" cy="20" r="4" fill="#ec4899" />
</svg>""",
    "ufficio_vicepreside.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none" stroke="#64748b" stroke-width="4">
  <rect x="20" y="40" width="60" height="40" rx="5" />
  <path d="M35 40 v-10 h30 v10" />
  <line x1="20" y1="60" x2="80" y2="60" />
  <circle cx="50" cy="50" r="3" fill="#64748b" />
</svg>"""
}

for filename, content in svgs.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
