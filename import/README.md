# Klasse 7 – fertige Arbeitsblätter

`Klasse7_Akustik_Messgeraete.json` ist ein **Backup** für das Arbeitsblatt-Studio.
Es enthält den Ordner **Klasse 7** und sechs Arbeitsblätter:

| Blatt | Thema | Inhalt |
| --- | --- | --- |
| Akustik 1 | Wie entsteht Schall? | Ziel, Infokasten, Stimmgabel-Versuch, Aufgaben, Lückentext, MC |
| Akustik 2 | Wie breitet sich Schall aus? | Vakuum-Versuch, Rechnen mit v = s/t, Gewitter/Echo, Diagramm |
| Akustik 3 | Amplitude und Frequenz | Merke, Schwingungsdiagramm, f = 1/T, Zuordnung, Tabelle |
| Akustik 4 | Hören, Lärm und Schallschutz | Ohr, Lärmbewertung, Schallschutz, Definition |
| Messgeräte 1 | Messgrößen und Einheiten | Größe/Einheit/Gerät, SI-Vorsätze, Zuordnung |
| Messgeräte 2 | Temperatur messen | Erwärmungsversuch, Messwerttabelle, Diagramm, Eichung |

Grundlage: Beispielcurriculum Physik Baden-Württemberg, Klasse 7
(4.1 Akustik, 4.2 Messgeräte entwickeln).

## Import in die App

1. `index.html` öffnen.
2. Dashboard → **Backup laden**.
3. Diese JSON-Datei wählen.

Die Blätter landen im Ordner **Klasse 7** und sind sofort bearbeitbar.
Der Import **ergänzt** die vorhandenen Blätter, er löscht nichts.

## Neu erzeugen

```
python build_klasse7.py
```

Das Skript schreibt die JSON-Datei neu (Inhalte stehen oben im Skript).
