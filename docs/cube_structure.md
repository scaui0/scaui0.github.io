# Würfelstruktur

Der Zauberwürfel besteht aus einer 3x3 Struktur, bei der man die einzelnen Ebenen drehen kann. Für die Arbeit mit dem
Zauberwürfel ist es wichtig, die verschiedenen Teile, wie die Bewegungen und die Ecken auseinanderhalten zu können.

## Die Züge

Jeder Seite ist ein Buchstabe zugeordnet. Schreibt man diesen Buchstaben, so meint das, dass die jeweilige Seite im 
Uhrzeigersinn (von der jeweiligen Seite aus geschaut) gedreht werden soll.

| Buchstabe | Seite (englisch) | Seite (deutsch) |
|-----------|------------------|-----------------|
| U         | Up               | Oben            |
| D         | Down             | Unten           |
| L         | Left             | Links           |
| R         | Right            | Rechts          |
| F         | Front            | Vorne           |
| B         | Back             | Hinten          |

Wenn die Seite nicht nur 90° im Uhrzeigersinn drehen will, kann man der Seite ein Zeichen hinzufügen. Ein `'` meint, 
dass die Seite 90° gegen den Uhrzeigersinn gedreht werden soll, und eine `2` bedeutet, dass die Seite um 180° gedreht 
werden soll.

Wenn man die Seite mit der jeweiligen mittleren Ebene drehen will, kann die Seite kleingeschrieben werden.

Die mittleren Ebenen alleine werden durch die Buchstaben `S`, `E` und `M`.

| Buchstabe | Folgt welcher Seite |
|-----------|---------------------|
| S         | F                   |
| E         | D                   |
| M         | L                   |

Tipp zum Merken: `S` ist im Alphabet näher an `F` als `B`. Das ist bei allen Ebenen so.

Die Buchstaben `x`, `y` und `z` drehen den Würfel um die entsprechenden Achsen.

## Die Ecken

Eine Ecke wird mit den drei Buchstaben der Seiten, an die sie grenzt, bezeichnet. Also ist die obere-rechte-vordere
Ecke `URF`.

## Die Kanten

Die Kanten werden ähnlich wie die Ecken mit den Buchstaben der Seiten bezeichnet, an die sie angrenzt. Beispiel: die 
Kante vorne-rechts ist `FR`.

## Würfel überprüfen

Da der Würfel eine bestimmte Struktur hat, die genau eingehalten werden muss, wird an einigen Stellen des Programms 
geprüft, ob der Würfel auch wirklich existieren kann. Dafür gibt es mehrere Kriterien:

* Die Summe der Kantenorientierungen muss immer eine gerade Zahl sein (durch 2 teilbar).
* Die Summe der Eckenorientierungen muss immer durch 3 teilbar sein.
* Die Parität der Ecken muss der der Kanten entsprechen.

Die Parität ist die Anzahl an Vertauschungen einer Permutation, bis diese gelöst ist. Die Parität kann entweder gerade
oder ungerade sein. Die Paritäten müssen übereinstimmen, weil bei einer Bewegung des Würfels immer Ecken und Kanten 
gedreht werden.

??? info "Videoerklärung"
    
    Die ersten 7 Minuten dieses Videos reichen, um in dieses Thema etwas tiefer einzusteigen.

    <div class="youtube-wrapper">
      <iframe 
        class="youtube-embed"
        src="https://www.youtube.com/embed/3BaZ3SkTfc0?rel=0"
        allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
      </iframe>
    </div>
