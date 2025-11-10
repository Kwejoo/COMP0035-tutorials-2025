from pathlib import Path

project_root = Path(__file__).parent.parent 
print(project_root)
csv_file = project_root.joinpath('solutions', 'practise.py')
print(csv_file)

if csv_file.exists():
    print(f"CSV file found: {csv_file}")
else:
    print("CSV file not found.")
