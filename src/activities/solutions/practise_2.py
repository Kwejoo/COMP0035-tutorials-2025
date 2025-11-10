from pathlib import Path
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

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
    
    
        




if __name__ == "__main__":
    project_root = Path(__file__).parent.parent

    csv_file = project_root.joinpath('data', 'paralympics_raw.csv')
    df = pd.read_csv(csv_file)
    clean_data(df)