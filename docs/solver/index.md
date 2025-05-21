---
title: Löser
---

# Löse-Methoden

Um einen Zauberwürfel zu lösen, gibt es verschiedene Methoden, die alle ihre Vor- und Nachteile haben.

## Koordinaten-Berechnung

[↳ Siehe Koordinaten-Berechnung](coordinates.md)

Die Algorithmen berechnen einen eindeutigen Index aus den relevanten Strukturen des Würfels. Diese Funktion ist hier
näher beschrieben.

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

## Kociembas Algorithmus

Herbert Kociembas Algorithmus löst einen Zauberwürfel in unter 22 Zügen in wenigen Sekunden. Dabei werden Symetrien des
Würfels genutzt, also dass ein Würfel der gleiche ist, wenn man ihn dreht. Da mir dieser Algorithmus eine Nummer zu groß
war, habe ich die Cube-Explorer-API genutzt. Der Cube Explorer beinhaltet die originale Implementation des Algorithmus.
