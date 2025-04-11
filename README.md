# Automatische Briefkasten-Benachrichtigung

Ein Raspberry Pi-basiertes System zur automatischen Benachrichtigung per E-Mail, wenn Post in den Briefkasten eingeworfen wird.

## Projektübersicht

Dieses Projekt wurde im Rahmen eines Schulprojekts entwickelt, um automatische Benachrichtigungen über eingegangene Post zu ermöglichen. Sobald ein Brief in den Briefkasten geworfen wird, erkennt ein Lasersensor die Unterbrechung des Lichtstrahls und sendet eine E-Mail-Benachrichtigung an den konfigurierten Empfänger.

### Funktionsweise

1. Ein Lasersensor ist im Briefkasten installiert und mit einem Raspberry Pi verbunden
2. Die Software überwacht kontinuierlich den Sensorstatus
3. Wenn Post eingeworfen wird, unterbricht dies den Laserstrahl
4. Das System sendet sofort eine E-Mail-Benachrichtigung

## Technische Details

### Hardware-Anforderungen

- Raspberry Pi (getestet mit Raspberry Pi 3/4)
- Lasersensor (angeschlossen an GPIO Pin 17)
- Stromversorgung für den Raspberry Pi
- Internetverbindung (WLAN oder Ethernet)

### Software-Komponenten

Das Projekt ist in Python implementiert und besteht aus den folgenden Komponenten:

- **config.py**: Zentrale Konfigurationsdatei für Sensor-Pins und E-Mail-Einstellungen
- **email_service.py**: Modul zum Versenden von E-Mail-Benachrichtigungen
- **gpio_service.py**: Service für die Interaktion mit den GPIO-Pins und Ereigniserkennung
- **main.py**: Hauptprogramm, das alle Komponenten integriert und ausführt
- **test_email.py**: Hilfsskript zum Testen der E-Mail-Funktionalität

### Systemarchitektur

```
+----------------+    +----------------+    +----------------+
| Lasersensor    | -> | GPIO Service   | -> | Email Service  |
| (Hardware)     |    | (Erkennung)    |    | (Benachricht.) |
+----------------+    +----------------+    +----------------+
                           ^
                           |
                      +----------------+
                      | Config         |
                      | (Einstellungen)|
                      +----------------+
```

## Installation und Einrichtung

### Voraussetzungen

- Raspberry Pi mit installiertem Raspberry Pi OS
- Python 3.x
- Internetverbindung

### Installation

1. Repository klonen:
   ```
   git clone https://github.com/[username]/Automatic-Letter-Notification.git
   cd Automatic-Letter-Notification
   ```

2. Abhängigkeiten installieren:
   ```
   pip install RPi.GPIO
   ```

3. Konfiguration anpassen:
   Öffnen Sie `src/config.py` und passen Sie die folgenden Einstellungen an:
   - `sensorPin`: GPIO-Pin, an dem der Lasersensor angeschlossen ist
   - E-Mail-Konfiguration (SMTP-Server, Anmeldeinformationen, Empfänger)

### Hardware-Setup

1. Verbinden Sie den Lasersensor mit dem konfigurierten GPIO-Pin (standardmäßig Pin 17)
2. Platzieren Sie den Sensor im Briefkasten so, dass der Laserstrahl unterbrochen wird, wenn Post eingeworfen wird

## Ausführung

So starten Sie das Programm:

```
cd src
python main.py
```

Um nur die E-Mail-Funktionalität zu testen:

```
cd src
python test_email.py
```

## Funktionsweise im Detail

### Erkennungsmethoden

Das System unterstützt zwei Erkennungsmethoden:

1. **Interrupt-basierte Erkennung**: Das Programm reagiert sofort auf Änderungen des Sensorzustands
2. **Polling-basierte Erkennung**: Als Fallback, falls die Interrupt-Methode nicht funktioniert

### E-Mail-Benachrichtigung

Die E-Mail enthält eine einfache Benachrichtigung "Es ist Post im Briefkasten" und wird über den konfigurierten SMTP-Server versendet.

## Fehlerbehebung

### Häufige Probleme

- **Sensor erkennt nicht korrekt**: Überprüfen Sie die Platzierung des Sensors und testen Sie den GPIO-Pin manuell
- **E-Mail wird nicht gesendet**: Überprüfen Sie die SMTP-Einstellungen und führen Sie `test_email.py` aus
- **GPIO-Fehler**: Stellen Sie sicher, dass der richtige Pin in `config.py` konfiguriert ist

## Projektstruktur

```
Automatic-Letter-Notification/
├── README.md
├── .gitignore
└── src/
    ├── config.py
    ├── email_service.py
    ├── gpio_service.py
    ├── main.py
    └── test_email.py
```

## Weiterentwicklungsmöglichkeiten

- Integration einer Weboberfläche zur Überwachung des Briefkastenstatus
- Unterstützung für Push-Benachrichtigungen auf dem Smartphone
- Bilderfassung zur Bestätigung eingegangener Post
- Batteriebetrieb mit Energiesparfunktionen

## Autoren

- Name: [Ihr Name]
- Projektzeitraum: [Datum]
- Schule: [Schulname]

## Lizenz

Dieses Projekt steht unter [Ihre gewählte Lizenz] - siehe die LICENSE-Datei für Details.
