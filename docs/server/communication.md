# Kommunikation

Der Server kommuniziert mit dem Client (Roboter), um wichtige Informationen wie Konfiguration, Farben oder Züge zu übertragen.

## Die Roboter-Züge

Computer sind dumm. Der Roboter kann die Züge, die der Server nutzt, nicht ausführen und hat deshalb sein eigenes
Protokoll. Dieses basiert auf JSON und besteht aus mehreren Schritten, die nacheinander ausgeführt werden können.

Es gibt verschiedene Aktionen, die der Roboter kennt, wie `rotate_cube_with_arm`, `rotate_plate`, `arm_up` oder
`arm_down`.

Das Hauptobjekt ist eine Liste von verschiedenen Aktionen, die anhand ihres `type` unterschieden werden.

Im Folgenden alle Aktionen sortiert nach `type`:

| `type`                 | Beschreibung                                                                                                                                                                                        |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `rotate_cube_with_arm` | Rotiert den Würfel mit dem Arm `times`-Mal. `end` ist dabei die Endposition des Arms, 0 ist dabei unten (Default, Würfel kann frei rotieren) und 90 ist oben (obere Würfelseite wird festgehalten). |                                                                                                                   |
| `rotate_plate`         | Rotiert die Platte, auf der der Würfel steht. `times` bestimmt dabei die Anzahl an 90°-Drehungen.                                                                                                   |
| `arm_up`               | Bewegt den Arm hoch (90°).                                                                                                                                                                          |
| `arm_down`             | Bewegt den Arm runter (0°).                                                                                                                                                                         |

## Das Gesamte

Der Roboter verbindet sich nach dem Starten mit dem Server und wartet, bis der Server einen Befehl sendet und führt
diesen aus. Einzelne Befehle, wie das Einscannen eines Würfels, benötigen einen Rückgabewert.

Alle Befehle mit `type`:

| `type`              | Beschreibung                                                                                                          |
|---------------------|-----------------------------------------------------------------------------------------------------------------------|
| `start`             | Der Client macht gar nichts und speichert nur die in `config` gespeicherte Konfiguration.                             |
| `run_moves`         | Der Client führt die in `robot_moves` angegeben Züge aus und sendet nach jedem Teil den aktuellen Index an den Server |
| `scan_cube`         | Der Client scannt den Würfel ein und sendet die Farben and den Server.                                                |
| `wait_for_new_cube` | Der Client wartet, bis ein Würfel entfernt und wieder eingelegt wurde.                                                |

Am Anfang werden immer die folgenden Befehle gesendet: 
```json
[
  {
    "type": "start", "config": {
      "start_moves_before_scanning": [
        {"type": "rotate_cube_with_arm", "times": 4}
      ]
    }
  },
  {"type": "wait_for_new_cube"}
]
```