# Custom Navigation

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - getting-started.md #(1)!
  - guides #(2)!
  - More Resources: #(3)!
    - "*" #(4)!
    - MkDocs: https://mkdocs.org #(5)!
```

1. Insert individual pages  
    [Read more below :material-arrow-down:](#)
2. Insert entire directories as sections  
    [Read more below :material-arrow-down:](#)
3. Create sections  
    [Read more below :material-arrow-down:](#)
4. Insert all files and directories that match glob patterns  
    [Read more below :material-arrow-down:](#)
5. Create external links  
    [Read more below :material-arrow-down:](#)

```title="File Structure"
docs/
├─ .nav.yml
├─ getting-started.md
├─ support.md
└─ guides/
   ├─ authentication.md
   └─ error-handling.md
```

Thistlethwaite Algorithmus ist eine Lösemethode, die den Lösevorgang in verschiedene Gruppen unterteilt, die die
jeweiligen Würfelzustände reduziert, damit der Würfel im nächsten Löseabschnitt schneller gelöst werden kann. Dadurch
wird die Lösung zwar schneller gefunden, braucht aber eventuell ein wenig mehr Züge (maximal 46).


</div>


## Pages

Reference a markdown file to insert that page into that spot in the navigation:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - support.md
```

```title="File Structure"
docs/
├─ .nav.yml
└─ support.md
```

- Support
</div>

The markdown file can be located in a different directory:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - help/support.md
```

```title="File Structure"
docs/
├─ .nav.yml
└─ help/
   └─ support.md
```

- Support
</div>

You can also override the title that is displayed in the navigation:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - Help: support.md
```

```title="File Structure"
docs/
├─ .nav.yml
└─ support.md
```

- Help
</div>
