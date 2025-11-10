from pathlib import Path
import pandas as pd
from pandas import DataFrame


project_root = Path(__file__).parent.parent
#print(project_root)
csv_file = project_root.joinpath('data', 'paralympics_raw.csv')
#print(csv_file)
xlsx_file = project_root.joinpath('data', 'paralympics_all_raw.xlsx')
#print(xlsx_file)


df0 = pd.read_csv(csv_file)


dx0 = pd.read_excel(xlsx_file, sheet_name=0)

dx1 = pd.read_excel(xlsx_file, sheet_name=1)



def describe_dataframe(df: DataFrame, title: str = None) -> None:
    """Print a concise description of a pandas DataFrame.

    The function prints the DataFrame shape, column names, dtypes, a small
    preview (head and tail) and the output of
    ``DataFrame.describe(include='all')``.

    Args:
        df (pandas.DataFrame): The DataFrame to describe.

    Returns:
        None: This function prints output to stdout and returns None.

    Example:
        >>> describe_dataframe(df0)
    """
    if not isinstance(df, DataFrame):
        print("Input is not a pandas DataFrame")
        return

    # Print an optional title for clarity when multiple DataFrames are shown
    if title:
        print(f"\n=== {title} ===")
    else:
        print("\n=== DataFrame summary ===")
    print("Shape:", df.shape)
    print("Columns:", list(df.columns))
    print("Dtypes:\n", df.dtypes)
    print("\nInfo:")
    # DataFrame.info prints directly to stdout; call to show non-null counts
    # and memory usage as requested by the exercise.
    df.info()
    print("\nHead:")
    print(df.head())
    print("\nTail:")
    print(df.tail())
    print("\nDescribe (including non-numeric):")
    try:
        print(df.describe(include='all'))
    except Exception as exc:  # pragma: no cover - defensive
        print("Could not run describe():", exc)


# Use the new helper to describe each loaded sheet / CSV
describe_dataframe(df0, title=csv_file.name)
describe_dataframe(dx0, title=f"{xlsx_file.name} [sheet 0]")
describe_dataframe(dx1, title=f"{xlsx_file.name} [sheet 1]")


