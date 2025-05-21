# Über diese Dokumentation

Diese Dokumentation basiert auf Markdown, einer Auszeichnungssprache, die in Plain-Text geschrieben wird. Sie beinhaltet
Strukturen wie Überschriften oder Tabellen.

## Material for Mkdocs

Diese Dokumentation wurde mit *Material for Mkdocs* erstellt. Material for Mkdocs ist ein Theme for Mkdocs, das dieses
schöne Design und die Suche bereitstellt. Mkdocs ist ein Programm, das aus verschiedenen Markdown-Dateien die 
Dokumentation zusammenstellt, so dass sie im Browser angezeigt werden kann.

[Mkdocs](https://mkdocs.org){ .md-button }
[Material for Mkdocs](https://squidfunk.github.io/mkdocs-material){ .md-button }

## Markdown

Markdown ist eine Auszeichnungssprache, die von John Gruber entworfen wurde. Sie kann von Menschen gelesen und
geschrieben werden. Die einzelnen Elemente sind strukturiert, es gibt z. B. Überschriften, die man klar als solche
erkennt.

Ein kleiner Einblick in die Markdown-Syntax:

| In Markdown                                                                  | Konvertiert zu HTML                                                        |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `[Link zu markdown](https://de.wikipedia.org/wiki/Markdown)`                 | [Link zu markdown](https://de.wikipedia.org/wiki/Markdown)                 |
| `[Link zu markdown](https://de.wikipedia.org/wiki/Markdown "Auf Wikipedia")` | [Link zu markdown](https://de.wikipedia.org/wiki/Markdown "Auf Wikipedia") |
| `*Kursiv*`                                                                   | *Kursiv*                                                                   |
| `**Fett**`                                                                   | **Fett**                                                                   |
| `***Beides***`                                                               | ***Beides***                                                               |
| `~~Durchgestrichen~~`                                                        | ~~Durchgestrichen~~                                                        |
| `` `Inline Code` ``                                                          | `Inline Code`                                                              |
| `CO~2~`                                                                      | CO~2~                                                                      |
| `km^2^`                                                                      | km^2^                                                                      |

### Code-Blöcke

Code-Block in Markdown:

````markdown
```python
def test(a, b):
    print(f"Summe aus a und b = {a+b}")
```
````

In formatiert:

```python
def test(a, b):
    print(f"Summe aus a und b = {a + b}")
```

### Tabellen

```markdown
| Linksbündig | Zentriert | Rechtsbündig |
|:------------|:---------:|-------------:|
| Zeile 1     |  Zeile 1  |      Zeile 1 |
| Zeile 2     |  Zeile 2  |      Zeile 2 |
```

| Linksbündig | Zentriert | Rechtsbündig |
|:------------|:---------:|-------------:|
| Zeile 1     |  Zeile 1  |      Zeile 1 |
| Zeile 2     |  Zeile 2  |      Zeile 2 |

## LaTeX

$\LaTeX$ ist ein Textformat, das meist genutzt wird, um mathematische Formeln darzustellen. Man kann es in Markdown
einbetten.

### Schreibweise

In $\LaTeX$ selbst existiert die Möglichkeit, das Logo mit `\LaTeX` darzustellen. Diese wird auch in dieser
Dokumentation genutzt.

Wer kein $\LaTeX$ nutzt, sollte stattdessen `LaTeX` schreiben.

### Aussprache

$\LaTeX$ wird \[ˈlaːtɛx] ausgesprochen. Da viele Leute das IPA (international phonetic alphabet, eine internationale
Liste der Lautschriftzeichen) nicht auswendig können, hier eine Beschreibung aus Deutsch: `Latäch`. Das `a` wird lang
gesprochen (deswegen auch das `ː`), das `ä` kurz und das `ch` wie das `ch` in `Bach`.

Auf Deutsch ist auch die Aussprache \[ˈlaːtɛç] (wieder `Latäch`) gebräuchlich. Der einzige Unterschied besteht darin,
dass das letzte Zeichen(`ç`) nicht wie das `ch` aus `Bach`, sondern wie das `ch` aus `Ich` gesprochen wird.
