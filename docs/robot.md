---
title: Der Roboter
---

# Der Roboter

![Der Roboter](/images/robot_1.jpg){ width="70%" }

///caption
Der Roboter
///

Der Roboter ist der Teil des Projekts, der mit der *echten* Welt interagiert. Er kann den Würfel einscannen und die 
Lösung ausführen, aufgrund mangelnder Rechenleistung aber nicht berechnen.

!!! info

    Der Roboter ist der [MindCub3r-Roboter von MindCuber.com](https://www.mindcuber.com/mindcub3r/mindcub3r.html). Das 
    Design variiert etwas, die Dekorationen sind nicht vorhanden.


Der Roboter besteht aus verschiedenen Teilen:

* Dem *Arm* (links), der den Würfel um die z-Achse dreht (nach links umklappt).
* Die *Platte* (mitte, unten), die den Würfel vertikal dreht.
* Der *Scanner* (rechts), der sich über den Würfel bewegt, um die Farben zu scannen.
* Der Abstandssensor (hinten), der prüft, ob sich ein Würfel im Roboter befindet.

Um eine Seite des Würfels zu drehen, bewegt der Roboter den Würfel mit dem Arm und der Platte erst so, dass die zu 
drehende Seite unten ist, und bewegt dann den Arm so, dass er die oberen zwei Reihen des Würfels festhält, damit die 
Platte anschließend die Seite drehen kann.
