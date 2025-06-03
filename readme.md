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

### Wie wird das Passwort aus der lokalen `.env`-Datei auf Azure übertragen?

Die lokale Datei `.env` enthält sensible Umgebungsvariablen wie das `PASSWORD`. Diese Datei wird **nicht ins Repository hochgeladen**, sondern lokal verwendet. Damit das Passwort trotzdem sicher auf Azure verfügbar ist, wird folgender Mechanismus verwendet:

1. Der Inhalt der `.env`-Datei (z. B. `PASSWORD=1Levin7`) wird **nicht direkt übergeben**, sondern über ein **GitHub Repository Secret**.

2. In den Repository-Einstellungen unter  
   `Settings → Secrets and variables → Actions`  
   wird ein Secret namens `PASSWORD` erstellt und dort der Wert `1Levin7` gespeichert.

3. In der GitHub Action (`deploy.yml`) wird beim Deployment automatisch eine neue `.env`-Datei erzeugt, die das Secret einfügt:

   ```yaml
   - name: Set environment file
     run: echo "PASSWORD=${{ secrets.PASSWORD }}" > .env
