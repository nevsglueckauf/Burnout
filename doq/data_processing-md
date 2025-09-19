# Projekt <i>Burnout der Arbeiterschaft, Vorhersage von Burnout bei Arbeitnehmern</i>
- Prosa folgt 

## Datenprozessierung

Die Daten der ursprünglichen auf [Kaggle](https://www.kaggle.com/datasets/blurredmachine/are-your-employees-burning-out?select=train.csv) publizierten Umfrage wurden als Excel-Datei von der IHK München zur Verfügung gestellt.

Hierbei wurde die Spalte <var>Burn Rate</var> bereits aus der Ursprungsdatei bereits kategorisiert als <var>Burn Risk</var>:

- <var>1</var> = <i>Hohes Risiko für Burnout</i> (>75% Risiko) und 
- <var>0</var> = <i>Kein Hohes Risiko für Burnout</i> (<=75% Risiko).



## Python modules and their relations

```mermaid
sequenceDiagram
autonumber
    
    box gray Datenquellen
        participant Originaldatei_Kaggle
        participant Datei_IHK
    end

    actor Gruppe_2

    box yellow Knime
        participant ExcelReader
        participant Sanitizer
        participant CSVWriter
    end

    box green PowerBI
        participant Dashboard
    end

     box lightblue Python
        participant PythonCore
        participant Pandas
        participant Seaborn
        participant NumPy
    end

     
    Gruppe_2->>ExcelReader: Einlesen der Datei
    CSVWriter->>Dashboard: Daten
     CSVWriter->>PythonCore: Daten
    Note right of Datei_IHK: Wurde kateg. Burnout_Risk

    
```