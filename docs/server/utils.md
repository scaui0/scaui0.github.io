# Hilfsmittel

!!! todo "Besserer Name"

    Diese Seite braucht einen besseren Namen, der beschreibt, was in ihr steht.

Der Server würde ohne einige Hilfsmittel nicht so gut laufen, wie er es tut.

## Der Move-Pruner

Der Move-Pruner vereinfacht Züge. Er basiert darauf, dass Züge in sogenannte *Gruppen* zerlegt werden, die dann wieder
zu Zügen zusammengesetzt werden.

Eine Gruppe besteht dabei aus den Bewegungen zweier gegenüberliegenden Seiten. Nach einer Gruppe muss immer eine Gruppe
anderen Typs kommen, also nach einer Gruppe `{R: 1, L:2}` muss eine Gruppe kommen, die keine `L` und `R` Züge mehr hat.

Dann werden die Gruppen wieder in Züge umgewandelt, indem für jede Gruppe nacheinander die Anzahl der Rotationen Modulo
4 gerechnet wird. Dann wird die Seite plus ein Modifikator (`2` und `'`) für die Rotationen 2 und 3 hinzugefügt.

Dadurch verringert sich die Länge der Zugfolgen durchschnittlich um ein Viertel ($\frac{76}{100}$). Dieser Wert stammt
aus einem Test mit 1 000 verschiedenen zufälligen Zugfolgen der Länge 100.

## Farbkorrigierer

Da die Farben von der [Farberkennung](../color_detection.md) selten zu 100 % stimmen, korrigiert dieser Algorithmus
die Farben, indem er je eine der überschüssigen Farben einer Defizitfarbe zuordnet.

Als Erstes werden die Positionen der Farben, die zu häufig vorkommen, gespeichert, ebenso wie die Farben, die es zu
wenig gibt (Defizitfarben), und die Anzahl, die sie mehr vorkommen müsste.

Dann wird für jede Position der Farben, die es zu viel gibt, die Wahrscheinlichkeit der Zugehörigkeit zu den
Defizitfarben berechnet.

Als Erstes wird die Zu-Viel-Farbe genommen, die die größte Wahrscheinlichkeit hat, zu einer der Defizitfarben zu passen,
und, sortiert nach Wahrscheinlichkeit der Zugehörigkeit zur Defizitfarbe, alle Wahrscheinlichkeiten durchgegangen. Wenn
die Farbe zu einer Defizitfarbe passt und die Defizitfarbe immer noch eine ist (nicht schon vorher aufgefüllt wurde),
wird das Feld zu der Defizitfarbe geändert und die Bestände aktualisiert.

Am Ende sollte es keine Defizitfarbe mehr geben. Da es immer noch die Wahrscheinlichkeit gibt, dass die Farben nicht
stimmen, wird in einem solchen Fall der Würfel noch einmal eingescannt.
