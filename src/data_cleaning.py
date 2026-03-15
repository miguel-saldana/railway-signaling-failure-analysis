# data_cleaning.py
# -------------------------------
# Modulo per caricare, pulire e calcolare KPI su dataset di guasti impianti ferroviari
# Tutti i commenti in italiano
# -------------------------------

import pandas as pd

def load_data(path):
    """
    Carica un file CSV e restituisce un DataFrame pandas.
    
    Parametri:
        path (str): percorso del file CSV
    Ritorno:
        df (DataFrame): dataset caricato
    """
    df = pd.read_csv(path)
    return df

def clean_data(df):
    """
    Pulisce il DataFrame:
    - converte la colonna 'date' in datetime
    - rimuove eventuali valori mancanti
    
    Parametri:
        df (DataFrame): dataset da pulire
    Ritorno:
        df (DataFrame): dataset pulito
    """
    # Converte la colonna data in formato datetime
    df["date"] = pd.to_datetime(df["date"])
    
    # Rimuove eventuali valori mancanti
    df = df.dropna()
    
    return df

def compute_kpi(df):
    """
    Calcola KPI principali:
    - numero di guasti per linea
    - tempo medio intervento per sistema
    
    Parametri:
        df (DataFrame): dataset pulito
    Ritorno:
        failures_by_line (Series): numero guasti per linea
        mean_intervention (Series): tempo medio intervento per sistema
    """
    # KPI 1: numero guasti per linea
    failures_by_line = df.groupby("line").size()
    
    # KPI 2: tempo medio intervento per sistema
    mean_intervention = df.groupby("system_type")["intervention_minutes"].mean()
    
    return failures_by_line, mean_intervention

