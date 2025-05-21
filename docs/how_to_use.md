# Nutzung des Programms

Haben Sie sich im Verlaufe des Lesens gefragt, ob Sie mein Programm selbst testen können? Wenn ja, finden Sie hier einen
Weg, dies zu tun.

??? info "Aber ich habe keinen Roboter."
   
    Kein Problem, alle Programmteile, die einen Roboter benötigen, lassen sich auch mit meinem Roboter-Emulator nutzen.
    Statt einen Würfel einzuscannen, können Sie ihn einfach eingeben und dann lösen lassen. Das Ausführen der Lösung
    müssen dann leider Sie übernehmen.

## Installation

Mein Programm nutzt *Python*, eine interpretierte Programmiersprache, die für seine Dynamik bekannt ist. Installieren
Sie Python 3.12 oder neuer einfach von [python.org](https://python.org) herunter. Setzten Sie im folgenden
Installationsvorgang die Option `Add bin to PATH`.

Laden Sie dann das Programm von GitHub runter. Gehen Sie dazu auf
[github.com/scaui0/RubiksCubeSolver](https://github.com/scaui0/RubiksCubeSolver), klicken oben rechts auf den grünen
`Code`-Button und auf `Download ZIP`. Entpacken Sie anschließend die ZIP-Datei.

Öffnen Sie ein Terminal ihrer Wahl (z. B. Windows Eingabeaufforderung oder Bash) und navigieren Sie mittels `cd` in
den Pfad der entpackten ZIP-Datei. Beispiel: `cd "C://Users/xyz/Downloads/RCS"`.

Installieren Sie die benötigten Pythonmodule mit `pip install -r requirements.txt`. Wenn der Befehl fehlschlägt, können
Sie `python -m pip install -r requirements.txt` probieren.

Testen Sie das Programm mit `python main.py --help` bzw. `python3 main.py --help`.

??? info "Mehrere Pythonversionen"

    Sollten Sie mehrere verschiedene Pythonversionen nutzen, können Sie die richtige mit `python3` oder `python3.12`
    ansprechen. Ersetzten Sie in diesem Fall im weiteren Verlauf die Pythonversion im Befehl durch die Richtige
    (3.12 oder neuer).

Da mein Programm aus Performancegründen ein externes Programm zum Lösen nutzt, müssen Sie den CubeExplorer von
[kociemba.org/download.htm](https://kociemba.org/download.htm). Legen Sie die Programmdatei an einen Ort ihrer Wahl und
starten Sie sie. Gehen Sie nach dem Erstellen einiger benötigter Dateien auf *Options* --> *Web server* und setzten Sie
einen Haken bei *Enable Web Server*. Wenn Sie mein Programm nutzen, sollten Sie immer eine Instanz des Programms
geöffnet haben, damit mein Programm den `Cube Explorer` im Hintergrund per API nutzen kann.

## Befehle

Im Folgenden eine Liste mit Befehlen (erstellt von `python main.py --help`):
```
api-gui: Startet die API mit GUI.
```

Um sich die Optionen/Argumente der Befehle anzeigen zu lassen, können Sie `--help` anhängen.

## Die API mit GUI

Starten Sie die API mit integrierter GUI mit dem folgenden Befehl: `python main.py api-gui <host> <port>`.
Ersetzten Sie `<host>` durch Ihren Hostnamen (z. B. `203.0.113.10` oder `localhost`).
Standard ist `localhost`, also ihr eigener Computer.
Der Port-Standard ist `3457`.

Um die API automatisch starten zu lassen (sodass automatisch angefangen wird, den Würfel zu lösen), nutzen Sie die
Option `--auto`.

Der Aufbau:

![Der Aufbau der GUI](/images/api_gui_with_descriptions.png)

1. Der Solve-Button zum Lösen des aktuellen Würfels in Feld 6.
2. Der Scan-Button zum Auffordern des Clients zum Scannen.
3. Die aktuellen Züge.
4. Der Send-Button zum Ausführen der Züge.
5. Die aktuellen Farbwerte nach dem Einscannen.
6. Die ausgewerteten Farben.
7. CheckBox, um den automatischen Modus zu aktivieren.

Im automatischen Modus (Checkbox aktiviert) wird ein Würfel direkt gelöst und die Lösung zurückgeschickt. Im manuellen
Modus müssen Sie dazu auf die `Solve`- und die `Send`-Buttons klicken. Dafür können Sie dort auch ihre eigenen Züge
eingeben und so zum Beispiel Muster erzeugen.

## Die textbased API

Starten Sie sie mit `python main.py api`.
Da dieser Modus nicht für die Visualisierung gedacht ist, gibt es keine Option, das automatische Lösen zu deaktivieren.

