
```mermaid
erDiagram
    Saba Weather {
    int Saba_id PK "NOT NULL, UNIQUE"
    int STN 
    date Date
    int Time (HH) "CHECK (HH BETWEEN 1 AND 24)"
    int Wind Direction (DD) "CHECK (DD BETWEEN 0 AND 360 OR DD = 990)"
    int Hourly Wind Speed (FH)
    int Mean Wind Speed (FF)
    int Max Gust (FX)
    int Temperature (T)
    int Minimum Temp (T10)
    int Dew Point Temp (TD) 
    int Sunshine duration (SQ)
    int Global radiation (Q)
    int Precipitation duration (DR)
    int Hourly precipitation (RH)
    int Air pressure (P)
    int Horizontal visibility (VV)
    int Cloud cover (N)
    int Relative atmospheric humidity  (U)
    int Weather Code  (WW) "CHECK (WW BETWEEN 0 AND 99)"
    int Indicator (IX) "CHECK (IX BETWEEN 1 AND 7)"
    int Fog (M) "CHECK (M BETWEEN 0 AND 1)"
    int Rainfall  (R) "CHECK (R BETWEEN 0 AND 1)"
    int Snow  (S) "CHECK (S BETWEEN 0 AND 1)"
    int Thunder (O) "CHECK (O BETWEEN 0 AND 1)"
    int Ice formation (Y) "CHECK (Y BETWEEN 0 AND 1)"
    }
```
    