"""Bettet die Klasse-7-Arbeitsblätter fest in index.html ein.

Liest Klasse7_Akustik_Messgeraete.json und ersetzt den Block zwischen den
Markern im Abschnitt "KLASSE7-DATEN".

Aufruf: python embed_klasse7.py
"""

import json
from pathlib import Path

HIER = Path(__file__).resolve().parent
HTML = HIER.parent / "index.html"
DATEN = HIER / "Klasse7_Akustik_Messgeraete.json"

START = "/* === KLASSE7-DATEN (generiert, nicht bearbeiten) === */"
ENDE = "/* === ENDE KLASSE7-DATEN === */"

data = json.loads(DATEN.read_text(encoding="utf-8"))
ordner = data["folders"][0]
blaetter = data["sheets"]

js = (
    START
    + "\nconst KLASSE7_FOLDER = "
    + json.dumps(ordner, ensure_ascii=False)
    + ";\nconst KLASSE7_SHEETS = "
    + json.dumps(blaetter, ensure_ascii=False)
    + ";\n"
    + ENDE
)

html = HTML.read_text(encoding="utf-8")

if START in html and ENDE in html:
    vor = html.split(START)[0]
    nach = html.split(ENDE, 1)[1]
    html = vor + js + nach
else:
    marker = "boot();"
    idx = html.rindex(marker)
    html = html[:idx] + js + "\n\n" + html[idx:]

HTML.write_text(html, encoding="utf-8")
print(f"{len(blaetter)} Blätter eingebettet, index.html ist jetzt {HTML.stat().st_size // 1024} KB groß")
