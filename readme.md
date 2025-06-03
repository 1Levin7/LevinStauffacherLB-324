# LB 324

## Aufgabe 2
## pre-commit verwenden

Mit pre-commit wird der Code beim Commit automatisch formatiert und beim Push geprüft.  
So wird sichergestellt, dass der Code immer sauber und getestet ist.

### Vorbereitung

Stelle sicher, dass Python und pip installiert sind.

### Schritte zur Einrichtung

1. **Terminal im Projektordner öffnen**  
   (z. B. in Visual Studio Code oder im Datei-Explorer mit Rechtsklick → „Terminal hier öffnen“)

2. **pre-commit installieren**

## bash
python -m pip install pre-commit

## pre-commit im Projekt aktivieren
python -m pre_commit install --> erwartetes ergebniss --> pre-commit installed at .git/hooks/pre-commit

## Manuelle Ausführung¨
python -m pre_commit run --all-files

## GitHub Actions

Bei jedem Pull Request auf den `dev`-Branch wird automatisch eine Test-Action ausgeführt.  
Diese prüft, ob die Applikation korrekt läuft.


## Aufgabe 4
Erklären Sie hier, wie Sie das Passwort aus Ihrer lokalen `.env` auf Azure übertragen.