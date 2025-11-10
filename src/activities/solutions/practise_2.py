from pathlib import Path
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

def useful_columns(csv_file):
    cols = ['type', 'year', 'country', 'host', 'start', 'end', 'countries', 'events', 'sports',
            'participants_m', 'participants_f', 'participants']

    df_selected_cols = pd.read_csv(csv_file, usecols=cols)

    return df_selected_cols

def clean_data(df: DataFrame) -> DataFrame:
    """Cleans the data by handling missing values and converting data types."""
    print(df['sports'])
    print(df.loc[7:9]['sports'])
    n1 = len(df.columns)
    list_columns = list(df.columns)
    print(list_columns)
    print(n1)
    print(df.iat[1, 3])
    for name in list_columns:
        print(df[name])
    event_type = "winter"


    df_winter = df.query("type == @event_type")
    print(df_winter)
    print(df_winter['country'].unique())
    
    
        
def remove_columns(df: DataFrame, columns_to_remove: list) -> DataFrame:
    """Removes specified columns from the DataFrame."""
    df_dropped = df.drop(columns=columns_to_remove)
    return df_dropped



if __name__ == "__main__":
    project_root = Path(__file__).parent.parent

    csv_file = project_root.joinpath('data', 'paralympics_raw.csv')
    df = pd.read_csv(csv_file)
    #clean_data(df)
    df = useful_columns(csv_file)
    print(df)
    clean_data(df)
    columns_to_remove = ['host', 'end', 'countries', 'events', 'sports']
    df = remove_columns(df, columns_to_remove)
    print(df)
    print(df.columns)