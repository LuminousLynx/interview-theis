# Stapler-Manager

## Beschreibung
Du arbeitest im SCM der flaschenpost GmbH im Jahre 2018. Es existiert bisher nur ein Lager in Münster, durch den großen Erfolg dort sind aber bereits weitere Standorte in Planung.

Zum Tracking der Flurförderfahrzeuge (FFZ) wurde von einem Praktikanten in seiner letzten Woche eine Django-App gestartet, womit Ausfälle der FFZ regisrtiert und Reparaturen angestoßen werden sollen.

Du sollst nun die Weiterentwicklung übernehmen, da bisher nur grundlegende Funktionen implementiert wurden und auch seit dem letzten Arbeitstag des Praktikanten die App gar nicht mehr nutzbar ist.

## Nötige Software
Installiere folgende Software, um am Projekt arbeiten zu können
- Git
- Python 3.11
- VisualStudio-Code (VSC)

## Installation
Nachdem du dieses Repository heruntergeladen hast, lege eine virtuelle Python-Umgebung an:
    
    python3.11 -m venv .venv
    
Installiere anschließend die in requirements.txt angegebenen Pakete.

Das Projekt sollte sich in VSC nun bereits durch die Datei .vscode/launch.json im Editor starten lassen. Es sollten auch bereits einige Datensätze in der db.sqlite3 vorhanden sein. Überprüfe den Start durch Aufruf von http://localhost:8081 im Browser.

## Server Error (500)
Leider wird dir hier bereits lediglich "Server Error" angezeigt, es scheint ein Problem zu geben. Finde das Problem und beschreibe deinen Lösungsweg.

## Funktionsumfang
Nachdem du das Problem gefunden und behoben hast, findest du dich auf der sehr rudimentären Oberfläche der Stapler-Verwaltung wieder. Dort sollte zu jedem bekannten FFZ eine Kachel vorhanden sein.

Im ersten Schritt sollen pro FFZ die eingewiesenen Personen einzutragen sein, die FFZ aktiviert und deaktiviert werden können, sowie die gelaufenen Stunden eintragbar sein. Teste, welche Funktionen bereits korrekt implementiert wurden und behebe ggfs. vorhandene Fehler. Beschreibe, wie du bei der Fehlersuche vorgegangen bist.

## Erweiterung - Teil 1
Um nicht nur den Status der FFZ einsehen zu können, sondern auch eine Reparatur bzw. UVV anzustoßen, sollen in einer zweiten Datenstruktur unsere Werkstattpartner inkl. E-Mail-Adresse abgelegt werden können:
- Jungheinrich AG (betreut ausschließlich Jungheinrich-FFZ)
- Becker Staplerservice GmbH (betreut herstellerübergreifend)
- Linde Hydraulics GmbH & Co. KG (betreut ausschließlich Linde)

Im Schadensfall soll aus einem der Partner ausgewählt werden können, sowie ein Mail-Anschreiben zur Reparatur erstellt werden (nur Text-Generierung, kein Versand!). Außerdem soll für anstehende UVV pro FFZ automatisch 2 Wochen vor Frist automatisch ein Auftrag generiert werden.

Dabei ist die Werkstatt vorauszuwählen, die bisher die schnellsten Reparaturen für das betroffene Model durchführen konnte. Entsprechend muss zu jeder Reparatur der Eintritt des Schadensfalles, sowie der Zeitpunkt der abgeschlossenen Reparatur mitgeschrieben werden.

Wähle dazu eine geeignete Erweiterung/Änderung der vorhandenen Datenstruktur und erläutere deine Wahl.

Beachte dabei auch, dass zukünftig weitere/andere Daten als die Reparaturdauer wichtig für die Auswahl der Werkstatt sein könnten. Erläutere dazu, welche Kriterien dies sein könnten und wie du sie berücksichtigst.

Natürlich soll ein Interface für die Eingabe der Daten durch die MA im Lager verfügbar sein. Passe also die bestehende GUI entsprechend an oder nutze das Django-eigene Admin-Interface. Begründe deine Wahl und präsentiere deine Lösung!

## Erweiterung - Teil 2
Wie bereits erwähnt, expandiert die flaschenpost in den nächsten Wochen. Dies sorgt für neue Anforderungen in den Interfaces, da nun die MA aus Münster natürlich nicht die FFZ der neuen Standorte sehen/bearbeiten sollen (und umgekehrt).

Darüber hinaus operiert "Becker Staplerservice GmbH" auschließlich im Münsterland, wohingegen in der neuen Region andere Werkstattpartner (mit anderen Bearbeitungszeiten) verfügbar sind.

Dies soll entsprechend in den Datenstrukturen, sowie der GUI angepasst werden. Entscheide selbst, welche Ansätze sinnvoll erscheinen und präsentiere deine Lösung.

## Anmerkungen
Insgesamt soll für das Lager ein möglichst einfach zu bedienendes und zuverlässiges Interface zur Verfügung stehen, welches mit möglichst wenigen Medienbrüchen auskommt und schnell erweiterbar ist.
Alle Funktionen im Backend sollten nach Möglichkeit durch Unit-Tests geprüft werden, nutze dazu bitte pytest.

## Optionale Zusatzaufgaben:
Sollten die Anforderungen oben die Vorbereitungszeit nicht auslasten, bzw. die 15 Minuten in der Präsentation nicht ausfüllen, stehen dir zwei (rein optionale) Zusatzaufgaben zur Verfügung:

### Aufgabe 1: Harmonisches Familienfest
Du verbringst Weihnachten mit der Familie. Jeder Verwandte bringt ein Geschenk mit. Ihr sitzt alle in einem nummerierten Kreis, beginnend mit Position 1. Dann, aufsteigend ab Sitzplatz 1, klaut ihr euch abwechselnd alle Geschenke von dem Verwandten zu eurer Linken. Ein Verwandter, der keine Geschenke hat, wird aus dem Kreis entfernt und ist ausgeschieden.

Zum Beispiel mit fünf Verwandten (nummeriert von 1 bis 5):

      1
    5   2
     4 3

- Verwandter 1 nimmt das Geschenk von Verwandtem 2.
- Verwandter 2 hat keine Geschenke und scheidet aus.
- Verwandter 3 nimmt das Geschenk von Verwandtem 4.
- Verwandter 4 hat keine Geschenke und scheidet ebenfalls aus
- Verwandter 5 nimmt die beiden Geschenke von Verwandtem 1.
- Verwandter 1 & 2 sind beide bereits ausgeschieden, werden also übersprungen.
- Verwandter 3 nimmt die drei Geschenke von Verwandtem 5.
Bei fünf Verwandten bekommt also der Verwandte, der an Position 3 sitzt, alle Geschenke.

Ihr erkennt allerdings schnell die Unsinnigkeit eurer Regeln für den Geschenketausch und vereinbart, stattdessen Geschenke von dem Verwandten zu stehlen, der direkt gegenüber im Kreis sitzt. Wenn sich zwei Verwandte gegenüber im Kreis befinden, wird derjenige bestohlen, der sich (aus Sicht des Stehlenden) links befindet. Die anderen Regeln bleiben unverändert: Verwandte, die keine Geschenke haben, werden ganz aus dem Kreis entfernt, und die anderen Verwandten rücken etwas nach, damit der Kreis gleichmäßig verteilt ist.

Welcher Platz bekommt alle Geschenke, wenn all deine 3012210 Cousins & Cousinen zu Besuch kommen? Erläutere deinen Lösungsweg!

### Aufgabe 2: flaschenpost-Kühlschrank
Du versuchst, dir Zugang zum einzigen sauberen flaschenpost-Kühlschrank zu verschaffen, der durch ein 4x4-Gitter aus kleinen, durch Türen verbundenen Räumen geschützt ist. Du beginnst im Raum oben links (mit S markiert) und kannst den Kühlschrank (mit V markiert) öffnen, sobald du den Raum unten rechts erreichst:

    #########
    #S| | | #
    #-#-#-#-#
    # | | | #
    #-#-#-#-#
    # | | | #
    #-#-#-#-#
    # | | |  
    ####### V

Feste Wände sind mit # gekennzeichnet, Türen mit - oder |.

Die Türen im aktuellen Raum sind entweder offen oder geschlossen (und verriegelt), basierend auf dem hexadezimalen MD5-Hash eines Passworts (pslxynzg), gefolgt von einer Folge von Großbuchstaben, die den bisher zurückgelegten Weg darstellen (U für oben, D für unten, L für links und R für rechts).

Nur die ersten vier Zeichen des Hashes werden verwendet; sie stehen jeweils für die Türen nach oben, unten, links und rechts von deiner aktuellen Position. Jedes b, c, d, e oder f bedeutet, dass die entsprechende Tür offen ist; jedes andere Zeichen (eine Zahl oder ein a) bedeutet, dass die entsprechende Tür geschlossen und verriegelt ist.

Welches ist der kürzeste Weg (der tatsächliche Weg, nicht nur die Länge), um den Kühlschrank zu erreichen? Beschreibe deinen Lösungsweg!

Beispiel-Lösungen:
Mit Passwort ihgpwlah, der kürzeste Weg wäre DDRRRD.
Mit Passwort kglvqrro, der kürzeste Weg wäre DDUDRLRRUDRD.
Mit Passwort ulqzkmiv, der kürzeste Weg wäre DRURDRUDDLLDLUURRDULRLDUUDDDRR.