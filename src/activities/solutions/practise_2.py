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
    """Read CSV and return a DataFrame with a useful subset of columns.

    Parameters:
        csv_file (str | pathlib.Path): Path to the CSV file to read.

    Returns:
        pandas.DataFrame: DataFrame containing only the selected columns.
    """
    cols = [
        'type', 'year', 'country', 'host', 'start', 'end',
        'countries', 'events', 'sports',
        'participants_m', 'participants_f', 'participants',
    ]

    df_selected_cols = pd.read_csv(csv_file, usecols=cols)

    return df_selected_cols


def clean_data(df: DataFrame) -> DataFrame:
    """Run lightweight exploratory prints and simple queries on the DataFrame.

    This helper is intended for interactive exploration in the tutorial. It
    prints selected column values, basic shape information and a filtered
    subset for a specific event type. It does not modify the DataFrame.

    Parameters:
        df (pandas.DataFrame): Input DataFrame to inspect.

    Returns:
        pandas.DataFrame: The original DataFrame (unchanged).
    """
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
    """Remove a fixed list of columns from the DataFrame and print result.

    This wrapper removes a small set of columns commonly dropped in the
    exercises and prints the resulting frame and its column labels.

    Parameters:
        df (pandas.DataFrame): The input DataFrame.
        columns_to_remove (list): Ignored; the function uses a fixed list of
            columns to drop for the exercises.

    Returns:
        pandas.DataFrame: DataFrame with the selected columns removed.
    """
    columns_to_remove = ['host', 'end', 'countries', 'events', 'sports']
    df1 = remove_columns(df, columns_to_remove)
    print(df1)
    print(df1.columns)
    return df1


def remove_rows_with_missing_values(df: DataFrame) -> DataFrame:
    """Remove rows that contain any missing values (NaN) from the DataFrame.

    Parameters:
        df (pandas.DataFrame): Input DataFrame.

    Returns:
        pandas.DataFrame: A new DataFrame with rows containing NaNs removed.
    """
    df_cleaned = df.dropna()
    return df_cleaned


def clean_types(df: DataFrame) -> DataFrame:
    """Normalise values in the `type` column.

    The function performs two small normalisations that are useful for the
    exercises:
    - Strips leading/trailing whitespace from every value in the ``type``
      column (fixes entries such as ``'winter '``).
    - Locates any exact matches of ``'Summer'`` and converts those to lower
      case (resulting in ``'summer'``).

    The operation mutates the input DataFrame and also returns it for
    convenience.

    Parameters:
        df (pandas.DataFrame): Input DataFrame with a ``type`` column.

    Returns:
        pandas.DataFrame: The same DataFrame after modification.
    """
    if 'type' not in df.columns:
        print("DataFrame has no 'type' column to clean")
        return df

    # 1) Strip whitespace from the entire column to remove entries like
    #    'winter'. This is easier and more reliable than fixing a single
    #    cell.
    df['type'] = df['type'].astype(str).str.strip()

    # 2) Locate rows where `type == 'Summer'` (case-sensitive match) and
    #    normalise them to lowercase using .str.lower()
    summer_mask = df['type'] == 'Summer'
    if summer_mask.any():
        df.loc[summer_mask, 'type'] = df.loc[summer_mask, 'type'].str.lower()
        print(f"Converted {summer_mask.sum()} 'Summer' row(s) to lowercase")

    # Show the resulting unique values for verification
    print("type column unique values:", df['type'].unique())
    return df


def change_types(df: DataFrame) -> DataFrame:
    """Convert selected columns to appropriate numeric / datetime dtypes.

    This helper casts a set of participant and event-count columns to
    integer dtype and converts date-like columns (`start`, `end`) to
    pandas datetimes (using day-first parsing to match the CSV format).

    Parameters:
        df (pandas.DataFrame): Input DataFrame whose columns will be cast.

    Returns:
        pandas.DataFrame: DataFrame after dtype conversions.
    """
    columns_to_change = [
        'countries',
        'events',
        'participants_m',
        'participants_f',
        'participants',
    ]

    for col in columns_to_change:
        df[col] = df[col].astype('int64')

    cols = df.columns
    print(cols)

    for col in cols:
        print(f"Dtype of column '{col}': {df[col].dtype}")
        if col == 'start' or col == 'end':
            print(f"Converting column '{col}' to datetime")
            print(df[col].dtype)
            df[col] = pd.to_datetime(df[col], dayfirst=True)
            print(df[col].dtype)
    return df


def deep_clean(df: DataFrame) -> DataFrame:
    """Run a sequence of cleaning steps to prepare the DataFrame for analysis.

    This convenience function runs the helper functions used in the
    exercises: selects useful columns, drops missing rows, normalises the
    `type` column and converts types for numeric and date columns.

    Parameters:
        df (pandas.DataFrame): Raw DataFrame read from CSV.

    Returns:
        pandas.DataFrame: The cleaned DataFrame ready for analysis.
    """
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
    return df


def new_columns(df: DataFrame) -> DataFrame:
    """Add derived columns to the DataFrame.

    Currently this helper computes a `duration` column as the difference in
    days between the `end` and `start` datetimes. The result is inserted
    immediately after the `end` column.

    Parameters:
        df (pandas.DataFrame): Input DataFrame with datetime `start`/`end`.

    Returns:
        pandas.DataFrame: DataFrame with the new `duration` column added.
    """
    # Example: add new column 'duration' as diff between 'end' and 'start'
    duration_values = (df['end'] - df['start']).dt.days.astype('Int64')
    df.insert(df.columns.get_loc('end') + 1, 'duration', duration_values)
    return df


if __name__ == "__main__":
    project_root = Path(__file__).parent.parent

    csv_file = project_root.joinpath('data', 'paralympics_raw.csv')
    df = pd.read_csv(csv_file)

    df = deep_clean(df)
    print(df)

    df = new_columns(df)
    print(df)
    df.set_index('type', inplace=True)
    print(df)

    filepath = Path(__file__).parent.joinpath('output.csv')
    df.to_csv(filepath)
