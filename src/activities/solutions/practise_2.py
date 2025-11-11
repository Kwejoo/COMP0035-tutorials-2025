from pathlib import Path
import pandas as pd
from pandas import DataFrame
# import matplotlib.pyplot as plt

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 0)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.expand_frame_repr", False)


def useful_columns(csv_file):
    cols = [
        'type', 'year', 'country', 'host', 'start', 'end',
        'countries', 'events', 'sports',
        'participants_m', 'participants_f', 'participants',
    ]

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
    event_type = "summer"

    df_winter = df.query("type == @event_type")
    print(df_winter)
    print(df_winter['country'].unique())


def remove_columns(df: DataFrame, columns_to_remove: list) -> DataFrame:
    """Removes specified columns from the DataFrame."""
    df_dropped = df.drop(columns=columns_to_remove)
    return df_dropped


def remove_columns_after(df: DataFrame, columns_to_remove: list) -> DataFrame:
    columns_to_remove = ['host', 'end', 'countries', 'events', 'sports']
    df1 = remove_columns(df, columns_to_remove)
    print(df1)
    print(df1.columns)


def remove_rows_with_missing_values(df: DataFrame) -> DataFrame:
    """Removes rows with any missing values from the DataFrame."""
    df_cleaned = df.dropna()
    return df_cleaned


def clean_types(df):
    """Clean and normalise the `type` column in-place.

    Actions performed:
    1. Strip whitespace from all values in the `type` column (fixes occurrences
       like `'winter '`).
    2. Locate rows where `type == "Summer"` and change them to lower-case
       using ``.str.lower()`` (so they become `'summer'`).

    Returns the modified DataFrame (the operation also mutates the input).
    """
    if 'type' not in df.columns:
        print("DataFrame has no 'type' column to clean")
        return df

    # 1) Strip whitespace from the entire column to remove entries like
    #    'winter'. This is easier and more reliable than fixing a single
    #    cell.
    print("Before stripping whitespace:\n", df['type'])
    print(df['type'].dtype)
    df['type'] = df['type'].str.strip()
    
    print("After stripping whitespace:\n", df['type'])

    # 2) Locate rows where `type == 'Summer'` (case-sensitive match) and
    #    normalise them to lowercase using .str.lower()
    summer_mask = df['type'] == 'Summer'
    print('summer mask\n', summer_mask)
    if summer_mask.any():
        print(df.loc[summer_mask, 'type'])
        df.loc[summer_mask, 'type'] = df.loc[summer_mask, 'type'].str.lower()

        print(f"Converted {summer_mask.sum()} 'Summer' row(s) to lowercase")

    # Show the resulting unique values for verification
    print("type column unique values:", df['type'].unique())
    return df


def change_types(df: DataFrame) -> DataFrame:
    """Change data types of specific columns in the DataFrame."""
    columns_to_change = [
        'countries',
        'events',
        'participants_m',
        'participants_f',
        'participants',
    ]

    for col in columns_to_change:
        df[col] = df[col].astype('int64')
    return df


if __name__ == "__main__":
    project_root = Path(__file__).parent.parent

    csv_file = project_root.joinpath('data', 'paralympics_raw.csv')
    df = pd.read_csv(csv_file)

    df = useful_columns(csv_file)
    print(df)

    clean_data(df)
    print(df)

    print(df.isna())
    df = remove_rows_with_missing_values(df)
    print(df)
    df = clean_types(df)

    print("Dtypes:\n", df.dtypes)
    df = change_types(df)
    print("Dtypes after change:\n", df.dtypes)

