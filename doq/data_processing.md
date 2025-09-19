# Projekt <br><i>Burnout der Arbeiterschaft, <br>Vorhersage von Burnout bei Arbeitnehmern</i>
- Prosa folgt 

## Datenprozessierung

Die Daten der ursprünglichen auf [Kaggle](https://www.kaggle.com/datasets/blurredmachine/are-your-employees-burning-out?select=train.csv) publizierten Umfrage wurden als Excel-Datei von der IHK München zur Verfügung gestellt.

Hierbei wurde die Spalte <var>Burn Rate</var> bereits aus der Ursprungsdatei bereits kategorisiert als <var>Burn Risk</var>:

- <var>1</var> = <i>Hohes Risiko für Burnout</i> (```>75%``` Risiko) und 
- <var>0</var> = <i>Kein Hohes Risiko für Burnout</i> (```<=75%``` Risiko).

### Projektfluß (sehr grob)

```mermaid
sequenceDiagram
autonumber

box gray Datenquellen
        participant Datei_IHK
end

box yellow Knime
        participant Sanitizer
        participant EDA
        participant ML
        participant Baseline
end

box green PowerBI
        participant Dashboard
end

Datei_IHK->>Sanitizer:  
Sanitizer->>EDA:  
Sanitizer->>Dashboard:   
EDA->>Baseline:  
Sanitizer->>ML:  
```

### Überblick Datenprozessierung (grob)

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
        participant DataExplorer
        participant EDA
        participant ML
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
    ExcelReader->>Sanitizer: Datenbereinung (nans, unnötige Spalten )
    Sanitizer->>CSVWriter: Datenübergabe
    CSVWriter->>Dashboard: Datenübergabe
    CSVWriter->>PythonCore: Datenübergabe
    Sanitizer->>DataExplorer: Datenübergabe
    DataExplorer->>EDA: Datenübergabe
    EDA->>Baseline: Definition der Baseline
    DataExplorer->>ML: Datenübergabe
    PythonCore->>Pandas: Berechnungen
    Pandas->NumPy: Datenstrukturen & Algorithmen
    NumPy->>Pandas: Ergebnisse
    Pandas->Seaborn: Grafiken
    
```

### Detailsicht auf EDA

- tbd
- => Baseline Score: 

### ML-Modelle

Die erstellten ML-Modelle werden [hier](ml_models.md) detailliert beschrieben.