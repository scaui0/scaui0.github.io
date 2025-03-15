# Rubik's Cube Notation

Wenn man sich viel mus Zauberwürfeln auseinandersetzt, ist es sinnvoll, eine Notation für die einzelnen Züge zu haben.
Diese hier ist die allgemeine Notation von Zauberwürfelbewegungen.

## Einzelne Seiten

* `R - Right`
* `L - Left`
* `F - Front`
* `T - Top`
* `B - Back`
* `D - Down`

## Mehrere Seiten

Schreibt man die Buchstaben der Seiten klein, so meint das die Seite und die parallele mittlere Seite.

## Mittlere Ebenen

Die mittleren Ebenen sind `S`, `E` und `M`.

* `S` ist die mittlere Seite, die an `F` angrenzt. Sie wird in die gleiche Richtung wie `F` gedreht.
* `E` ist die horizontale Ebene. Sie wird wie `D` gedreht.
* `M` ist die letzte Ebene, sie wird in die gleiche Richtung wie `L` gedreht.

Merken kann man sich die Drehrichtungen, weil eine Seite immer nach der nächsten Seite im Alphabet gedreht wird.
So ist `S` im Alphabet näher an `F` als an `B` und `E` näher an `D` als an `L`.


## Den Würfel um Achse rotieren

Die Züge `x`, `y` und `z` drehen den Würfel um die entsprechenden Achsen.

## Gegen Uhrzeigersinn und mehrfach Drehen

Wenn man ein `'` hinzufügt, so meint man die gleiche Seite gegen den Uhrzeigersinn.

Fügt man eine `2` zu dem originalen Zug hinzu, so muss der Zug zweimal ausgeführt werden.
Kombinationen wie `F'2` machen keinen Sinn, da es eine 180° Drehung gegen den Uhrzeigersinn meint.

## Algorithmen

!!! warning "Allgemeinverständlichkeit nicht gewährleistet!"

    Diese Art, Algorithmen zu schreiben, wird möglicherweise nicht von allen verstanden! Passen Sie auf, wenn sie ihre
    eigenen Züge notieren und weitergeben, das die Zielperson(en) sie verstehen können!

Beispiel:

```
(F R F' R')2
```

Also den Algorithmus `F R F' R'` 2-mal ausführen.
