from pathlib import Path
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


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


def plot_timeseries(
    df: DataFrame,
    x: str = "start",
    y: str = "participants",
    savepath: str | None = None,
    show: bool = True,
) -> None:
    """Plot a simple time series of `y` versus `x` from a DataFrame.

    The function attempts to convert the `x` column to datetimes, groups by
    the x values and sums `y` (useful if there are multiple rows per date).

    Args:
        df: Source DataFrame.
        x: Column name to use for the x-axis (default: "start").
        y: Column name to use for the y-axis (default: "participants").
        savepath: Optional path to save the figure (PNG). If None the plot
            is only shown.
        show: If True, call ``plt.show()`` after drawing the figure.

    Returns:
        None: shows or saves a plot and returns None.
    """
    if x not in df.columns or y not in df.columns:
        print(f"Missing required columns for timeseries plot: {x!r} or {y!r}")
        return

    data = df.copy()
    # Try parsing dates with dayfirst=True (CSV appears to use dd/mm/YYYY).
    try:
        data[x] = pd.to_datetime(data[x], dayfirst=True)
    except Exception:
        try:
            data[x] = pd.to_datetime(data[x])
        except Exception:
            pass

    grouped = data.groupby(data[x])[y].sum().sort_index()

    fig, ax = plt.subplots(figsize=(10, 5))
    grouped.plot(ax=ax, marker="o")
    ax.set_title(f"{y} over {x}")
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.grid(True)

    if savepath:
        fig.savefig(savepath, bbox_inches="tight")
        print(f"Saved timeseries to {savepath}")
    # Improve layout and display
    plt.tight_layout()
    if show:
        plt.show()
    plt.close(fig)


def plot_timeseries_by_gender(
    df: DataFrame,
    x: str = "start",
    y: str = "participants",
    gender_col_candidates=None,
    savepath: str | None = None,
    show: bool = True,
) -> None:
    """Plot participants over time split by gender where possible.

    The function will try several strategies to detect gendered participant
    counts:
    - If there is a `gender`-like column and a `participants` column, it
      aggregates participants by (x, gender) and plots each gender as a line.
    - If explicit columns for male/female participant counts exist (for
      example `male_participants` / `female_participants`), it will plot
      those two series.

    This function is defensive: if it cannot find a sensible gender split it
    prints a message and returns.
    """
    if gender_col_candidates is None:
        gender_col_candidates = ["gender", "sex"]

    # direct male/female columns patterns to check
    pairs = [
        ("male_participants", "female_participants"),
        ("participants_male", "participants_female"),
        ("men", "women"),
    ]

    # Case 1: explicit male/female columns
    for mcol, fcol in pairs:
        if mcol in df.columns and fcol in df.columns:
            data = df.copy()
            try:
                data[x] = pd.to_datetime(data[x], dayfirst=True)
            except Exception:
                try:
                    data[x] = pd.to_datetime(data[x])
                except Exception:
                    pass
            grouped = data.groupby(data[x])[[mcol, fcol]].sum().sort_index()
            fig, ax = plt.subplots(figsize=(10, 5))
            grouped.plot(ax=ax, marker="o")
            ax.set_title(f"{y} by gender over {x}")
            ax.set_xlabel(x)
            ax.set_ylabel(y)
            ax.grid(True)
            if savepath:
                fig.savefig(savepath, bbox_inches="tight")
                print(f"Saved gender timeseries to {savepath}")
            if show:
                plt.show()
            plt.close(fig)
            return

    # Case 2: long-form gender column + participants column
    gender_col = None
    for cand in gender_col_candidates:
        if cand in df.columns and y in df.columns:
            gender_col = cand
            break

    if gender_col:
        data = df.copy()
        try:
            data[x] = pd.to_datetime(data[x], dayfirst=True)
        except Exception:
            try:
                data[x] = pd.to_datetime(data[x])
            except Exception:
                pass
        grouped = (
            data.groupby([data[x], data[gender_col]])[y]
            .sum()
            .unstack(fill_value=0)
        )
        fig, ax = plt.subplots(figsize=(10, 5))
        grouped.plot(ax=ax, marker="o")
        ax.set_title(f"{y} by {gender_col} over {x}")
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.grid(True)
        if savepath:
            fig.savefig(savepath, bbox_inches="tight")
            print(f"Saved gender timeseries to {savepath}")
        if show:
            plt.show()
        plt.close(fig)
        return

    print(
        "Could not find gendered participant counts in the DataFrame "
        "to split the plot."
    )


if __name__ == "__main__":
    project_root = Path(__file__).parent.parent

    csv_file = project_root.joinpath('data', 'paralympics_raw.csv')

    xlsx_file = project_root.joinpath('data', 'paralympics_all_raw.xlsx')
    df0 = pd.read_csv(csv_file)
    # Count how many sheets are in the xlsx file and show their names
    xls = pd.ExcelFile(xlsx_file)
    sheet_names = xls.sheet_names
    # Keep the printed line under 79 characters for style checks
    print(
        f"{xlsx_file.name} contains {len(sheet_names)} sheet(s): "
        f"{sheet_names}"
    )

    # Read and describe each sheet that actually exists in the workbook.
    # This is safer than hard-coding sheet indices; it will skip sheets that
    # cannot be read and print a warning instead of crashing.
    describe_dataframe(df0, title=csv_file.name)

    for sheet in sheet_names:
        try:
            df_sheet = pd.read_excel(xlsx_file, sheet_name=sheet)
        except Exception as exc:
            print(f"Warning: could not read sheet {sheet!r}: {exc}")
            continue
        # Use the sheet name in the title for clarity; it may be int or str
        describe_dataframe(
            df_sheet, title=f"{xlsx_file.name} [{sheet}]"
        )
        # Also plot timeseries for this sheet (participants over start)
        # and attempt a gender-split plot if the data supports it.
        plot_timeseries(df_sheet)
        plot_timeseries_by_gender(df_sheet)
    print('last')
    dx2 = pd.read_excel(xlsx_file, sheet_name=2, )

    print(dx2.isna().sum())
    print(dx2.isnull().sum())

    df1 = pd.read_csv(csv_file)
    # ax = pd.plotting.boxplot(df1)
    # plt.show()
    # print(df1)
    # df0_list = list(df0.columns)
    # print(df0_list)
    print(df1['country'].unique())
    print(df1['country'].value_counts())
    print(df1['type'].unique())
    print(df1['type'].value_counts())
    print(df1['disabilities_included'].unique())
    print(df1['disabilities_included'].value_counts())
