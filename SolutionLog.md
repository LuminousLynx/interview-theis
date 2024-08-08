# Lösungs-Log

Diese Log-Datei enthält eine Auflistung meiner Vorgehensweisen zur Lösung der einzelnen Teilprobleme, wenn diese nicht bereits durch Commit-Messages ersichtlich sind.

## Lösung: Server Error 500
1) localhost:8081 im Browser nach Start des Programms in launch.json mit Django run config aufgerufen -> Server Error 500 wie erwartet
2) In settings.py DEBUG=True gesetzt um stacktrace im Browser zu erhalten und Fehler nachvollziehen zu können (nach fix -> DEBUG=False!!)
3) offensichtlich Fehler aus dem Template "overview.html", das von views.py zu rendern versucht wurde -> Fehler: forklift_forklift.next_check: no such column
4) Context der render-Methode ruft die Klasse Forklift aus models.py auf -> in models.py nach next_check gesucht
5) in models.py das DataField next_check auskommentiert -> Server startet und App zeigt beschriebene Kacheln


UPDATE: scratch 1-5. Migrated 0002_forklift_next_check.py. Works now. 

## Funktionsumfang
Lösung der Tickbox-Backends mit JSON und ajax. Probleme gab es bei Eingabefeldern mit Text bzw Daten: Parsen der Values mit JSON führte zu None-Werten im Backend und damit zu BadRequests. Zeitbedingter Workaround über Buttons mit Eingabefeldern. Nicht schön, aber funktioniert!

Facelift Interface als kleine Spielerei: Erste Berührung mit html templates!

alle funktionalitäten über PUT und json aus Zeitgründen

## Erweiterung 1
Zwei weitere DBs erstellt: Workshop für Werkstätten und Repair für einzelne Reparaturen.
Workshop DB wurde dabei schon um "niedrigster Durchschnittspreis" und einen "Reliability-Score" ergänzt - dies könnten spätere Kriterien für die Werkstattauswahl sein (z.B. Wähle zwischen schneller, günstiger oder zuverlässiger Reparatur je nach Bedarf).

Auto-Check noch nicht fertig implementiert, wirft noch bad request

## Erweiterung 2
Lösung über User groups vor rendering des GUI

