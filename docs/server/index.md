# Der Server

Der Server ist der Teil des Projekts, der den Würfel löst.

Der Server läuft und wartet, bis sich ein Client (Roboter) verbindet. Dann sendet er die Konfiguration und wartet, bis
der Client Farben sendet, die der Server dann auswertet und den Würfel löst. Wenn der Würfel gelöst ist, sendet er ihn
zum Client zurück.

??? info "Ablaufdiagramm des Servers"

    ```mermaid
    graph TD
        A(Start) --> B[Warte auf Client]
        B --> C[Sende Konfiguration]
        C --> D[Warte, bis Client Farben schickt]
        D --> E[Werte Farben mit KI aus]
        E --> F{Ausgewerteter Würfel \nkann so existieren}
        F --> |Nein|G[Versuche Würfel zu korrigieren]
        F --> |Ja|I[Löse Würfel]
        G --> H{Würfel kann jetzt existieren}
        H --> |Ja|I
        H --> |Nein|K[Sende Client Aufforderung \nzum erneuten Einscannen]
        K --> D
        I --> L[Wandle die vereinfachten \nZüge in Roboter-Züge\n und schicke sie zum Client]
        L --> D
    ```
