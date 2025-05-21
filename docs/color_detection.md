# Farberkennung

Die RGB-Werte[^1], die von Roboter eingescannt werden, müssen vor dem Lösen des Würfels noch in die programm-internen
Farben umgewandelt werden. Die Farben, die erkannt werden müssen, sind Weiß, Gelb, Grün, Blau, Rot und Orange.

Die Farbstruktur ist eine Liste mit Länge 54 von RGB-Werten. Es gibt von jeder Farbe exakt 9 Farbwerte.

## Erkennen mit KI

Die KI (neuronales Netzwerk) sortiert die Farben basierend auf verschieden mathematischen Rechnungen, die im Training
herausgefunden wurden. Die KI bekommt die RGB-Werte der Farbe und muss basierend darauf eine Schätzung abgeben, welche
Farbe es ist. Diese Schätzung ist die Wahrscheinlichkeit für jede einzelne Farbe.

Trainiert wurde die KI mit 100 Würfeln, die zuvor eingescannt wurde.

Da die KI mit echten Daten trainiert wurde, kann sie die Farben meist richtig erkennen, allerdings auch nicht zu 
100 %, deshalb wende ich nach dem Erkennen noch meinen [Farbkorrigierer](server/utils.md#farbkorrigierer) an.

## Algorithmisches Erkennen

Dieser Algorithmus sortiert die Farben basierend auf verschiedenen Kriterien, die nacheinander verschiedene Farben
zuordnet. Leider ist der Algorithmus sehr ungenau und ordnet die Farben Rot, Orange und Gelb oft einer falschen Farbe
zu. Daher wird er aktuell nicht verwendet.

### Schritt 1 - Weiß und Gelb

Als Erstes werden die Positionen von Weiß und Gelb in der Ausgangsliste gefunden.

Dazu werden als Erstes die 18 Positionen mit der größten Summe der RGB-Werte gefunden und der Reihe nach durchgegangen.
Die Summe der RGB-Werte wird deshalb genutzt, weil Weiß und Gelb in allen Farbkanälen sehr hohe Werte haben.
Um zu unterscheiden, ob der aktuelle Wert jetzt weiß oder gelb ist, wird geguckt, ob
die [Sättigung](https://de.wikipedia.org/wiki/Farbs%C3%A4ttigung) des Wertes in der oberen oder unteren Hälfte der
Sättigungen der RGB-Werte liegt. Liegt sie unten, so ist die Farbe Weiß, liegt sie oben, ist es Gelb. Das liegt daran,
dass Gelb eine höhere Sättigung als Weiß hat.

Wenn eine Farbe erkannt wurde, wird sie aus den noch zu verarbeitenden Farben entfernt und an der passenden Stelle im
Ergebnis eingefügt.

### Schritt 2 - Grün und Blau

Im zweiten Schritt wird davon ausgegangen, dass die Werte, die die größte Summe von Grün- und Blaukanälen haben, auch
Grün und Blau sind. Um sie zu unterscheiden, werden die Farben nach Blaukanal sortiert. Die 9 Farben mit dem größten
Blaukanal sind Blau, die anderen 9 Grün.

Dann werden die gefundenen Farben wieder aus der noch zu verarbeitenden Liste entfernt und ins Ergebnis eingefügt.

### Schritt 3 - Rot und Orange

Im letzten Schritt werden die noch verbleibenden Elemente nach Rot oder Orange sortiert. Dabei spielt die Differenz
zwischen Grün- und Blaukanal eine große Rolle: Wenn sie klein ist, ist die Farbe Rot, sonst Orange. Das liegt daran,
dass Orange zusätzlich zum Rot auch noch etwas Grün braucht, und somit der Grünkanal größer ist.

[^1]: RGB: Red-Green-Blue, eine Farbskala auf der jeder der drei Farbkanäle einen Wert von 0 - 255 hat.
