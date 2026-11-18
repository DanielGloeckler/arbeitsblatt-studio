# Arbeitsblatt-Studio

**Live:** https://monographix25.github.io/arbeitsblatt-studio/

Beim ersten Start sind die **sechs Klasse-7-Blätter** (Akustik 1–4,
Messgeräte 1–2) bereits im Ordner **Klasse 7** enthalten – kein Import nötig.
Zusätzlich liegt das Backup unter `import/Klasse7_Akustik_Messgeraete.json`
(auch online abrufbar) und lässt sich über „Backup laden" in einen anderen
Browser übernehmen.

Arbeitsblätter im Baukastenprinzip erstellen – eine einzige `index.html`, kein
Server, kein Build, kein Login.

## Veröffentlichen (GitHub Pages)

1. `index.html` in ein Repository legen (z. B. ins Hauptverzeichnis oder nach `docs/`).
2. Im Repository: **Settings → Pages**.
3. Unter *Source* den Branch (`main`) und den Ordner (`/ (root)` bzw. `/docs`) wählen.
4. Speichern – nach etwa einer Minute ist die Seite unter
   `https://<benutzername>.github.io/<repo>/` erreichbar.

Es ist keine weitere Konfiguration nötig: kein Node.js, kein Build-Schritt,
keine Serverfunktionen. Die Datei läuft genauso per Doppelklick lokal.

## Funktionsumfang

**Dashboard „Eigene Materialien"**
- **Neues Arbeitsblatt** öffnet einen Dialog mit **sechs Layout-Vorschauen**
  (Klassisch, Balken, Rahmen, Minimal, Frisch, Klar) – jede Karte zeigt eine
  echte Mini-Vorschau; dazu Titel, Fach und Klasse. Layout später jederzeit
  über „Design" änderbar.
- **KI-Assistent**: erzeugt aus Thema/Klasse/Seitenzahl ein fertiges Blatt
  (Vorschau → Übernehmen). Siehe Abschnitt „KI".
- **Ordner**: anlegen über „Ordner", umbenennen per Doppelklick, löschen über ✕.
  Jede Karte hat ein Ordner-Menü, die Filterleiste zeigt „Alle", „Ohne Ordner"
  und jeden Ordner mit Anzahl.
- **Sortierung**: zuletzt bearbeitet, zuletzt erstellt oder Titel A–Z.
- Suche über Titel, Fach, Klasse und Inhalte, Filter für Fach und Klassenstufe
- Kachel- oder Listenansicht, Kacheln mit echter Mini-Vorschau des A4-Blatts
- Bearbeiten, Duplizieren, Löschen
- Beim ersten Start drei fertige Beispiel-Arbeitsblätter (Physik/NWT)

**Editor**
- **Fächer**: Physik und NWT.
- **Kopfzeile in vier Designs**: Klassisch, Balken (schwarzes Band),
  Rahmen, Minimal – umschaltbar in den Baustein-Einstellungen, mit Schaltern
  für Name, Klasse und Datum sowie **Schullogo** (Upload, Höhe in mm).
- **Vier Seiten-Designs** von verspielt bis clean: *Vorlage* (schwarz/weiß,
  Rahmen 1 cm vom Rand, Kopfzeile Klasse/Fach/Datum, schwarze Titelkästchen,
  Helvetica – entspricht `arbeitsblatt.sty`), *Verspielt* (Klasse 5–7),
  *Freundlich* (7–9), *Sachlich* (9–11), *Clean* (11–13).
- **Mehrere Seiten**: „Neue Seite" links, „+ Seite" an jeder Seitenleiste,
  Seite löschen mit Rückgängig. Aufgaben werden über alle Seiten durchgezählt.
- **Bausteine** (links): Kopfzeile, Überschrift & Text (normal/Merke/Info/Tipp),
  Aufgabenblock (Nummer `A 1`, **Teilaufgaben a) b) c)**, Lösung – **ohne
  Punkte**),
  Lückentext (`[Wörter]`, **auch mit Formeln** `$…$`), Schreiblinien/Karopapier,
  Multiple-Choice, **Tabelle** (Zeilen/Spalten frei), Bild, **QR-Code**,
  **Punktesumme**, **Formel** (abgesetzt, LaTeX), **Begriffsdefinition**,
  **Zitat / Textquelle**, **Sortieraufgabe** (Kästchen zum Eintragen),
  **Quellcode**, **Unterschrift**, **Abstand** (Leerraum, optional bis zum
  Seitenende), **Versuch** (Material, Durchführung, Beobachtung, Auswertung),
  **Messwerttabelle**, **Koordinatensystem** (Achsen, Bereiche, Legende,
  Vorlagen für s-t, v-t, U-I, Temperatur-Zeit und Kraft-Weg),
  **Zahlenstrahl**, **Formelsammlung** (Name + Formel), **Schaltplan**
  (Batterie, Lampe, Schalter, Widerstand), **Notenspiegel**, **Zeitplan**,
  **Wörter zuordnen** (zwei Spalten zum Verbinden, Lösungen in der
  Lehrerversion) und **Wortsuchrätsel** (aus Wortliste, Lösungen markiert).
  Bausteine lassen sich **aus der linken Leiste direkt ins Blatt ziehen** – die
  grüne Linie zeigt die Einfügestelle, auch auf einer anderen Seite. Ein Klick
  fügt weiterhin am Ende ein.
- **Direkt auf dem Blatt bearbeiten**: Klick **irgendwo in einen Baustein** –
  egal ob auf die Textzeile oder in die Kastenfläche – der Text wird editierbar.
  Zusätzlich **Doppelklick** auf den Baustein oder das **Stift-Symbol** in der
  Werkzeugleiste. Klick daneben speichert und rendert. Fett `**…**`, kursiv
  `*…*`, Code `` `…` ``, Formeln `$…$` bzw. `$$…$$` (KaTeX). Gespeichert wird
  **während des Tippens**, nicht erst beim Verlassen des Feldes.
- **Formel-Werkzeugleiste** über dem Feld: **F**, *I*, ∑ (inline), ∑⁄ (abgesetzt).
  Strg+B / Strg+I funktionieren ebenfalls.
- **Bilder flexibel**: Breite 10–100 %, Ausrichtung, Ersetzen/Entfernen,
  Einfügen per Datei, **Strg+V** oder **Drag & Drop** auf das Blatt.
  **Am Bild selbst ziehen** – es löst sich dabei automatisch aus dem Textfluss
  und lässt sich danach direkt weiter verschieben (kein Griff nötig).
  Bildunterschrift und Quelle lassen sich **abschalten**.
- **QR-Code flexibel**: Größe 12–60 mm, **Text an/aus**. Ohne Text ist es ein
  kompakter Block, der sich frei verschieben lässt (auch als kleiner Aufkleber
  neben einer Aufgabe). Mit **„Frei positionieren“** wird das Bild
  aus dem Textfluss gelöst: im Blatt mit der Maus **ziehen**, Ecke unten rechts
  ändert die Größe. Koordinaten werden in mm gespeichert und drucken identisch.
- **Bausteine frei positionieren**: **jeder** Baustein lässt sich am **Griff ⠿**
  frei im Blatt verschieben – beim ersten Ziehen löst er sich automatisch aus
  dem Textfluss. Ecke unten rechts ändert die Breite. Über das Häkchen
  „Frei positioniert" geht es auch zurück in den Textfluss; Bilder lassen sich
  direkt ziehen.
- **Führungslinien & Einrasten**: beim Ziehen erscheinen gestrichelte Linien an
  beiden Seitenrändern und in der Mitte, dazu die Kanten/Mitten der anderen
  Bausteine. Innerhalb von 2 mm rastet der Baustein ein (grüne Linie). Über dem
  Baustein steht live der Abstand **links und rechts in mm**.
- **Reihenfolge**: Pfeiltasten im Baustein (↑ ↓) verschieben ihn schrittweise,
  am Seitenrand auf die Nachbarseite.
- **Baustein auswählen** → rechte Spalte zeigt seine Einstellungen
  (Darstellung, Punkte, Teilaufgaben, Zeilen, Bildbreite …).
  Neue Bausteine werden **nach dem ausgewählten** eingefügt.
- **Dokument**: Titel, Fach, Klassenstufe, Schriftart, Seitenrand (Preset **und**
  je Seite in mm), **Fußzeile mit Platzhaltern** `{Fach} {Klasse} {Titel} {Seite} {Seiten}`.
- **Schüler-/Lehrerversion** als Umschalter: Lösungen rot, Lückentexte mit
  eingesetzten Wörtern, richtige Antworten markiert.
- Strg+S speichert sofort, sonst automatisch nach kurzer Pause.

**Export**
- **Als PDF / Drucken**: erzeugt beim Druck eine frische, saubere Kopie des
  Blattes (`#print-root`) – ohne Seitenleisten, Zoom, Auswahlrahmen oder aktive
  Eingabefelder. Eine Blattseite = eine PDF-Seite, Fußzeile unten.
- **LaTeX-Code anzeigen**: aufklappbares Fenster mit dem kompletten `.tex`-Code
  (eigenständige Präambel, kompiliert z. B. in Overleaf) – zum Kopieren oder als
  `.tex`-Datei. Bilder erscheinen dort als Platzhalter, weil sie im Browser
  eingebettet sind.
- **LaTeX übernehmen** (Button „LaTeX" im Dashboard): `.tex`-Datei wählen oder
  Code einfügen → daraus werden bearbeitbare Bausteine. Erkannt werden
  Absätze, `\section`/`\subsection`, `itemize`/`enumerate`, Formeln
  (`$…$`, `\[…\]`), `tcolorbox` und Textformatierung (`\textbf`, `\emph`, …).
  Der Import ist eine Heuristik – danach normal weiterbearbeiten.
- **HTML-Datei exportieren**: eigenständige Datei mit allen Seiten.
- **Backup sichern / laden**: alle Arbeitsblätter als JSON.

## Druckhinweise

- Chrome oder Edge verwenden.
- Der Druck ist **randlos** (`@page margin: 0`), die Ränder stecken im Blatt.
  Dadurch bleibt unten kein Dateipfad und kein Seitenzähler des Browsers stehen.
  Falls doch etwas erscheint, im Dialog **„Kopf- und Fußzeilen"** ausschalten.
- Im Druckdialog **„Hintergrundgrafiken"** aktivieren, sonst verlieren Merke-,
  Info- und Tabellenflächen ihre Farbe.
- Formeln werden als HTML gerendert; die KaTeX-Schrift kommt beim ersten Laden
  aus dem Netz.

## Datenspeicherung

Alles liegt im `localStorage` des Browsers – nichts wird hochgeladen, es gibt
kein Konto.

| Schlüssel | Inhalt |
| --- | --- |
| `arbeitsblatt-studio.v1` | Arbeitsblätter, Ordner, Ansicht/Sortierung |
| `abw.ai` | KI-Einstellungen (Base-URL, Modell) – kein Key |
| `abw.ai.key.ss` | API-Key, **nur diese Sitzung** (Standard) |
| `abw.ai.key.ls` | API-Key, dauerhaft – nur wenn du es anhakst |
| `abw.printHint` | Merker für den Druckhinweis |

Daraus folgt:

- Daten gelten **pro Browser und pro Adresse**. Ein anderer PC, ein anderer
  Browser oder ein Wechsel von `file://` zu `https://` sieht andere Daten.
- Deshalb regelmäßig **Backup sichern** und auf dem Zielgerät **Backup laden**.
- **Der API-Key ist nie im Backup** und nie in den Blättern.
- Der Speicher fasst je nach Browser etwa 5 MB. Bilder werden vor dem Speichern
  auf maximal 1400 px verkleinert und als JPEG komprimiert.
- Inkognito-Fenster und „Browserdaten löschen" entfernen die Arbeitsblätter.

## KI-Assistent

- Button **„KI"** im Dashboard. Einstellungen: Base-URL, Modell, API-Key.
  **„Verbindung testen"** prüft Key und Modell mit einer Mini-Anfrage.
- Standard ist **OpenRouter** (`https://openrouter.ai/api/v1`, Modell
  `openai/gpt-4o-mini`) – läuft direkt aus dem Browser. Jeder OpenAI-kompatible
  Anbieter funktioniert.
- Der Key wird **nie** in die Datei geschrieben, nie geloggt, nie ins Backup
  übernommen und nur an die eingetragene Base-URL gesendet. Standard ist
  „nur diese Sitzung"; dauerhaft speichern nur per Häkchen (nicht auf fremden
  Rechnern).
- Die Antwort wird **streng geprüft** (nur bekannte Bausteintypen, Längen- und
  Zahlenlimits), dann als Vorschau gezeigt. Erst „Übernehmen" legt das Blatt an.
- Inhalt immer fachlich prüfen – das Modell kann Fehler erfinden.

## Technik

- Eine Datei, ca. 90 KB, kein Build.
- Tailwind CSS, Lucide Icons, KaTeX und qrcode-generator über CDN
  (`cdn.tailwindcss.com`, `unpkg.com/lucide@latest`, `cdn.jsdelivr.net`).
  Beim ersten Aufruf wird eine Internetverbindung benötigt.
- Das Blatt selbst nutzt **keine** Tailwind-Klassen, sondern eigene `ab-*`-Klassen.
  Dadurch sehen Bildschirm, PDF und HTML-Export identisch aus.
- Direktlinks auf ein Blatt: `#editor/<id>`.

## Grenzen

- Keine Zusammenarbeit, keine Cloud-Synchronisierung, keine Konten.
- Keine freie Positionierung/Layer – Bausteine fließen wie Text. Genau dadurch
  kann nichts verrutschen.
- Nur A4 Hochformat; Querformat/Präsentation gibt es (noch) nicht.
- Kein Kreuzworträtsel, Wortsuchrätsel, Zuordnung oder Notenspiegel
  (bei tutory vorhanden, hier bewusst noch nicht).
- Bilder liegen im Dokument (deshalb die Größenbegrenzung).
