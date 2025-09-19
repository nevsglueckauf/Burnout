# Projekt <br><i>Burnout der Arbeiterschaft, <br>Vorhersage von Burnout bei Arbeitnehmern</i>


## Detailsicht auf ML

Aus dem Bereich des Machine Learning wurden Modelle benutzt, die:

- [Regression](https://de.wikipedia.org/wiki/Regressionsanalyse), oder 
- [Klassifizierung](https://de.wikipedia.org/wiki/Klassifizierung) nutzen, oder
- beides kombinieren



Die benutzten Machine Learning Modelle werden im folgenden beschrieben - die generelle Arbeitsweise ist: 

```mermaid
sequenceDiagram
autonumber

loop Acc >Baseline + x?
        Partitioner->>Learner: Trainingsdaten
        Partitioner->>Predictor: Testdaten
        Learner-->Predictor: Training
        Predictor->Scorer: Vorhersage
        Scorer->TableOutput: Bewertung
    end
```


-tbd

### K-Nearest Neighbors
-tbd

### Random Forest

-tbd
### Gradient Boosting

-tbd