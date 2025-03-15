---
title: Löser
---

# Löse-Methoden

Um einen Zauberwürfel zu lösen, gibt es verschiedene Methoden, die alle ihre Vor- und Nachteile haben.


!!! danger "Umstrukturierung"

    Diese Seite mitsamt ihren Unterseiten braucht eine umfassende Umstrukturierung. Dabei soll möglichst nach folgenden
    Punkten gearbeitet werden:
    
    * Link zum Originalprojekt, zu dem auch die PDBs gehören. Die PDBs auch als extern markieren.
    * Die genaue Funktionsweise grob erklären (Koordinatenberechnung).
    * Kociembas Algorithmus hinzufügen.

## IDA\*

[↳ Siehe IDA\*](ida_star.md)

Die folgenden Algorithmen basieren auf einer Tiefensuche mit Heuristik, die unwahrscheinliche Zugfolgen nicht weiter
durchsucht.

## Korfs Algorithmus

[↳ Siehe Korfs Algorithmus](korf.md)

Korfs Algorithmus ist eine Lösemethode für Zauberwürfel, der die optimale Lösung (maximal 20 Züge) findet, aber viel
Zeit benötigt.

## Thistlethwaite Algorithmus

[↳ Siehe Thistlethwaite Algorithmus](thistlethwaite.md)

Thistlethwaite Algorithmus ist eine Lösemethode, die den Lösevorgang in verschiedene Gruppen unterteilt, die die
jeweiligen Würfelzustände reduziert, damit der Würfel im nächsten Löseabschnitt schneller gelöst werden kann. Dadurch
wird die Lösung zwar schneller gefunden, braucht aber eventuell ein wenig mehr Züge (maximal 46).
