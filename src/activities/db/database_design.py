from pathlib import Path
import pandas as pd


if __name__ == "__main__":
    project_root = Path(__file__).parent.parent

    xlsx_file = project_root.joinpath('data', 'paralympics_all_raw.xlsx')

    print(xlsx_file)
        # Count how many sheets are in the xlsx file and show their names
    xls_events = pd.read_excel(xlsx_file, sheet_name='games')
    xls_codes = pd.read_excel(xlsx_file, sheet_name='team_codes')

    print(xls_events.head())
    print(xls_codes.head())

