"""Erzeugt ein Backup (JSON) mit dem Ordner "Klasse 7" und sechs Arbeitsblättern.
Basis: Beispielcurriculum Physik BW, Klasse 7 (4.1 Akustik, 4.2 Messgeräte).

Stil: Vorlage nach arbeitsblatt.sty (schwarz/weiß, Rahmen, Kopfzeile oben).

Aufruf:  python build_klasse7.py
Ergebnis: Klasse7_Akustik_Messgeraete.json  (im gleichen Ordner)
"""

import itertools
import json
from datetime import datetime, timezone

NOW = datetime.now(timezone.utc).isoformat()
FOLDER_ID = "k7-folder"
SUBJECT = "Physik"
GRADE = "7"

_seq = itertools.count(1)


def blk(type_, **kw):
    return {"id": f"k7-b{next(_seq)}", "type": type_, **kw}


def page(blocks, pid):
    return {"id": pid, "blocks": blocks}


def sheet(title, pages, theme="vorlage", font="sans", folder=FOLDER_ID):
    return {
        "id": f"k7-sheet-{abs(hash(title)) % 10**9}",
        "title": title,
        "subject": SUBJECT,
        "grade": GRADE,
        "font": font,
        "margin": "normal",
        "theme": theme,
        "folderId": folder,
        "createdAt": NOW,
        "updatedAt": NOW,
        "pages": pages,
    }


def header(topic, variant="vorlage", school="Muster-Gymnasium"):
    return blk("header", school=school, subject=SUBJECT, topic=topic,
               showName=False, showClass=True, showDate=True, variant=variant)


def ziel(text):
    return blk("text", variant="merke", heading="Ziel der Stunde", body=text)


def merke(text, heading="Merke"):
    return blk("text", variant="merke", heading=heading, body=text)


def info(text, heading="Information"):
    return blk("text", variant="info", heading=heading, body=text)


def task(text, points="", solution="", parts=None):
    return blk("task", text=text, points="", solution=solution, parts=parts or [])


def cloze(text):
    return blk("cloze", text=text)


def lines(n=3, pattern="dotted"):
    return blk("lines", count=n, pattern=pattern)


def mc(question, options):
    return blk("mc", question=question,
               options=[{"text": t, "correct": c} for t, c in options])


def table(cells, header_row=True):
    return blk("table", header=header_row, cells=cells)


def formula(tex):
    return blk("formula", tex=tex)


def versuch(titel, material, schritte, lines_b=2, lines_a=2, auswertung=""):
    return blk("versuch", titel=titel, material=material,
               durchfuehrung=schritte, linesB=lines_b, linesA=lines_a,
               auswertung=auswertung)


def axes(xlabel, ylabel, xmax=10, ymax=10, xstep=1, ystep=1, caption="", height=95):
    return blk("axes", xLabel=xlabel, yLabel=ylabel, caption=caption,
               grid=True, numbers=True, square=False,
               xMin=0, xMax=xmax, xStep=xstep, yMin=0, yMax=ymax, yStep=ystep,
               width=100, heightMM=height, legend=[])


def total(label="Punkte gesamt", note=""):
    return blk("total", label=label, note=note)


def match(titel, pairs, order=None):
    return blk("match", titel=titel,
               items=[{"left": l, "right": r} for l, r in pairs],
               order=order or list(range(len(pairs)))[::-1])


def defbox(term, text):
    return blk("defbox", term=term, **{"def": text})


def signature(label="Datum, Unterschrift"):
    return blk("signature", label=label)


# ---------------------------------------------------------------- Blatt 1
s1 = sheet("Akustik 1 – Wie entsteht Schall?", [
    page([
        header("Akustik 1 – Wie entsteht Schall?"),
        ziel("Du kannst Schallquellen benennen und erklären, dass Schall durch "
             "schwingende Körper entsteht."),
        info("Ob Türknallen, Vogelzwitschern oder das Summen eines Handys – ständig "
             "erreichen uns Geräusche. Von **Schall** sprechen wir, wenn ein Körper "
             "**schwingt** und diese Schwingung über ein Medium (zum Beispiel Luft) "
             "zu unserem Ohr gelangt.", heading="Schall ist überall"),
        blk("block", label="A", titel="Einstieg: Hören und Beobachten"),
        task("Hörspaziergang: Schließe 30 Sekunden die Augen. Notiere fünf Geräusche "
             "und beschreibe sie möglichst genau.",
             solution="Individuelle Lösung, z. B. Tastaturklappern, Verkehr, Vogel, "
                      "Kühlschrank, Schritte."),
        table([["Geräusch", "Schallquelle", "laut / leise", "hoch / tief"],
               ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]),
        task("Was haben alle Schallquellen gemeinsam? Formuliere eine Vermutung.",
             solution="Alle Schallquellen schwingen bzw. bewegen sich."),
        lines(3),
    ], "k7-p1"),
    page([
        header("Akustik 1 – Wie entsteht Schall?"),
        blk("block", label="B", titel="Erklären: Schwingungen"),
        versuch("Versuch: Die zitternde Stimmgabel",
                "Stimmgabel, Schlagklöppel, Glas mit Wasser, Papierstreifen.",
                ["Stimmgabel vorsichtig anschlagen und ans Ohr halten.",
                 "Stimmgabel kurz in die Wasseroberfläche tauchen.",
                 "Leichten Papierstreifen an die Gabel halten."],
                lines_b=2, lines_a=2),
        task("Erkläre mit eigenen Worten, warum das Wasser spritzt und warum du einen "
             "Ton hörst. Nutze die Begriffe **Schwingung**, **Schallquelle** und **Luft**.",
             solution="Die Gabel schwingt und überträgt Energie auf das Wasser. Über die "
                      "Luft gelangt die Schwingung als Schall zum Ohr."),
        cloze("Schall entsteht, wenn ein Körper [schwingt]. Diese Schwingung breitet sich "
              "über ein [Medium] aus und erreicht unser [Ohr]."),
        mc("Welche Aussagen sind richtig?",
           [("Schall entsteht durch schwingende Körper.", True),
            ("Schall braucht keine Schwingung.", False),
            ("Ein Lautsprecher ist eine Schallquelle.", True),
            ("Schall kann man nur sehen.", False)]),
    ], "k7-p1b"),
])

# ---------------------------------------------------------------- Blatt 2
s2 = sheet("Akustik 2 – Wie breitet sich Schall aus?", [
    page([
        header("Akustik 2 – Wie breitet sich Schall aus?"),
        ziel("Du kannst erklären, dass Schall ein Ausbreitungsmedium braucht, und "
             "die Schallgeschwindigkeit für einfache Rechnungen nutzen."),
        merke("Schall breitet sich als Schwingung in einem **Medium** aus "
              "(Luft, Wasser, Metall). Im **Vakuum** ist kein Schall hörbar. "
              "In Luft ist Schall etwa **340 m/s** schnell."),
        blk("block", label="A", titel="Ausbreitung untersuchen"),
        versuch("Versuch: Schall braucht einen Träger",
                "Wecker (oder Handy), Glasglocke mit Pumpe, Vakuumpumpe.",
                ["Wecker in die Glocke legen und einschalten.",
                 "Luft langsam absaugen.",
                 "Geräusch beobachten und beschreiben."],
                lines_b=2, lines_a=2),
        task("Erkläre, warum der Wecker immer leiser wird, obwohl er weiter klingelt.",
             solution="Die Luft als Medium wird entfernt; ohne Medium kann sich die "
                      "Schwingung nicht ausbreiten."),
        blk("block", label="B", titel="Rechnen: Schallgeschwindigkeit"),
        formula(r"v = \frac{s}{t} \quad\Rightarrow\quad s = v \cdot t"),
        task("Bei einem Gewitter hörst du den Donner **3 s** nach dem Blitz. "
             "Wie weit ist das Gewitter entfernt? (v = 340 m/s)",
             solution="s = v · t = 340 m/s · 3 s = 1020 m ≈ 1 km."),
        task("Ein Echo kommt nach 0,6 s zurück. Wie weit ist die Wand entfernt? "
             "Achte darauf, dass der Schall hin und zurück läuft.",
             solution="s = v · t = 340 m/s · 0,6 s = 204 m (hin und zurück), "
                      "also 102 m bis zur Wand."),
        blk("block", label="C", titel="Sichern"),
        axes("t in s", "s in m", xmax=3, ymax=1200, xstep=0.5, ystep=200,
             caption="Weg des Schalls bei 340 m/s"),
        cloze("Schall braucht ein [Medium]. Im [Vakuum] kann er sich nicht ausbreiten. "
              "Die Schallgeschwindigkeit in Luft beträgt etwa [340 m/s]."),
        mc("Wie weit kommt Schall in 2 Sekunden (Luft)?",
           [("etwa 680 m", True), ("etwa 170 m", False),
            ("etwa 340 m", False), ("etwa 2 m", False)]),
    ], "k7-p2"),
])

# ---------------------------------------------------------------- Blatt 3
s3 = sheet("Akustik 3 – Amplitude und Frequenz", [
    page([
        header("Akustik 3 – Amplitude und Frequenz"),
        ziel("Du kannst Amplitude und Frequenz aus einem Schwingungsdiagramm ablesen "
             "und erklären, wie sie Lautstärke und Tonhöhe bestimmen."),
        merke("**Amplitude** = größte Auslenkung → bestimmt die **Lautstärke**. "
              "**Frequenz** = Schwingungen pro Sekunde (Einheit **Hertz, Hz**) → "
              "bestimmt die **Tonhöhe**."),
        defbox("Periode T", "Zeit für eine vollständige Schwingung. "
                            "Es gilt: f = 1 / T."),
        formula(r"f = \frac{1}{T}"),
        blk("block", label="A", titel="Diagramm lesen"),
        axes("t in ms", "Auslenkung", xmax=20, ymax=10, xstep=2, ystep=2,
             caption="Schwingung einer Stimmgabel (schematisch)"),
        task("Im Diagramm dauert eine vollständige Schwingung **4 ms**. "
             "Berechne die Frequenz in Hertz.",
             solution="T = 4 ms = 0,004 s → f = 1/0,004 s = 250 Hz."),
        task("Eine Saite schwingt mit 440 Hz. Wie lange dauert eine Schwingung?",
             solution="T = 1/f = 1/440 s ≈ 0,00227 s ≈ 2,3 ms."),
        blk("block", label="B", titel="Übertragen"),
        match("Ordne zu:", [
            ("große Amplitude", "lauter Ton"),
            ("kleine Amplitude", "leiser Ton"),
            ("hohe Frequenz", "hoher Ton"),
            ("kleine Frequenz", "tiefer Ton"),
        ]),
        cloze("Die Amplitude bestimmt die [Lautstärke], die Frequenz die [Tonhöhe]. "
              "Die Einheit der Frequenz ist [Hertz]."),
        mc("Ein Ton wird höher. Was ändert sich?",
           [("Die Frequenz steigt.", True), ("Die Amplitude steigt.", False),
            ("Die Frequenz sinkt.", False), ("Die Periode steigt.", False)]),
    ], "k7-p3"),
    page([
        header("Akustik 3 – Übungen"),
        blk("block", label="C", titel="Vertiefung"),
        table([["Frequenz f", "Periode T", "Tonhöhe"],
               ["100 Hz", "", ""], ["", "0,01 s", ""], ["1000 Hz", "", ""], ["", "2 ms", ""]]),
        task("Ergänze die Tabelle.",
             solution="100 Hz → 0,01 s; T = 0,01 s → 100 Hz; 1000 Hz → 1 ms; "
                      "T = 2 ms → 500 Hz."),
        lines(4),
        signature(),
    ], "k7-p3b"),
])

# ---------------------------------------------------------------- Blatt 4
s4 = sheet("Akustik 4 – Hören, Lärm und Schallschutz", [
    page([
        header("Akustik 4 – Hören, Lärm und Schallschutz"),
        ziel("Du kannst das Ohr als Schallempfänger beschreiben und begründen, "
             "wann Schall zu Lärm wird und wie man sich schützt."),
        info("Das **Ohr** nimmt Schall auf: Ohrmuschel → Gehörgang → Trommelfell → "
             "Gehörknöchelchen → Innenohr. Der Hörbereich des Menschen liegt etwa "
             "zwischen **16 Hz und 20 000 Hz**.", heading="Wie wir hören"),
        blk("block", label="A", titel="Lärm bewerten"),
        task("Nenne drei Situationen aus deinem Alltag, in denen Schall zu **Lärm** "
             "wird. Begründe jeweils kurz.",
             solution="z. B. Baustelle (dauerhaft laut), Kopfhörer zu laut (Gehör), "
                      "Bohrmaschine im Unterricht (Konzentration)."),
        task("Zwei Personen streiten über laute Musik im Zug. Formuliere je ein "
             "Argument für beide Seiten.",
             solution="Dafür: Freiheit, eigene Musik. Dagegen: Ruhebedürfnis, "
                      "Gesundheit, Rücksichtnahme."),
        blk("block", label="B", titel="Schallschutz"),
        defbox("Schallschutz", "Maßnahmen, die verhindern, dass Schall stört oder "
                               "das Gehör schädigt – z. B. Dämmung, Abstand, "
                               "Gehörschutz, leiseres Gerät."),
        task("Ordne drei Schallschutz-Maßnahmen den Begriffen **Dämmung**, "
             "**Abstand** und **Gehörschutz** zu.",
             solution="Dämmung: Teppich, Schaumstoff. Abstand: weiter weg von der "
                      "Quelle. Gehörschutz: Ohrstöpsel, Kapselgehörschutz."),
        cloze("Schall wird im Ohr vom [Trommelfell] aufgenommen. Zu lauter Schall "
              "kann das [Gehör] schädigen. Schutz bieten [Ohrstöpsel] oder Abstand."),
        mc("Welche Aussage ist richtig?",
           [("Lärm ist Schall, der stört oder schadet.", True),
            ("Jeder Schall ist Lärm.", False),
            ("Lärm kann das Gehör nicht schädigen.", False),
            ("Schallschutz macht Geräte immer lauter.", False)]),
        signature("Datum, Unterschrift der Erziehungsberechtigten"),
    ], "k7-p4"),
])

# ---------------------------------------------------------------- Blatt 5
s5 = sheet("Messgeräte 1 – Messgrößen und Einheiten", [
    page([
        header("Messgeräte 1 – Messgrößen und Einheiten"),
        ziel("Du kannst Messgröße, Einheit und Messgerät unterscheiden und mit "
             "Vorsätzen (k, m, µ) rechnen."),
        merke("Jede Messung besteht aus **Zahl** und **Einheit**. "
              "Physikalische Größen haben feste Einheiten (SI-System). "
              "Vorsätze: k = 1000 · m = 1/1000 · µ = 1/1 000 000."),
        blk("block", label="A", titel="Größen und Geräte"),
        table([["Messgröße", "Einheit", "Messgerät"],
               ["Länge", "", ""], ["Masse", "", ""], ["Zeit", "", ""], ["Temperatur", "", ""]]),
        task("Ergänze die Tabelle.",
             solution="Länge: Meter (m), Lineal/Maßband; Masse: Kilogramm (kg), Waage; "
                      "Zeit: Sekunde (s), Stoppuhr; Temperatur: Grad Celsius (°C), Thermometer."),
        match("Ordne Größe und Einheit zu:", [
            ("Länge", "Meter (m)"),
            ("Masse", "Kilogramm (kg)"),
            ("Zeit", "Sekunde (s)"),
            ("Temperatur", "Grad Celsius (°C)"),
        ]),
        blk("block", label="B", titel="Vorsätze"),
        task("Rechne um: 2500 m in km, 0,3 A in mA, 450 mg in g, 2,5 kV in V.",
             solution="2,5 km; 300 mA; 0,45 g; 2500 V."),
        cloze("1 km sind [1000] m. 1 mA sind [0,001] A. Die Einheit der Masse ist "
              "[Kilogramm]."),
        mc("Welche Angabe ist vollständig?",
           [("12,5 cm", True), ("12,5", False), ("cm", False), ("12,5 Grad", False)]),
    ], "k7-p5"),
])

# ---------------------------------------------------------------- Blatt 6
s6 = sheet("Messgeräte 2 – Temperatur messen", [
    page([
        header("Messgeräte 2 – Temperatur messen"),
        ziel("Du kannst eine Messreihe durchführen, Messwerte in einer Tabelle "
             "festhalten und daraus ein Diagramm zeichnen."),
        info("Thermometer nutzen die **Ausdehnung** von Flüssigkeiten oder die "
             "Spannung eines Sensors. Eine Skala muss **geeicht** sein, sonst sind "
             "die Werte nicht vergleichbar.", heading="Wie misst man Temperatur?"),
        blk("block", label="A", titel="Versuch: Erwärmen"),
        versuch("Versuch: Wasser erwärmen",
                "Becherglas, Wasser, Thermometer, Heizplatte, Stoppuhr.",
                ["200 ml Wasser in das Becherglas geben.",
                 "Thermometer eintauchen und Starttemperatur ablesen.",
                 "Alle 2 Minuten die Temperatur messen und notieren."],
                lines_b=2, lines_a=2, auswertung=""),
        table([["Zeit in min", "0", "2", "4", "6", "8", "10"],
               ["Temperatur in °C", "", "", "", "", "", ""]]),
        blk("block", label="B", titel="Auswerten"),
        axes("t in min", "T in °C", xmax=10, ymax=100, xstep=2, ystep=10,
             caption="Erwärmungskurve"),
        task("Zeichne die Messwerte in das Diagramm und beschreibe den Verlauf.",
             solution="Die Temperatur steigt zunächst gleichmäßig an; die Kurve "
                      "flacht bei Annäherung an den Siedepunkt ab."),
        task("Ein Thermometer zeigt bei Eiswasser 3 °C statt 0 °C. Was bedeutet das "
             "für alle Messwerte?",
             solution="Das Thermometer ist falsch geeicht; alle Werte sind um 3 °C "
                      "zu hoch und müssen korrigiert werden."),
        mc("Was gehört zu einer guten Messreihe?",
           [("Mehrere Messungen und ein Mittelwert.", True),
            ("Nur ein einziger Wert.", False),
            ("Angabe ohne Einheit.", False),
            ("Messung ohne Gerät.", False)]),
        signature(),
    ], "k7-p6"),
])

BACKUP = {
    "app": "arbeitsblatt-studio",
    "version": 2,
    "exportedAt": NOW,
    "folders": [{"id": FOLDER_ID, "name": "Klasse 7"}],
    "prefs": {"view": "grid", "sort": "updated"},
    "sheets": [s1, s2, s3, s4, s5, s6],
}

with open("Klasse7_Akustik_Messgeraete.json", "w", encoding="utf-8") as f:
    json.dump(BACKUP, f, ensure_ascii=False, indent=2)

print("OK:", len(BACKUP["sheets"]), "Blätter")
for s in BACKUP["sheets"]:
    print(" -", s["title"], f"({sum(len(p['blocks']) for p in s['pages'])} Bausteine)")
