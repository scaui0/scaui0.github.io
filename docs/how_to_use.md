# How to use

Haben Sie sich im Verlaufe des Lesens gefragt, ob Sie mein Programm selbst testen können? Wenn ja, finden Sie hier einen
Weg dies zu tun. 

??? info "Aber ich habe keinen Roboter."
    
    Kein Problem, alle Programmteile, die einen Roboter benötigen, lassen sich auch mit meinem Roboter-Emulator nutzen.
    Statt einen Würfel einzuscannen, können Sie ihn einfach eingeben und dann lösen lassen. Das ausführen der Lösung 
    müssen dann leider Sie übernehmen.

## Installation

Mein Programm nutzt *Python*, eine interpretierte Programmiersprache, die für seine Dynamik bekannt ist. Installieren 
Sie Python 3.12 oder neuer einfach von [python.org](https://python.org) herunter. Setzten Sie im folgenden 
Installationsvorgang die Option `Add bin to PATH`. 

Laden Sie dann das Programm von GitHub runter. Gehen Sie dazu auf [github.com/scaui0/RubiksCubeSolver], klicken oben
rechts auf den grünen `Code` Button und auf `Download ZIP`. Entpacken Sie anschließend die ZIP-Datei.

Öffnen Sie ein Terminal ihrer Wahl (z. B. Windows Eingabeaufforderung oder Bash) und navigieren sie mittels `cd` in 
den Pfad der entpackten ZIP-Datei. Beispiel: `cd "C://Users/xyz/Downloads/RCS"`.

Installieren Sie die benötigten Pythonmodule mit `pip install -r requirements.txt`. Wenn der Befehl fehlschlägt, können 
Sie `python -m pip install -r requirements.txt` probieren.

Testen Sie das Programm mit `python main.py --help` bzw. `python3 main.py --help`.

!!! info "Mehrere Pythonversionen"

    Sollten Sie mehrere verschiedene Pythonversionen nutzen, können Sie die richtige mit `python3` oder `python3.12` 
    ansprechen. Ersetzten Sie in diesem Fall im weiteren Verlauf die Pythonversion im Befehl durch die richtige 
    (3.12 oder neuer).

## Befehle

Im Folgenden eine Liste mit Befehlen:
```
api-gui: Startet die API mit GUI.
```

Um sich die Optionen/Argumente der Befehl anzeigen zu lassen, können Sie `--help` anhängen.

## Die API mit GUI

Starten Sie die API mit integrierter GUI mit dem folgenden Befehl: `python main.py api-gui`. Um die API automatisch 
starten zu lassen (sodass automatisch angefangen wird, den Würfel zu lösen) nutzen Sie die Option `--auto`.

Der Aufbau:

![]()

1. Automatischer Modus
2. Aktueller Würfel
3. Eingescannte Würfelfarben
4. Solve-Button
5. Züge
6. Send-Button, sendet Züge an den Client
7. Scan-Button

Im automatischen Modus (CheckBox aktiviert) wird ein Würfel direkt gelöst und die Lösung zurückgeschickt. Im manuellen 
Modus müssen Sie dazu auf die `Solve`- und die `Send`-Buttons klicken. Dafür können Sie auch ihre eigenen Züge eingeben.

## Die textbased Modus
