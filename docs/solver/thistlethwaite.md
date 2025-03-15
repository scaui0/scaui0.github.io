# Thistlethwaite Algorithmus

!!! info "Leichte Abweichungen zum Original"

    Der Algoritmus, den ich verwende unterscheidet sich vom Original insofern, dass er in Schritt 3 eine andere 
    Strategie nutzt. Mehr dazu unten.

Der Thistlethwaite Algorithmus teilt den Löseprozess in vier Schritte, in denen der Würfel nur begrenzte Variationen
haben kann, und damit im nächsten Teil schneller gelöst werden kann.

Die schlechteste Lösung sind 46 Züge, im Original aber 52.

## Funktionsweise

Thistlethwaites Algorithmus funktioniert – wie auch schon Korfs – mit IDA\*.

Anders als Korfs Algorithmus gibt es hier verschiedene Schritte, in denen der Würfel nur noch begrenzte Möglichkeiten
der Verdrehung hat.

## Die Schritte

Die verschiedenen Gruppen von Würfelzuständen werden als *group* bezeichnet. Daher kommen auch die Namen `G0` bis `G4`.
Die Programmschritte, um zu diesen Zuständen zu kommen, werden benannt nach ihren Zielgruppen. Jede Gruppe nutzt ihre
eigene Pattern-Database.

Die erste Gruppe `G0` ist ein beliebig verdrehter Würfel. Da jede Kante eine von zwei Orientierungen haben muss und
diese ohne die Viertelzüge der Vorder- und Rückseite nicht verändert werden können, kann man, wenn man die Kanten im
ersten Schritt löst, diese Züge in der restlichen Lösung weglassen. Am Ende von Schritt `G1` sind die Kanten richtig
orientiert.

Im nächsten Schritt (`G2`) werden die Ecken orientiert und zusätzlich die Kanten an die Positionen FR, FL, BL und BR
gebracht. Dadurch verringert sich die Menge der verschiedenen Züge und F, F', B und B'.

Schritt 3 unterscheidet sich von Thistlethwaites Algorithmus. Das Original nutzt eine Reihe von vorbereiteten Zügen, um
zu prüfen, wie die Cubies innerhalb ihrer Tetraden positioniert sind. (Die Ecken `{ULB, URF, DLF, DRB}` bilden eine
Tetrade, `{URB, ULF, DLB, DRF}` die andere). Diese Implementierung nutzt die Technik von Stefan Pochmann, die die Ecken
paart, wobei sichergestellt wird, dass `{ULB, URF}`, `{DLF, DRB}`, `{URB, ULF}` und `{DLB, DRF}` innerhalb der
jeweiligen Tetrade gepaart sind. Gleichzeitig wird die Parität der Ecken gerade, was bedeutet, dass die Ecken mit einer
geraden Anzahl an Vertauschungen gelöst werden können. Wenn die Parität der Ecken gerade ist, ist es die Parität der
Kanten auch. In dem Schritt werden die Kanten der M- und S-Scheibe auch richtig positioniert. In Gruppe `G2` sind die
Ecken bereits richtig ausgerichtet, sodass es ohne die Vierteldrehungen von L und R geht. Maximal 10 Züge.

| Gruppe | Erlaubte Züge                                                                                        | Maximale Züge |
|--------|------------------------------------------------------------------------------------------------------|---------------|
| `G1`   | `L`, `L'`, `L2`, `R`, `R'`, `R2`, `U`, `U'`, `U2`, `D`, `D'`, `D2`, `F`, `F'`, `F2`, `B`, `B'`, `B2` | 7             |
| `G2`   | `L`, `L'`, `L2`, `R`, `R'`, `R2`, `U`, `U'`, `U2`, `D`, `D'`, `D2`, `F2`, `B2`                       | 10            |
| `G3`   | `L2`, `R2`, `U`, `U'`, `U2`, `D`, `D'`, `D2`, `F2`, `B2`                                             | 14            |
| `G4`   | `L2`, `R2`, `U2`, `D2`, `F2`, `B2`                                                                   | 15            |
